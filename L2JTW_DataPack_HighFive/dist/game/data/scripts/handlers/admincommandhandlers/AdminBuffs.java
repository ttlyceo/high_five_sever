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
package handlers.admincommandhandlers;

import java.util.Collection;
import java.util.StringTokenizer;

import com.l2jserver.Config;
import com.l2jserver.gameserver.datatables.SkillTreesData;
import com.l2jserver.gameserver.handler.IAdminCommandHandler;
import com.l2jserver.gameserver.model.L2World;
import com.l2jserver.gameserver.model.actor.L2Character;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.effects.L2Effect;
import com.l2jserver.gameserver.model.skills.L2Skill;
import com.l2jserver.gameserver.network.SystemMessageId;
import com.l2jserver.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jserver.gameserver.network.serverpackets.SkillCoolTime;
import com.l2jserver.gameserver.util.GMAudit;
import com.l2jserver.util.StringUtil;
import com.l2jserver.gameserver.datatables.MessageTable;

public class AdminBuffs implements IAdminCommandHandler
{
	private final static int PAGE_LIMIT = 20;
	
	private static final String[] ADMIN_COMMANDS =
	{
		"admin_getbuffs",
		"admin_stopbuff",
		"admin_stopallbuffs",
		"admin_areacancel",
		"admin_removereuse",
		"admin_switch_gm_buffs"
	};
	
	@Override
	public boolean useAdminCommand(String command, L2PcInstance activeChar)
	{
		
		if (command.startsWith("admin_getbuffs"))
		{
			StringTokenizer st = new StringTokenizer(command, " ");
			command = st.nextToken();
			
			if (st.hasMoreTokens())
			{
				L2PcInstance player = null;
				String playername = st.nextToken();
				
				try
				{
					player = L2World.getInstance().getPlayer(playername);
				}
				catch (Exception e)
				{
				}
				
				if (player != null)
				{
					int page = 1;
					if (st.hasMoreTokens())
						page = Integer.parseInt(st.nextToken());
					showBuffs(activeChar, player, page);
					return true;
				}
				activeChar.sendMessage(MessageTable.Messages[1451].getExtra(1) + playername + MessageTable.Messages[1451].getExtra(2));
				return false;
			}
			else if ((activeChar.getTarget() != null) && (activeChar.getTarget() instanceof L2Character))
			{
				showBuffs(activeChar, (L2Character) activeChar.getTarget(), 1);
				return true;
			}
			else
			{
				activeChar.sendPacket(SystemMessageId.TARGET_IS_INCORRECT);
				return false;
			}
		}
		else if (command.startsWith("admin_stopbuff"))
		{
			try
			{
				StringTokenizer st = new StringTokenizer(command, " ");
				
				st.nextToken();
				int objectId = Integer.parseInt(st.nextToken());
				int skillId = Integer.parseInt(st.nextToken());
				
				removeBuff(activeChar, objectId, skillId);
				return true;
			}
			catch (Exception e)
			{
				activeChar.sendMessage("Failed removing effect: " + e.getMessage());
				activeChar.sendMessage("Usage: //stopbuff <objectId> <skillId>");
				return false;
			}
		}
		else if (command.startsWith("admin_stopallbuffs"))
		{
			try
			{
				StringTokenizer st = new StringTokenizer(command, " ");
				st.nextToken();
				int objectId = Integer.parseInt(st.nextToken());
				removeAllBuffs(activeChar, objectId);
				return true;
			}
			catch (Exception e)
			{
				activeChar.sendMessage("Failed removing all effects: " + e.getMessage());
				activeChar.sendMessage("Usage: //stopallbuffs <objectId>");
				return false;
			}
		}
		else if (command.startsWith("admin_areacancel"))
		{
			StringTokenizer st = new StringTokenizer(command, " ");
			st.nextToken();
			String val = st.nextToken();
			try
			{
				int radius = Integer.parseInt(val);
				
				for (L2Character knownChar : activeChar.getKnownList().getKnownCharactersInRadius(radius))
				{
					if ((knownChar instanceof L2PcInstance) && !(knownChar.equals(activeChar)))
						knownChar.stopAllEffects();
				}
				
				activeChar.sendMessage(MessageTable.Messages[1452].getExtra(1) + radius + MessageTable.Messages[1452].getExtra(2));
				return true;
			}
			catch (NumberFormatException e)
			{
				activeChar.sendMessage("Usage: //areacancel <radius>");
				return false;
			}
		}
		else if (command.startsWith("admin_removereuse"))
		{
			StringTokenizer st = new StringTokenizer(command, " ");
			command = st.nextToken();
			
			L2PcInstance player = null;
			if (st.hasMoreTokens())
			{
				String playername = st.nextToken();
				
				try
				{
					player = L2World.getInstance().getPlayer(playername);
				}
				catch (Exception e)
				{
				}
				
				if (player == null)
				{
					activeChar.sendMessage("The player " + playername + " is not online.");
					return false;
				}
			}
			else if (activeChar.getTarget() instanceof L2PcInstance)
			{
				player = (L2PcInstance) activeChar.getTarget();
			}
			else
			{
				activeChar.sendPacket(SystemMessageId.TARGET_IS_INCORRECT);
				return false;
			}
			
			try
			{
				player.getSkillReuseTimeStamps().clear();
				player.getDisabledSkills().clear();
				player.sendPacket(new SkillCoolTime(player));
				activeChar.sendMessage("Skill reuse was removed from " + player.getName() + ".");
				return true;
			}
			catch (NullPointerException e)
			{
				return false;
			}
		}
		else if (command.startsWith("admin_switch_gm_buffs"))
		{
			if (Config.GM_GIVE_SPECIAL_SKILLS != Config.GM_GIVE_SPECIAL_AURA_SKILLS)
			{
				final boolean toAuraSkills = activeChar.getKnownSkill(7041) != null;
				switchSkills(activeChar, toAuraSkills);
				activeChar.sendSkillList();
				activeChar.sendMessage("You have succefully changed to target " + (toAuraSkills ? "aura" : "one") + " special skills.");
				return true;
			}
			activeChar.sendMessage("There is nothing to switch.");
			return false;
		}
		else
		{
			return true;
		}
	}
	
	/**
	 * @param gmchar the player to switch the Game Master skills.
	 * @param toAuraSkills if {@code true} it will remove "GM Aura" skills and add "GM regular" skills, vice versa if {@code false}.
	 */
	public void switchSkills(L2PcInstance gmchar, boolean toAuraSkills)
	{
		final Collection<L2Skill> skills = toAuraSkills ? SkillTreesData.getInstance().getGMSkillTree().values() : SkillTreesData.getInstance().getGMAuraSkillTree().values();
		for (L2Skill skill : skills)
		{
			gmchar.removeSkill(skill, false); // Don't Save GM skills to database
		}
		SkillTreesData.getInstance().addSkills(gmchar, toAuraSkills);
	}
	
	@Override
	public String[] getAdminCommandList()
	{
		return ADMIN_COMMANDS;
	}
	
	public void showBuffs(L2PcInstance activeChar, L2Character target, int page)
	{
		final L2Effect[] effects = target.getAllEffects();
		
		if (page > effects.length / PAGE_LIMIT + 1 || page < 1)
			return;
		
		int max = effects.length / PAGE_LIMIT;
		if (effects.length > PAGE_LIMIT * max)
			max++;
		
		final StringBuilder html = StringUtil.startAppend(500 + effects.length * 200,
				"<html><table width=\"100%\"><tr><td width=45><button value=\""+MessageTable.Messages[1453].getMessage()+"\" action=\"bypass -h admin_admin\" width=45 height=21 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"></td><td width=180><center><font color=\"LEVEL\">"+MessageTable.Messages[1454].getMessage(), 
				target.getName(),
		"</font></td><td width=45><button value=\""+MessageTable.Messages[1455].getMessage()+"\" action=\"bypass -h admin_current_player\" width=45 height=21 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"></td></tr></table><br><table width=\"100%\"><tr><td width=150>"+MessageTable.Messages[1456].getExtra(1)+"</td><td width=50>"+MessageTable.Messages[1456].getExtra(2)+"</td><td width=70>"+MessageTable.Messages[1456].getExtra(3)+"</td></tr>");
		
		int start = ((page - 1) * PAGE_LIMIT);
		int end = Math.min(((page - 1) * PAGE_LIMIT) + PAGE_LIMIT, effects.length);
		
		for (int i = start; i < end; i++)
		{
			L2Effect e = effects[i];
			if (e != null)
			{
				StringUtil.append(html,
						"<tr><td>",
						e.getSkill().getName(),
						"</td><td>",
						e.getSkill().isToggle() ? "toggle" : e.getAbnormalTime() - e.getTime() + "s",
								"</td><td><button value=\""+MessageTable.Messages[1457].getMessage()+"\" action=\"bypass -h admin_stopbuff ",
								Integer.toString(target.getObjectId()),
								" ",
								String.valueOf(e.getSkill().getId()),
				"\" width=60 height=21 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"></td></tr>");
			}
		}
		
		html.append("</table><table width=300 bgcolor=444444><tr>");
		for (int x = 0; x < max; x++)
		{
			int pagenr = x + 1;
			if (page == pagenr)
			{
				html.append("<td>"+MessageTable.Messages[1458].getMessage());
				html.append(pagenr);
				html.append(MessageTable.Messages[1458].getExtra(1)+"</td>");
			}
			else
			{
				html.append("<td><a action=\"bypass -h admin_getbuffs ");
				html.append(target.getName());
				html.append(" ");
				html.append(x + 1);
				html.append("\"> "+MessageTable.Messages[1458].getMessage());
				html.append(pagenr);
				html.append(MessageTable.Messages[1458].getExtra(1)+"</a></td>");
			}
		}
		
		html.append("</tr></table>");
		
		StringUtil.append(html, "<br><center><button value=\""+MessageTable.Messages[1459].getMessage()+"\" action=\"bypass -h admin_stopallbuffs ", 
				Integer.toString(target.getObjectId()),
		"\" width=80 height=21 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\"></html>");
		
		NpcHtmlMessage ms = new NpcHtmlMessage(1);
		ms.setHtml(html.toString());
		activeChar.sendPacket(ms);
		
		if (Config.GMAUDIT)
			GMAudit.auditGMAction(activeChar.getName()+" ["+activeChar.getObjectId()+"]", "getbuffs", target.getName() + " (" + Integer.toString(target.getObjectId()) + ")", "");
	}
	
	private void removeBuff(L2PcInstance activeChar, int objId, int skillId)
	{
		L2Character target = null;
		try
		{
			target = (L2Character) L2World.getInstance().findObject(objId);
		}
		catch (Exception e)
		{
		}
		
		if ((target != null) && (skillId > 0))
		{
			L2Effect[] effects = target.getAllEffects();
			
			for (L2Effect e : effects)
			{
				if ((e != null) && (e.getSkill().getId() == skillId))
				{
					e.exit();
					activeChar.sendMessage(MessageTable.Messages[1460].getExtra(1) + e.getSkill().getName() + MessageTable.Messages[1460].getExtra(2) + e.getSkill().getLevel() + MessageTable.Messages[1460].getExtra(3) + target.getName() + " (" + objId + ")");
				}
			}
			showBuffs(activeChar, target, 1);
			if (Config.GMAUDIT)
				GMAudit.auditGMAction(activeChar.getName()+" ["+activeChar.getObjectId()+"]", "stopbuff", target.getName() + " (" + objId + ")", Integer.toString(skillId));
		}
	}
	
	private void removeAllBuffs(L2PcInstance activeChar, int objId)
	{
		L2Character target = null;
		try
		{
			target = (L2Character) L2World.getInstance().findObject(objId);
		}
		catch (Exception e)
		{
		}
		
		if (target != null)
		{
			target.stopAllEffects();
			activeChar.sendMessage(MessageTable.Messages[1461].getMessage() + target.getName() + " (" + objId + ")");
			showBuffs(activeChar, target, 1);
			if (Config.GMAUDIT)
				GMAudit.auditGMAction(activeChar.getName()+" ["+activeChar.getObjectId()+"]", "stopallbuffs", target.getName() + " (" + objId + ")", "");
		}
	}
}