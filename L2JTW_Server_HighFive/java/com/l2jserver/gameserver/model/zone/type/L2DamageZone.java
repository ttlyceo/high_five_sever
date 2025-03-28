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
package com.l2jserver.gameserver.model.zone.type;

import java.util.concurrent.Future;

import com.l2jserver.gameserver.ThreadPoolManager;
import com.l2jserver.gameserver.instancemanager.CastleManager;
import com.l2jserver.gameserver.model.L2Object.InstanceType;
import com.l2jserver.gameserver.model.actor.L2Character;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.entity.Castle;
import com.l2jserver.gameserver.model.stats.Stats;
import com.l2jserver.gameserver.model.zone.L2ZoneType;

/**
 * A damage zone
 * @author durgus
 */
public class L2DamageZone extends L2ZoneType
{
	private int _damageHPPerSec;
	private int _damageMPPerSec;
	private Future<?> _task;
	
	private int _castleId;
	private Castle _castle;
	
	private int _startTask;
	private int _reuseTask;
	
	protected boolean _enabled;
	
	public L2DamageZone(int id)
	{
		super(id);
		
		// Setup default damage
		_damageHPPerSec = 200;
		_damageMPPerSec = 0;
		
		// Setup default start / reuse time
		_startTask = 10;
		_reuseTask = 5000;
		
		// no castle by default
		_castleId = 0;
		_castle = null;
		
		// enabled by default
		_enabled = true;
		
		setTargetType(InstanceType.L2Playable); // default only playabale
	}
	
	@Override
	public void setParameter(String name, String value)
	{
		if (name.equals("dmgHPSec"))
		{
			_damageHPPerSec = Integer.parseInt(value);
		}
		else if (name.equals("dmgMPSec"))
		{
			_damageMPPerSec = Integer.parseInt(value);
		}
		else if (name.equals("castleId"))
		{
			_castleId = Integer.parseInt(value);
		}
		else if (name.equalsIgnoreCase("initialDelay"))
		{
			_startTask = Integer.parseInt(value);
		}
		else if (name.equalsIgnoreCase("reuse"))
		{
			_reuseTask = Integer.parseInt(value);
		}
		else if (name.equalsIgnoreCase("default_enabled"))
		{
			_enabled = Boolean.parseBoolean(value);
		}
		else
		{
			super.setParameter(name, value);
		}
	}
	
	@Override
	protected void onEnter(L2Character character)
	{
		if (_task == null && (_damageHPPerSec != 0 || _damageMPPerSec != 0))
		{
			L2PcInstance player = character.getActingPlayer();
			if (getCastle() != null) // Castle zone
			{
				if (!(getCastle().getSiege().getIsInProgress() && player != null && player.getSiegeState() != 2)) // Siege and no defender
				{
					return;
				}
			}
			
			synchronized (this)
			{
				if (_task == null)
					_task = ThreadPoolManager.getInstance().scheduleGeneralAtFixedRate(new ApplyDamage(this), _startTask, _reuseTask);
			}
		}
	}
	
	@Override
	protected void onExit(L2Character character)
	{
		if (_characterList.isEmpty() && _task != null)
		{
			stopTask();
		}
	}
	
	protected int getHPDamagePerSecond()
	{
		return _damageHPPerSec;
	}
	
	protected int getMPDamagePerSecond()
	{
		return _damageMPPerSec;
	}
	
	protected void stopTask()
	{
		if (_task != null)
		{
			_task.cancel(false);
			_task = null;
		}
	}
	
	protected Castle getCastle()
	{
		if (_castleId > 0 && _castle == null)
			_castle = CastleManager.getInstance().getCastleById(_castleId);
		
		return _castle;
	}
	
	private final class ApplyDamage implements Runnable
	{
		private final L2DamageZone _dmgZone;
		private final Castle _castle;
		
		protected ApplyDamage(L2DamageZone zone)
		{
			_dmgZone = zone;
			_castle = zone.getCastle();
		}
		
		@Override
		public void run()
		{	
			if (!_enabled)
			{
				return;
			}
			
			boolean siege = false;
			
			if (_castle != null)
			{
				siege = _castle.getSiege().getIsInProgress();
				// castle zones active only during siege
				if (!siege)
				{
					_dmgZone.stopTask();
					return;
				}
			}
			
			for (L2Character temp : _dmgZone.getCharactersInside())
			{
				if (temp != null && !temp.isDead())
				{
					if (siege)
					{
						// during siege defenders not affected
						final L2PcInstance player = temp.getActingPlayer();
						if (player != null && player.isInSiege() && player.getSiegeState() == 2)
							continue;
					}
					
					double multiplier = 1 + (temp.calcStat(Stats.DAMAGE_ZONE_VULN, 0, null, null) / 100);
					
					if (getHPDamagePerSecond() != 0)
						temp.reduceCurrentHp(_dmgZone.getHPDamagePerSecond() * multiplier, null, null);
					if (getMPDamagePerSecond() != 0)
						temp.reduceCurrentMp(_dmgZone.getMPDamagePerSecond() * multiplier);
				}
			}
		}
	}
	
	public void setEnabled(boolean state)
	{
		_enabled = state;
	}
	
	@Override
	public void onDieInside(L2Character character)
	{
	}
	
	@Override
	public void onReviveInside(L2Character character)
	{
	}
}
