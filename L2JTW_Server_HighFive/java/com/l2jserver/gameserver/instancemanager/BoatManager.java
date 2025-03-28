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
package com.l2jserver.gameserver.instancemanager;

import gnu.trove.procedure.TObjectProcedure;

import java.util.Map;

import javolution.util.FastMap;

import com.l2jserver.Config;
import com.l2jserver.gameserver.idfactory.IdFactory;
import com.l2jserver.gameserver.model.L2World;
import com.l2jserver.gameserver.model.StatsSet;
import com.l2jserver.gameserver.model.VehiclePathPoint;
import com.l2jserver.gameserver.model.actor.instance.L2BoatInstance;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.actor.templates.L2CharTemplate;
import com.l2jserver.gameserver.network.serverpackets.L2GameServerPacket;

public class BoatManager
{
	private Map<Integer, L2BoatInstance> _boats = new FastMap<>();
	private boolean[] _docksBusy = new boolean[3];
	
	public static final int TALKING_ISLAND = 1;
	public static final int GLUDIN_HARBOR = 2;
	public static final int RUNE_HARBOR = 3;
	
	public static final BoatManager getInstance()
	{
		return SingletonHolder._instance;
	}
	
	protected BoatManager()
	{
		for (int i = 0; i < _docksBusy.length; i++)
			_docksBusy[i] = false;
	}
	
	public L2BoatInstance getNewBoat(int boatId, int x, int y, int z, int heading)
	{
		if (!Config.ALLOW_BOAT)
			return null;
		
		StatsSet npcDat = new StatsSet();
		npcDat.set("npcId", boatId);
		npcDat.set("level", 0);
		npcDat.set("jClass", "boat");
		
		npcDat.set("baseSTR", 0);
		npcDat.set("baseCON", 0);
		npcDat.set("baseDEX", 0);
		npcDat.set("baseINT", 0);
		npcDat.set("baseWIT", 0);
		npcDat.set("baseMEN", 0);
		
		npcDat.set("baseShldDef", 0);
		npcDat.set("baseShldRate", 0);
		npcDat.set("baseAccCombat", 38);
		npcDat.set("baseEvasRate", 38);
		npcDat.set("baseCritRate", 38);
		
		// npcDat.set("name", "");
		npcDat.set("collision_radius", 0);
		npcDat.set("collision_height", 0);
		npcDat.set("sex", "male");
		npcDat.set("type", "");
		npcDat.set("baseAtkRange", 0);
		npcDat.set("baseMpMax", 0);
		npcDat.set("baseCpMax", 0);
		npcDat.set("rewardExp", 0);
		npcDat.set("rewardSp", 0);
		npcDat.set("basePAtk", 0);
		npcDat.set("baseMAtk", 0);
		npcDat.set("basePAtkSpd", 0);
		npcDat.set("aggroRange", 0);
		npcDat.set("baseMAtkSpd", 0);
		npcDat.set("rhand", 0);
		npcDat.set("lhand", 0);
		npcDat.set("armor", 0);
		npcDat.set("baseWalkSpd", 0);
		npcDat.set("baseRunSpd", 0);
		npcDat.set("baseHpMax", 50000);
		npcDat.set("baseHpReg", 3.e-3f);
		npcDat.set("baseMpReg", 3.e-3f);
		npcDat.set("basePDef", 100);
		npcDat.set("baseMDef", 100);
		L2CharTemplate template = new L2CharTemplate(npcDat);
		L2BoatInstance boat = new L2BoatInstance(IdFactory.getInstance().getNextId(), template);
		_boats.put(boat.getObjectId(), boat);
		boat.setHeading(heading);
		boat.setXYZInvisible(x, y, z);
		boat.spawnMe();
		return boat;
	}
	
	/**
	 * @param boatId
	 * @return
	 */
	public L2BoatInstance getBoat(int boatId)
	{
		return _boats.get(boatId);
	}
	
	/**
	 * Lock/unlock dock so only one ship can be docked
	 * @param h Dock Id
	 * @param value True if dock is locked
	 */
	public void dockShip(int h, boolean value)
	{
		try
		{
			_docksBusy[h] = value;
		}
		catch (ArrayIndexOutOfBoundsException e)
		{}
	}
	
	/**
	 * Check if dock is busy
	 * @param h Dock Id
	 * @return Trye if dock is locked
	 */
	public boolean dockBusy(int h)
	{
		try
		{
			return _docksBusy[h];
		}
		catch (ArrayIndexOutOfBoundsException e)
		{
			return false;
		}
	}
	
	/**
	 * Broadcast one packet in both path points
	 * @param point1 
	 * @param point2 
	 * @param packet 
	 */
	public void broadcastPacket(VehiclePathPoint point1, VehiclePathPoint point2, L2GameServerPacket packet)
	{
		
		L2World.getInstance().forEachPlayer(new ForEachPlayerBroadcastPackets(point1, point2, packet));
	}
	
	/**
	 * Broadcast several packets in both path points
	 * @param point1 
	 * @param point2 
	 * @param packets 
	 */
	public void broadcastPackets(VehiclePathPoint point1, VehiclePathPoint point2, L2GameServerPacket... packets)
	{
		L2World.getInstance().forEachPlayer(new ForEachPlayerBroadcastPackets(point1, point2, packets));
	}
	
	private final class ForEachPlayerBroadcastPackets implements TObjectProcedure<L2PcInstance>
	{
		VehiclePathPoint _point1, _point2;
		L2GameServerPacket[] _packets;
		
		protected ForEachPlayerBroadcastPackets(VehiclePathPoint point1, VehiclePathPoint point2, L2GameServerPacket ... packets)
		{
			_point1 = point1;
			_point2 = point2;
			_packets = packets;
		}
		
		@Override
		public final boolean execute(final L2PcInstance player)
		{
			if (player != null)
			{
				double dx = (double) player.getX() - _point1.x;
				double dy = (double) player.getY() - _point1.y;
				if (Math.sqrt(dx * dx + dy * dy) < Config.BOAT_BROADCAST_RADIUS)
				{
					for (L2GameServerPacket p : _packets)
						player.sendPacket(p);
				}
				else
				{
					dx = (double) player.getX() - _point2.x;
					dy = (double) player.getY() - _point2.y;
					if (Math.sqrt(dx * dx + dy * dy) < Config.BOAT_BROADCAST_RADIUS)
					{
						for (L2GameServerPacket p : _packets)
							player.sendPacket(p);
					}
				}
			}
			
			return true;
		}
	}
	
	private static class SingletonHolder
	{
		protected static final BoatManager _instance = new BoatManager();
	}
}