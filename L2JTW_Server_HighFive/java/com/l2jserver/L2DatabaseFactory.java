/*
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later
 * version.
 * 
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 */
package com.l2jserver;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

import javolution.util.FastMap;

import com.l2jserver.gameserver.ThreadPoolManager;
import com.mchange.v2.c3p0.ComboPooledDataSource;

/**
 * This class manages the database connections.
 */
public class L2DatabaseFactory
{
	private static final Logger _log = Logger.getLogger(L2DatabaseFactory.class.getName());
	
	/**
	 * The Enum ProviderType.
	 */
	public static enum ProviderType
	{
		MySql,
		MsSql
	}
	
	private static L2DatabaseFactory _instance;
	private static volatile ScheduledExecutorService _executor;
	private static Map<Connection, ScheduledFuture<?>> _connectionClosers = new FastMap<Connection, ScheduledFuture<?>>().shared();
	private ProviderType _providerType;
	private ComboPooledDataSource _source;
	
	/**
	 * Instantiates a new l2 database factory.
	 * @throws SQLException the SQL exception
	 */
	public L2DatabaseFactory() throws SQLException
	{
		try
		{
			if (Config.DATABASE_MAX_CONNECTIONS < 2)
			{
				Config.DATABASE_MAX_CONNECTIONS = 2;
				_log.warning("A minimum of " + Config.DATABASE_MAX_CONNECTIONS + " db connections are required.");
			}
			
			_source = new ComboPooledDataSource();
			_source.setAutoCommitOnClose(true);
			
			_source.setInitialPoolSize(10);
			_source.setMinPoolSize(10);
			_source.setMaxPoolSize(Math.max(10, Config.DATABASE_MAX_CONNECTIONS));
			
			_source.setAcquireRetryAttempts(0); // try to obtain connections indefinitely (0 = never quit)
			_source.setAcquireRetryDelay(500); // 500 milliseconds wait before try to acquire connection again
			_source.setCheckoutTimeout(0); // 0 = wait indefinitely for new connection
			// if pool is exhausted
			_source.setAcquireIncrement(5); // if pool is exhausted, get 5 more connections at a time
			// cause there is a "long" delay on acquire connection
			// so taking more than one connection at once will make connection pooling
			// more effective.
			
			// this "connection_test_table" is automatically created if not already there
			_source.setAutomaticTestTable("connection_test_table");
			_source.setTestConnectionOnCheckin(false);
			
			// testing OnCheckin used with IdleConnectionTestPeriod is faster than testing on checkout
			
			_source.setIdleConnectionTestPeriod(3600); // test idle connection every 60 sec
			_source.setMaxIdleTime(Config.DATABASE_MAX_IDLE_TIME); // 0 = idle connections never expire
			// *THANKS* to connection testing configured above
			// but I prefer to disconnect all connections not used
			// for more than 1 hour
			
			// enables statement caching, there is a "semi-bug" in c3p0 0.9.0 but in 0.9.0.2 and later it's fixed
			_source.setMaxStatementsPerConnection(100);
			
			_source.setBreakAfterAcquireFailure(false); // never fail if any way possible
			// setting this to true will make
			// c3p0 "crash" and refuse to work
			// till restart thus making acquire
			// errors "FATAL" ... we don't want that
			// it should be possible to recover
			_source.setDriverClass(Config.DATABASE_DRIVER);
			_source.setJdbcUrl(Config.DATABASE_URL);
			_source.setUser(Config.DATABASE_LOGIN);
			_source.setPassword(Config.DATABASE_PASSWORD);
			
			/* Test the connection */
			_source.getConnection().close();
			
			if (Config.DEBUG)
			{
				_log.fine("Database Connection Working");
			}
			
			if (Config.DATABASE_DRIVER.toLowerCase().contains("microsoft"))
			{
				_providerType = ProviderType.MsSql;
			}
			else
			{
				_providerType = ProviderType.MySql;
			}
		}
		catch (SQLException x)
		{
			if (Config.DEBUG)
			{
				_log.fine("Database Connection FAILED");
			}
			// re-throw the exception
			throw x;
		}
		catch (Exception e)
		{
			if (Config.DEBUG)
			{
				_log.fine("Database Connection FAILED");
			}
			throw new SQLException("Could not init DB connection:" + e.getMessage());
		}
	}
	
	/**
	 * Prepared query select.
	 * @param fields the fields
	 * @param tableName the table name
	 * @param whereClause the where clause
	 * @param returnOnlyTopRecord the return only top record
	 * @return the string
	 */
	public final String prepQuerySelect(String[] fields, String tableName, String whereClause, boolean returnOnlyTopRecord)
	{
		String msSqlTop1 = "";
		String mySqlTop1 = "";
		if (returnOnlyTopRecord)
		{
			if (getProviderType() == ProviderType.MsSql)
			{
				msSqlTop1 = " Top 1 ";
			}
			if (getProviderType() == ProviderType.MySql)
			{
				mySqlTop1 = " Limit 1 ";
			}
		}
		String query = "SELECT " + msSqlTop1 + safetyString(fields) + " FROM " + tableName + " WHERE " + whereClause + mySqlTop1;
		return query;
	}
	
	/**
	 * Shutdown.
	 */
	public void shutdown()
	{
		try
		{
			_source.close();
		}
		catch (Exception e)
		{
			_log.log(Level.INFO, "", e);
		}
		try
		{
			_source = null;
		}
		catch (Exception e)
		{
			_log.log(Level.INFO, "", e);
		}
	}
	
	/**
	 * Safety string.
	 * @param whatToCheck the what to check
	 * @return the string
	 */
	public final String safetyString(String... whatToCheck)
	{
		// NOTE: Use brace as a safety precaution just in case name is a reserved word
		final char braceLeft;
		final char braceRight;
		
		if (getProviderType() == ProviderType.MsSql)
		{
			braceLeft = '[';
			braceRight = ']';
		}
		else
		{
			braceLeft = '`';
			braceRight = '`';
		}
		
		int length = 0;
		
		for (String word : whatToCheck)
		{
			length += word.length() + 4;
		}
		
		final StringBuilder sbResult = new StringBuilder(length);
		
		for (String word : whatToCheck)
		{
			if (sbResult.length() > 0)
			{
				sbResult.append(", ");
			}
			
			sbResult.append(braceLeft);
			sbResult.append(word);
			sbResult.append(braceRight);
		}
		
		return sbResult.toString();
	}
	
	/**
	 * Gets the single instance of L2DatabaseFactory.
	 * @return single instance of L2DatabaseFactory
	 * @throws SQLException the SQL exception
	 */
	public static L2DatabaseFactory getInstance() throws SQLException
	{
		synchronized (L2DatabaseFactory.class)
		{
			if (_instance == null)
			{
				_instance = new L2DatabaseFactory();
			}
		}
		return _instance;
	}
	
	/**
	 * Gets the connection.
	 * @return the connection
	 */
	public Connection getConnection()
	{
		Connection con = null;
		while (con == null)
		{
			try
			{
				con = _source.getConnection();
				if (Server.serverMode == Server.MODE_GAMESERVER)
				{
					_connectionClosers.put(con, ThreadPoolManager.getInstance().scheduleGeneral(new ConnectionCloser(con, new RuntimeException()), Config.CONNECTION_CLOSE_TIME));
				}
				else
				{
					getExecutor().schedule(new ConnectionCloser(con, new RuntimeException()), 60, TimeUnit.SECONDS);
				}
			}
			catch (SQLException e)
			{
				_log.log(Level.WARNING, "L2DatabaseFactory: getConnection() failed, trying again " + e.getMessage(), e);
			}
		}
		return con;
	}
	
	/**
	 * The Class ConnectionCloser.
	 */
	private static class ConnectionCloser implements Runnable
	{
		private static final Logger _log = Logger.getLogger(ConnectionCloser.class.getName());
		
		/** The connection. */
		private final Connection c;
		
		/** The exception. */
		private final RuntimeException exp;
		
		/**
		 * Instantiates a new connection closer.
		 * @param con the con
		 * @param e the e
		 */
		public ConnectionCloser(Connection con, RuntimeException e)
		{
			c = con;
			exp = e;
		}
		
		@Override
		public void run()
		{
			try
			{
				if (!c.isClosed())
				{
					_log.log(Level.WARNING, "Unclosed connection! Trace: " + exp.getStackTrace()[1], exp);
				}
			}
			catch (SQLException e)
			{
				_log.log(Level.WARNING, "", e);
			}
		}
	}
	
	/**
	 * Close the connection.
	 * @param con the con
	 */
	public static void close(Connection con)
	{
		if (con == null)
		{
			return;
		}
		
		try
		{
			con.close();
			ScheduledFuture<?> conCloser = _connectionClosers.remove(con);
			if (conCloser != null)
			{
				conCloser.cancel(true);
				conCloser = null;
			}
		}
		catch (SQLException e)
		{
			_log.log(Level.WARNING, "Failed to close database connection!", e);
		}
	}
	
	/**
	 * Gets the executor.
	 * @return the executor
	 */
	private static ScheduledExecutorService getExecutor()
	{
		if (_executor == null)
		{
			synchronized (L2DatabaseFactory.class)
			{
				if (_executor == null)
				{
					_executor = Executors.newSingleThreadScheduledExecutor();
				}
			}
		}
		return _executor;
	}
	
	/**
	 * Gets the busy connection count.
	 * @return the busy connection count
	 * @throws SQLException the SQL exception
	 */
	public int getBusyConnectionCount() throws SQLException
	{
		return _source.getNumBusyConnectionsDefaultUser();
	}
	
	/**
	 * Gets the idle connection count.
	 * @return the idle connection count
	 * @throws SQLException the SQL exception
	 */
	public int getIdleConnectionCount() throws SQLException
	{
		return _source.getNumIdleConnectionsDefaultUser();
	}
	
	/**
	 * Gets the provider type.
	 * @return the provider type
	 */
	public final ProviderType getProviderType()
	{
		return _providerType;
	}
}
