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
package com.l2jserver.gameserver.model.actor.instance;

import com.l2jserver.gameserver.datatables.ItemTable;
import com.l2jserver.gameserver.instancemanager.HandysBlockCheckerManager.ArenaParticipantsHolder;
import com.l2jserver.gameserver.model.actor.L2Character;
import com.l2jserver.gameserver.model.actor.templates.L2NpcTemplate;
import com.l2jserver.gameserver.model.entity.BlockCheckerEngine;
import com.l2jserver.gameserver.model.items.instance.L2ItemInstance;
import com.l2jserver.gameserver.network.serverpackets.AbstractNpcInfo;
import com.l2jserver.gameserver.network.serverpackets.ActionFailed;
import com.l2jserver.gameserver.network.serverpackets.ExCubeGameChangePoints;
import com.l2jserver.gameserver.network.serverpackets.ExCubeGameExtendedChangePoints;
import com.l2jserver.gameserver.network.serverpackets.MyTargetSelected;
import com.l2jserver.gameserver.network.serverpackets.StatusUpdate;
import com.l2jserver.gameserver.network.serverpackets.ValidateLocation;
import com.l2jserver.util.Rnd;

/**
 * @author BiggBoss
 */
public class L2BlockInstance extends L2MonsterInstance
{
	private int _colorEffect;
	
	/**
	 * @param objectId
	 * @param template
	 */
	public L2BlockInstance(int objectId, L2NpcTemplate template)
	{
		super(objectId, template);
	}
	
	/**
	 * Will change the color of the block and update
	 * the appearance in the known players clients
	 * @param attacker 
	 * @param holder 
	 * @param team 
	 */
	public void changeColor(L2PcInstance attacker, ArenaParticipantsHolder holder, int team)
	{
		// Do not update color while sending old info
		synchronized(this)
		{
			final BlockCheckerEngine event = holder.getEvent();
			if(_colorEffect == 0x53)
			{
				// Change color
				_colorEffect = 0x00;
				// BroadCast to all known players
				this.broadcastPacket(new AbstractNpcInfo.NpcInfo(this, attacker));
				increaseTeamPointsAndSend(attacker, team, event);
			}
			else
			{
				// Change color
				_colorEffect = 0x53;
				// BroadCast to all known players
				this.broadcastPacket(new AbstractNpcInfo.NpcInfo(this, attacker));
				increaseTeamPointsAndSend(attacker, team, event);
			}
			// 30% chance to drop the event items
			int random = Rnd.get(100);
			// Bond
			if(random > 69 && random <= 84)
				dropItem(13787, event, attacker);
			// Land Mine
			else if(random > 84)
				dropItem(13788, event, attacker);
		}
	}
	
	/**
	 * Sets if the block is red or blue. Mainly used in
	 * block spawn
	 * @param isRed
	 */
	public void setRed(boolean isRed)
	{
		_colorEffect = isRed? 0x53 : 0x00;
	}
	
	/**
	 * Return if the block is red at this momment
	 * @return
	 */
	@Override
	public int getColorEffect()
	{
		return _colorEffect;
	}
	
	@Override
	public boolean isAutoAttackable(L2Character attacker)
	{
		if(attacker instanceof L2PcInstance)
			return attacker.getActingPlayer() != null && attacker.getActingPlayer().getBlockCheckerArena() > -1;
		return true;
	}
	
	@Override
	public boolean isAttackable()
	{
		return true;
	}
	
	@Override
	public boolean doDie(L2Character killer)
	{
		return false;
	}
	
	@Override
	public void onAction(L2PcInstance player, boolean interact)
	{
		if (!this.canTarget(player))
			return;
		
		player.setLastFolkNPC(this);
		
		if(player.getTarget() != this)
		{
			player.setTarget(this);
			this.getAI(); //wake up ai
			// Send a Server->Client packet MyTargetSelected to the L2PcInstance activeChar
			// The activeChar.getLevel() - getLevel() permit to display the correct color in the select window
			MyTargetSelected my = new MyTargetSelected(getObjectId(), player.getLevel() - getLevel());
			player.sendPacket(my);
			
			// Send a Server->Client packet StatusUpdate of the L2Npc to the L2PcInstance to update its HP bar
			StatusUpdate su = new StatusUpdate(this);
			su.addAttribute(StatusUpdate.CUR_HP, (int) getCurrentHp());
			su.addAttribute(StatusUpdate.MAX_HP, getMaxHp());
			player.sendPacket(su);
			player.sendPacket(new ValidateLocation(this));
		}
		else if(interact)
		{
			player.sendPacket(new ValidateLocation(this));
			player.sendPacket(ActionFailed.STATIC_PACKET);
		}
	}
	
	private void increaseTeamPointsAndSend(L2PcInstance player, int team, BlockCheckerEngine eng)
	{
		eng.increasePlayerPoints(player, team);
		
		int timeLeft = (int)((eng.getStarterTime() - System.currentTimeMillis()) / 1000);
		boolean isRed = eng.getHolder().getRedPlayers().contains(player);
		
		ExCubeGameChangePoints changePoints = new ExCubeGameChangePoints(timeLeft, eng.getBluePoints(), eng.getRedPoints());
		ExCubeGameExtendedChangePoints secretPoints = new ExCubeGameExtendedChangePoints(timeLeft, eng.getBluePoints(), eng.getRedPoints(),
				isRed, player, eng.getPlayerPoints(player, isRed));
		
		eng.getHolder().broadCastPacketToTeam(changePoints);
		eng.getHolder().broadCastPacketToTeam(secretPoints);
	}
		
	private void dropItem(int id, BlockCheckerEngine eng, L2PcInstance player)
	{
		L2ItemInstance drop = ItemTable.getInstance().createItem("Loot", id, 1, player, this);
		int x = getX() + Rnd.get(50);
		int y = getY() + Rnd.get(50);
		int z = getZ();
		
		drop.dropMe(this, x, y, z);
		
		eng.addNewDrop(drop);
	}
}
