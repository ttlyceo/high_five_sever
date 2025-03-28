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
package com.l2jserver.gameserver.model.skills.funcs;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.logging.Level;
import java.util.logging.Logger;

import com.l2jserver.gameserver.model.conditions.Condition;
import com.l2jserver.gameserver.model.stats.Env;
import com.l2jserver.gameserver.model.stats.Stats;

/**
 * @author mkizub
 */
public final class FuncTemplate
{
	protected static final Logger _log = Logger.getLogger(FuncTemplate.class.getName());
	
	public Condition attachCond;
	public Condition applayCond;
	public final Class<?> func;
	public final Constructor<?> constructor;
	public final Stats stat;
	public final int order;
	public final Lambda lambda;
	
	public FuncTemplate(Condition pAttachCond, Condition pApplayCond, String pFunc, Stats pStat, int pOrder, Lambda pLambda)
	{
		attachCond = pAttachCond;
		applayCond = pApplayCond;
		stat = pStat;
		order = pOrder;
		lambda = pLambda;
		try
		{
			func = Class.forName("com.l2jserver.gameserver.model.skills.funcs.Func" + pFunc);
		}
		catch (ClassNotFoundException e)
		{
			throw new RuntimeException(e);
		}
		try
		{
			constructor = func.getConstructor(new Class<?>[]
			{
				// Stats to update
				Stats.class,
				// Order of execution
				Integer.TYPE,
				// Owner
				Object.class,
				// Value for function
				Lambda.class
			});
		}
		catch (NoSuchMethodException e)
		{
			throw new RuntimeException(e);
		}
	}
	
	public Func getFunc(Env env, Object owner)
	{
		if ((attachCond != null) && !attachCond.test(env))
		{
			return null;
		}
		try
		{
			Func f = (Func) constructor.newInstance(stat, order, owner, lambda);
			if (applayCond != null)
			{
				f.setCondition(applayCond);
			}
			return f;
		}
		catch (IllegalAccessException e)
		{
			_log.log(Level.WARNING, "", e);
			return null;
		}
		catch (InstantiationException e)
		{
			_log.log(Level.WARNING, "", e);
			return null;
		}
		catch (InvocationTargetException e)
		{
			_log.log(Level.WARNING, "", e);
			return null;
		}
	}
}
