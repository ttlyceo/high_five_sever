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
package com.l2jserver.gameserver.model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ScheduledFuture;
import java.util.logging.Level;
import java.util.logging.Logger;

import javolution.util.FastList;
import javolution.util.FastMap;

import com.l2jserver.Config;
import com.l2jserver.L2DatabaseFactory;
import com.l2jserver.gameserver.SevenSigns;
import com.l2jserver.gameserver.ThreadPoolManager;
import com.l2jserver.gameserver.model.actor.L2Character;
import com.l2jserver.gameserver.model.actor.L2Npc;
import com.l2jserver.gameserver.model.actor.instance.L2DefenderInstance;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.network.clientpackets.Say2;
import com.l2jserver.gameserver.network.serverpackets.CreatureSay;
import com.l2jserver.util.Rnd;

/**
 * Auto Chat Handler
 *
 * Allows NPCs to automatically send messages to nearby players
 * at a set time interval.
 *
 * @author Tempy
 */
public class AutoChatHandler implements SpawnListener
{
	protected static final Logger _log = Logger.getLogger(AutoChatHandler.class.getName());
	
	private static final int DEFAULT_CHAT_DELAY = 60000; // 60 secs by default
	
	protected Map<Integer, AutoChatInstance> _registeredChats;
	
	protected AutoChatHandler()
	{
		_registeredChats = new FastMap<>();
		restoreChatData();
		L2Spawn.addSpawnListener(this);
	}
	
	private void restoreChatData()
	{
		int numLoaded = 0;
		Connection con = null;
		try
		{
			con = L2DatabaseFactory.getInstance().getConnection();
			
			PreparedStatement statement = con.prepareStatement("SELECT * FROM auto_chat ORDER BY groupId ASC");
			ResultSet rs = statement.executeQuery();
			
			PreparedStatement statement2 = con.prepareStatement("SELECT * FROM auto_chat_text WHERE groupId=?");
			while (rs.next())
			{
				numLoaded++;
				
				statement2.setInt(1, rs.getInt("groupId"));
				ResultSet rs2 = statement2.executeQuery();
				statement2.clearParameters();
				
				rs2.last();
				String[] chatTexts = new String[rs2.getRow()];
				int i = 0;
				rs2.beforeFirst();
				
				while (rs2.next())
				{
					chatTexts[i++] = rs2.getString("chatText");
				}
				
				registerGlobalChat(rs.getInt("npcId"), chatTexts, rs.getLong("chatDelay"));
			}
			statement2.close();
			rs.close();
			statement.close();
			
			if (Config.DEBUG)
				_log.info("AutoChatHandler: Loaded " + numLoaded + " chat group(s) from the database.");
		}
		catch (Exception e)
		{
			_log.log(Level.WARNING, "AutoSpawnHandler: Could not restore chat data: " + e.getMessage(), e);
		}
		finally
		{
			L2DatabaseFactory.close(con);
		}
	}
	
	public void reload()
	{
		// unregister all registered spawns
		for (AutoChatInstance aci : _registeredChats.values())
		{
			if (aci != null)
			{
				// clear timer
				if (aci._chatTask != null)
					aci._chatTask.cancel(true);
				this.removeChat(aci);
			}
		}
		
		// create clean list
		_registeredChats = new FastMap<>();
		
		// load
		restoreChatData();
	}
	
	public static AutoChatHandler getInstance()
	{
		return SingletonHolder._instance;
	}
	
	public int size()
	{
		return _registeredChats.size();
	}
	
	/**
	 * Registers a globally active auto chat for ALL instances of the given NPC ID.
	 * <BR>
	 * Returns the associated auto chat instance.
	 *
	 * @param npcId
	 * @param chatTexts
	 * @param chatDelay (-1 = default delay)
	 * @return AutoChatInstance chatInst
	 */
	public AutoChatInstance registerGlobalChat(int npcId, String[] chatTexts, long chatDelay)
	{
		return registerChat(npcId, null, chatTexts, chatDelay);
	}
	
	/**
	 * Registers a NON globally-active auto chat for the given NPC instance, and adds to the currently
	 * assigned chat instance for this NPC ID, otherwise creates a new instance if
	 * a previous one is not found.
	 * <BR>
	 * Returns the associated auto chat instance.
	 *
	 * @param npcInst
	 * @param chatTexts
	 * @param chatDelay (-1 = default delay)
	 * @return AutoChatInstance chatInst
	 */
	public AutoChatInstance registerChat(L2Npc npcInst, String[] chatTexts, long chatDelay)
	{
		return registerChat(npcInst.getNpcId(), npcInst, chatTexts, chatDelay);
	}
	
	private final AutoChatInstance registerChat(int npcId, L2Npc npcInst, String[] chatTexts, long chatDelay)
	{
		AutoChatInstance chatInst = null;
		
		if (chatDelay < 0)
			chatDelay = DEFAULT_CHAT_DELAY + Rnd.nextInt(DEFAULT_CHAT_DELAY);
		
		if (_registeredChats.containsKey(npcId))
			chatInst = _registeredChats.get(npcId);
		else
			chatInst = new AutoChatInstance(npcId, chatTexts, chatDelay, (npcInst == null));
		
		if (npcInst != null)
			chatInst.addChatDefinition(npcInst);
		
		_registeredChats.put(npcId, chatInst);
		
		return chatInst;
	}
	
	/**
	 * Removes and cancels ALL auto chat definition for the given NPC ID,
	 * and removes its chat instance if it exists.
	 *
	 * @param npcId
	 * @return removedSuccessfully
	 */
	public boolean removeChat(int npcId)
	{
		AutoChatInstance chatInst = _registeredChats.get(npcId);
		return removeChat(chatInst);
	}
	
	/**
	 * Removes and cancels ALL auto chats for the given chat instance.
	 *
	 * @param chatInst
	 * @return {@code true} if the chat is removed successfully.
	 */
	public boolean removeChat(AutoChatInstance chatInst)
	{
		if (chatInst == null)
			return false;
		
		_registeredChats.remove(chatInst.getNPCId());
		chatInst.setActive(false);
		
		if (Config.DEBUG)
			_log.info("AutoChatHandler: Removed auto chat for NPC ID " + chatInst.getNPCId());
		
		return true;
	}
	
	/**
	 * Returns the associated auto chat instance either by the given NPC ID
	 * or object ID.
	 *
	 * @param id
	 * @param byObjectId
	 * @return AutoChatInstance chatInst
	 */
	public AutoChatInstance getAutoChatInstance(int id, boolean byObjectId)
	{
		if (!byObjectId)
			return _registeredChats.get(id);
		
		for (AutoChatInstance chatInst : _registeredChats.values())
			if (chatInst.getChatDefinition(id) != null)
				return chatInst;
		
		return null;
	}
	
	/**
	 * Sets the active state of all auto chat instances to that specified,
	 * and cancels the scheduled chat task if necessary.
	 *
	 * @param isActive
	 */
	public void setAutoChatActive(boolean isActive)
	{
		for (AutoChatInstance chatInst : _registeredChats.values())
			chatInst.setActive(isActive);
	}
	
	/**
	 * Used in conjunction with a SpawnListener, this method is called every time
	 * an NPC is spawned in the world.
	 * <BR><BR>
	 * If an auto chat instance is set to be "global", all instances matching the registered
	 * NPC ID will be added to that chat instance.
	 * @param npc 
	 */
	@Override
	public void npcSpawned(L2Npc npc)
	{
		synchronized (_registeredChats)
		{
			if (npc == null)
				return;
			
			int npcId = npc.getNpcId();
			
			if (_registeredChats.containsKey(npcId))
			{
				AutoChatInstance chatInst = _registeredChats.get(npcId);
				
				if (chatInst != null && chatInst.isGlobal())
					chatInst.addChatDefinition(npc);
			}
		}
	}
	
	/**
	 * Auto Chat Instance
	 * <BR><BR>
	 * Manages the auto chat instances for a specific registered NPC ID.
	 *
	 * @author Tempy
	 */
	public class AutoChatInstance
	{
		protected int _npcId;
		private long _defaultDelay = DEFAULT_CHAT_DELAY;
		private String[] _defaultTexts;
		private boolean _defaultRandom = false;
		
		private boolean _globalChat = false;
		private boolean _isActive;
		
		private Map<Integer, AutoChatDefinition> _chatDefinitions = new FastMap<>();
		protected ScheduledFuture<?> _chatTask;
		
		protected AutoChatInstance(int npcId, String[] chatTexts, long chatDelay, boolean isGlobal)
		{
			_defaultTexts = chatTexts;
			_npcId = npcId;
			_defaultDelay = chatDelay;
			_globalChat = isGlobal;
			
			if (Config.DEBUG)
				_log.info("AutoChatHandler: Registered auto chat for NPC ID " + _npcId + " (Global Chat = " + _globalChat + ").");
			
			setActive(true);
		}
		
		protected AutoChatDefinition getChatDefinition(int objectId)
		{
			return _chatDefinitions.get(objectId);
		}
		
		protected AutoChatDefinition[] getChatDefinitions()
		{
			return _chatDefinitions.values().toArray(new AutoChatDefinition[_chatDefinitions.values().size()]);
		}
		
		/**
		 * Defines an auto chat for an instance matching this auto chat instance's registered NPC ID,
		 * and launches the scheduled chat task.
		 * <BR>
		 * Returns the object ID for the NPC instance, with which to refer
		 * to the created chat definition.
		 * <BR>
		 * <B>Note</B>: Uses pre-defined default values for texts and chat delays from the chat instance.
		 * @param npcInst
		 * @return
		 */
		public int addChatDefinition(L2Npc npcInst)
		{
			return addChatDefinition(npcInst, null, 0);
		}
		
		/**
		 * Defines an auto chat for an instance matching this auto chat instance's registered NPC ID,
		 * and launches the scheduled chat task.
		 * <BR>
		 * Returns the object ID for the NPC instance, with which to refer
		 * to the created chat definition.
		 *
		 * @param npcInst
		 * @param chatTexts
		 * @param chatDelay
		 * @return objectId
		 */
		public int addChatDefinition(L2Npc npcInst, String[] chatTexts, long chatDelay)
		{
			int objectId = npcInst.getObjectId();
			AutoChatDefinition chatDef = new AutoChatDefinition(this, npcInst, chatTexts, chatDelay);
			if (npcInst instanceof L2DefenderInstance)
				chatDef.setRandomChat(true);
			_chatDefinitions.put(objectId, chatDef);
			return objectId;
		}
		
		/**
		 * Removes a chat definition specified by the given object ID.
		 *
		 * @param objectId
		 * @return {@code true} if the chat is removed successfully.
		 */
		public boolean removeChatDefinition(int objectId)
		{
			if (!_chatDefinitions.containsKey(objectId))
				return false;
			
			AutoChatDefinition chatDefinition = _chatDefinitions.get(objectId);
			chatDefinition.setActive(false);
			
			_chatDefinitions.remove(objectId);
			
			return true;
		}
		
		/**
		 * Tests if this auto chat instance is active.
		 *
		 * @return boolean isActive
		 */
		public boolean isActive()
		{
			return _isActive;
		}
		
		/**
		 * Tests if this auto chat instance applies to
		 * ALL currently spawned instances of the registered NPC ID.
		 *
		 * @return boolean isGlobal
		 */
		public boolean isGlobal()
		{
			return _globalChat;
		}
		
		/**
		 * Tests if random order is the DEFAULT for new chat definitions.
		 *
		 * @return boolean isRandom
		 */
		public boolean isDefaultRandom()
		{
			return _defaultRandom;
		}
		
		/**
		 * Tests if the auto chat definition given by its object ID is set to be random.
		 * @param objectId 
		 * @return boolean isRandom
		 */
		public boolean isRandomChat(int objectId)
		{
			if (!_chatDefinitions.containsKey(objectId))
				return false;
			
			return _chatDefinitions.get(objectId).isRandomChat();
		}
		
		/**
		 * Returns the ID of the NPC type managed by this auto chat instance.
		 *
		 * @return int npcId
		 */
		public int getNPCId()
		{
			return _npcId;
		}
		
		/**
		 * Returns the number of auto chat definitions stored for this instance.
		 *
		 * @return int definitionCount
		 */
		public int getDefinitionCount()
		{
			return _chatDefinitions.size();
		}
		
		/**
		 * Returns a list of all NPC instances handled by this auto chat instance.
		 *
		 * @return L2NpcInstance[] npcInsts
		 */
		public L2Npc[] getNPCInstanceList()
		{
			List<L2Npc> npcInsts = new FastList<>();
			
			for (AutoChatDefinition chatDefinition : _chatDefinitions.values())
				npcInsts.add(chatDefinition._npcInstance);
			
			return npcInsts.toArray(new L2Npc[npcInsts.size()]);
		}
		
		/**
		 * A series of methods used to get and set default values for new chat definitions.
		 * @return 
		 */
		public long getDefaultDelay()
		{
			return _defaultDelay;
		}
		
		public String[] getDefaultTexts()
		{
			return _defaultTexts;
		}
		
		public void setDefaultChatDelay(long delayValue)
		{
			_defaultDelay = delayValue;
		}
		
		public void setDefaultChatTexts(String[] textsValue)
		{
			_defaultTexts = textsValue;
		}
		
		public void setDefaultRandom(boolean randValue)
		{
			_defaultRandom = randValue;
		}
		
		/**
		 * Sets a specific chat delay for the specified auto chat definition given by its object ID.
		 *
		 * @param objectId
		 * @param delayValue
		 */
		public void setChatDelay(int objectId, long delayValue)
		{
			AutoChatDefinition chatDef = getChatDefinition(objectId);
			
			if (chatDef != null)
				chatDef.setChatDelay(delayValue);
		}
		
		/**
		 * Sets a specific set of chat texts for the specified auto chat definition given by its object ID.
		 *
		 * @param objectId
		 * @param textsValue
		 */
		public void setChatTexts(int objectId, String[] textsValue)
		{
			AutoChatDefinition chatDef = getChatDefinition(objectId);
			
			if (chatDef != null)
				chatDef.setChatTexts(textsValue);
		}
		
		/**
		 * Sets specifically to use random chat order for the auto chat definition given by its object ID.
		 *
		 * @param objectId
		 * @param randValue
		 */
		public void setRandomChat(int objectId, boolean randValue)
		{
			AutoChatDefinition chatDef = getChatDefinition(objectId);
			
			if (chatDef != null)
				chatDef.setRandomChat(randValue);
		}
		
		/**
		 * Sets the activity of ALL auto chat definitions handled by this chat instance.
		 *
		 * @param activeValue
		 */
		public void setActive(boolean activeValue)
		{
			if (_isActive == activeValue)
				return;
			
			_isActive = activeValue;
			
			if (!isGlobal())
			{
				for (AutoChatDefinition chatDefinition : _chatDefinitions.values())
					chatDefinition.setActive(activeValue);
				
				return;
			}
			
			if (isActive())
			{
				AutoChatRunner acr = new AutoChatRunner(_npcId, -1);
				_chatTask = ThreadPoolManager.getInstance().scheduleGeneralAtFixedRate(acr, _defaultDelay, _defaultDelay);
			}
			else
			{
				_chatTask.cancel(false);
			}
		}
		
		/**
		 * Auto Chat Definition
		 * <BR><BR>
		 * Stores information about specific chat data for an instance of the NPC ID
		 * specified by the containing auto chat instance.
		 * <BR>
		 * Each NPC instance of this type should be stored in a subsequent AutoChatDefinition class.
		 *
		 * @author Tempy
		 */
		private class AutoChatDefinition
		{
			protected int _chatIndex = 0;
			protected L2Npc _npcInstance;
			
			protected AutoChatInstance _chatInstance;
			
			private long _chatDelay = 0;
			private String[] _chatTexts = null;
			private boolean _isActiveDefinition;
			private boolean _randomChat;
			
			protected AutoChatDefinition(AutoChatInstance chatInst, L2Npc npcInst, String[] chatTexts, long chatDelay)
			{
				_npcInstance = npcInst;
				
				_chatInstance = chatInst;
				_randomChat = chatInst.isDefaultRandom();
				
				_chatDelay = chatDelay;
				_chatTexts = chatTexts;
				
				if (Config.DEBUG)
					_log.info("AutoChatHandler: Chat definition added for NPC ID " + _npcInstance.getNpcId() + " (Object ID = "
							+ _npcInstance.getObjectId() + ").");
				
				// If global chat isn't enabled for the parent instance,
				// then handle the chat task locally.
				if (!chatInst.isGlobal())
					setActive(true);
			}
			
			protected String[] getChatTexts()
			{
				if (_chatTexts != null)
					return _chatTexts;
				
				return _chatInstance.getDefaultTexts();
			}
			
			private long getChatDelay()
			{
				if (_chatDelay > 0)
					return _chatDelay;
				
				return _chatInstance.getDefaultDelay();
			}
			
			private boolean isActive()
			{
				return _isActiveDefinition;
			}
			
			boolean isRandomChat()
			{
				return _randomChat;
			}
			
			void setRandomChat(boolean randValue)
			{
				_randomChat = randValue;
			}
			
			void setChatDelay(long delayValue)
			{
				_chatDelay = delayValue;
			}
			
			void setChatTexts(String[] textsValue)
			{
				_chatTexts = textsValue;
			}
			
			void setActive(boolean activeValue)
			{
				if (isActive() == activeValue)
					return;
				
				if (activeValue)
				{
					AutoChatRunner acr = new AutoChatRunner(_npcId, _npcInstance.getObjectId());
					if (getChatDelay() == 0)
						// Schedule it set to 5Ms, isn't error, if use 0 sometime
						// chatDefinition return null in AutoChatRunner
						_chatTask = ThreadPoolManager.getInstance().scheduleGeneral(acr, 5);
					else
						_chatTask = ThreadPoolManager.getInstance().scheduleGeneralAtFixedRate(acr, getChatDelay(), getChatDelay());
				}
				else
				{
					_chatTask.cancel(false);
				}
				
				_isActiveDefinition = activeValue;
			}
		}
		
		/**
		 * Auto Chat Runner
		 * <BR><BR>
		 * Represents the auto chat scheduled task for each chat instance.
		 *
		 * @author Tempy
		 */
		private class AutoChatRunner implements Runnable
		{
			private int _runnerNpcId;
			private int _objectId;
			
			protected AutoChatRunner(int pNpcId, int pObjectId)
			{
				_runnerNpcId = pNpcId;
				_objectId = pObjectId;
			}
			
			@Override
			public synchronized void run()
			{
				AutoChatInstance chatInst = _registeredChats.get(_runnerNpcId);
				AutoChatDefinition[] chatDefinitions;
				
				if (chatInst.isGlobal())
				{
					chatDefinitions = chatInst.getChatDefinitions();
				}
				else
				{
					AutoChatDefinition chatDef = chatInst.getChatDefinition(_objectId);
					
					if (chatDef == null)
					{
						_log.warning("AutoChatHandler: Auto chat definition is NULL for NPC ID " + _npcId + ".");
						return;
					}
					
					chatDefinitions = new AutoChatDefinition[] { chatDef };
				}
				
				if (Config.DEBUG)
					_log.info("AutoChatHandler: Running auto chat for " + chatDefinitions.length + " instances of NPC ID " + _npcId + "."
							+ " (Global Chat = " + chatInst.isGlobal() + ")");
				
				for (AutoChatDefinition chatDef : chatDefinitions)
				{
					try
					{
						L2Npc chatNpc = chatDef._npcInstance;
						List<L2PcInstance> nearbyPlayers = new FastList<>();
						List<L2PcInstance> nearbyGMs = new FastList<>();
						
						for (L2Character player : chatNpc.getKnownList().getKnownCharactersInRadius(1500))
						{
							if (!(player instanceof L2PcInstance))
								continue;
							
							if (((L2PcInstance) player).isGM())
								nearbyGMs.add((L2PcInstance) player);
							else
								nearbyPlayers.add((L2PcInstance) player);
						}
						
						int maxIndex = chatDef.getChatTexts().length;
						int lastIndex = Rnd.nextInt(maxIndex);
						
						String creatureName = chatNpc.getName();
						String text;
						
						if (!chatDef.isRandomChat())
						{
							lastIndex = chatDef._chatIndex + 1;
							
							if (lastIndex == maxIndex)
								lastIndex = 0;
							
							chatDef._chatIndex = lastIndex;
						}
						
						text = chatDef.getChatTexts()[lastIndex];
						
						if (text == null)
							return;
						
						if (!nearbyPlayers.isEmpty())
						{
							int randomPlayerIndex = Rnd.nextInt(nearbyPlayers.size());
							
							L2PcInstance randomPlayer = nearbyPlayers.get(randomPlayerIndex);
							
							final int winningCabal = SevenSigns.getInstance().getCabalHighestScore();
							int losingCabal = SevenSigns.CABAL_NULL;
							
							if (winningCabal == SevenSigns.CABAL_DAWN)
								losingCabal = SevenSigns.CABAL_DUSK;
							else if (winningCabal == SevenSigns.CABAL_DUSK)
								losingCabal = SevenSigns.CABAL_DAWN;
							
							if (text.indexOf("%player_random%") > -1)
								text = text.replaceAll("%player_random%", randomPlayer.getName());
							
							if (text.indexOf("%player_cabal_winner%") > -1)
							{
								for (L2PcInstance nearbyPlayer : nearbyPlayers)
								{
									if (SevenSigns.getInstance().getPlayerCabal(nearbyPlayer.getObjectId()) == winningCabal)
									{
										text = text.replaceAll("%player_cabal_winner%", nearbyPlayer.getName());
										break;
									}
								}
							}
							
							if (text.indexOf("%player_cabal_loser%") > -1)
							{
								for (L2PcInstance nearbyPlayer : nearbyPlayers)
								{
									if (SevenSigns.getInstance().getPlayerCabal(nearbyPlayer.getObjectId()) == losingCabal)
									{
										text = text.replaceAll("%player_cabal_loser%", nearbyPlayer.getName());
										break;
									}
								}
							}
						}
						
						if (text == null)
							return;
						
						if (!text.contains("%player_"))
						{
							CreatureSay cs = new CreatureSay(chatNpc.getObjectId(), Say2.ALL, creatureName, text);
							
							for (L2PcInstance nearbyPlayer : nearbyPlayers)
								nearbyPlayer.sendPacket(cs);
							for (L2PcInstance nearbyGM : nearbyGMs)
								nearbyGM.sendPacket(cs);
						}
						
						if (Config.DEBUG)
							_log.fine("AutoChatHandler: Chat propogation for object ID " + chatNpc.getObjectId() + " (" + creatureName
									+ ") with text '" + text + "' sent to " + nearbyPlayers.size() + " nearby players.");
					}
					catch (Exception e)
					{
						_log.log(Level.WARNING, "Exception on AutoChatRunner.run(): " + e.getMessage(), e);
						return;
					}
				}
			}
		}
	}
	
	private static class SingletonHolder
	{
		protected static final AutoChatHandler _instance = new AutoChatHandler();
	}
}
