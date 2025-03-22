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
package com.l2jserver.gameserver.network.clientpackets;

import java.util.StringTokenizer;
import java.util.logging.Level;

import com.l2jserver.Config;
import com.l2jserver.gameserver.ai.CtrlIntention;
import com.l2jserver.gameserver.communitybbs.CommunityBoard;
import com.l2jserver.gameserver.datatables.AdminTable;
import com.l2jserver.gameserver.handler.AdminCommandHandler;
import com.l2jserver.gameserver.handler.BypassHandler;
import com.l2jserver.gameserver.handler.IAdminCommandHandler;
import com.l2jserver.gameserver.handler.IBypassHandler;
import com.l2jserver.gameserver.model.L2CharPosition;
import com.l2jserver.gameserver.model.L2Object;
import com.l2jserver.gameserver.model.L2World;
import com.l2jserver.gameserver.model.actor.L2Npc;
import com.l2jserver.gameserver.model.actor.instance.L2MerchantSummonInstance;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.entity.Hero;
import com.l2jserver.gameserver.network.SystemMessageId;
import com.l2jserver.gameserver.network.communityserver.CommunityServerThread;
import com.l2jserver.gameserver.network.communityserver.writepackets.RequestShowCommunityBoard;
import com.l2jserver.gameserver.network.serverpackets.ActionFailed;
import com.l2jserver.gameserver.network.serverpackets.ConfirmDlg;
import com.l2jserver.gameserver.network.serverpackets.NpcHtmlMessage;
import com.l2jserver.gameserver.util.GMAudit;
import com.l2jserver.gameserver.util.Util;
import com.l2jserver.gameserver.datatables.MessageTable;

/**
 * This class ...
 * @version $Revision: 1.12.4.5 $ $Date: 2005/04/11 10:06:11 $
 */
public final class RequestBypassToServer extends L2GameClientPacket
{
	private static final String _C__23_REQUESTBYPASSTOSERVER = "[C] 23 RequestBypassToServer";
	
	// S
	private String _command;
	
	@Override
	protected void readImpl()
	{
		_command = readS();
	}
	
	@Override
	protected void runImpl()
	{
		final L2PcInstance activeChar = getClient().getActiveChar();
		if (activeChar == null)
			return;
		
		if (!getClient().getFloodProtectors().getServerBypass().tryPerformAction(_command))
			return;
		
		if (_command.isEmpty())
		{
			_log.info(activeChar.getName() + " send empty requestbypass");
			activeChar.logout();
			return;
		}
		
		try
		{
			if (_command.startsWith("admin_"))
			{
				String command = _command.split(" ")[0];
				
				IAdminCommandHandler ach = AdminCommandHandler.getInstance().getHandler(command);
				
				if (ach == null)
				{
					if (activeChar.isGM())
					{
						/* Move To MessageTable For L2JTW
						activeChar.sendMessage("The command " + command.substring(6) + " does not exist!");
						*/
						activeChar.sendMessage(MessageTable.Messages[255].getExtra(1) + command.substring(6) + MessageTable.Messages[255].getExtra(2));
					}
					_log.warning(activeChar + " requested not registered admin command '" + command + "'");
					return;
				}
				
				if (!AdminTable.getInstance().hasAccess(command, activeChar.getAccessLevel()))
				{
					/*
					activeChar.sendMessage("You don't have the access rights to use this command!");
					*/
					activeChar.sendPacket(SystemMessageId.YOU_ARE_NOT_AUTHORIZED_TO_DO_THAT);
					_log.warning("Character " + activeChar.getName() + " tried to use admin command " + command + ", without proper access level!");
					return;
				}
				
				if (AdminTable.getInstance().requireConfirm(command))
				{
					activeChar.setAdminConfirmCmd(_command);
					ConfirmDlg dlg = new ConfirmDlg(SystemMessageId.S1);
					dlg.addString("Are you sure you want execute command " + _command.substring(6) + " ?");
					activeChar.sendPacket(dlg);
				}
				else
				{
					if (Config.GMAUDIT)
					{
						GMAudit.auditGMAction(activeChar.getName() + " [" + activeChar.getObjectId() + "]", _command, (activeChar.getTarget() != null ? activeChar.getTarget().getName() : "no-target"));
					}
					
					ach.useAdminCommand(_command, activeChar);
				}
			}
			else if (_command.equals("come_here") && activeChar.isGM())
			{
				comeHere(activeChar);
			}
			else if (_command.startsWith("npc_"))
			{
				if (!activeChar.validateBypass(_command))
					return;
				
				int endOfId = _command.indexOf('_', 5);
				String id;
				if (endOfId > 0)
				{
					id = _command.substring(4, endOfId);
				}
				else
				{
					id = _command.substring(4);
				}
				if (Util.isDigit(id))
				{
					L2Object object = L2World.getInstance().findObject(Integer.parseInt(id));
					
					if (object != null && object.isNpc() && endOfId > 0 && activeChar.isInsideRadius(object, L2Npc.INTERACTION_DISTANCE, false, false))
					{
						((L2Npc) object).onBypassFeedback(activeChar, _command.substring(endOfId + 1));
					}
				}
				
				activeChar.sendPacket(ActionFailed.STATIC_PACKET);
			}
			else if (_command.startsWith("summon_"))
			{
				if (!activeChar.validateBypass(_command))
					return;
				
				int endOfId = _command.indexOf('_', 8);
				String id;
				
				if (endOfId > 0)
				{
					id = _command.substring(7, endOfId);
				}
				else
				{
					id = _command.substring(7);
				}
				
				if (Util.isDigit(id))
				{
					L2Object object = L2World.getInstance().findObject(Integer.parseInt(id));
					
					if (object instanceof L2MerchantSummonInstance && endOfId > 0 && activeChar.isInsideRadius(object, L2Npc.INTERACTION_DISTANCE, false, false))
					{
						((L2MerchantSummonInstance) object).onBypassFeedback(activeChar, _command.substring(endOfId + 1));
					}
				}
				activeChar.sendPacket(ActionFailed.STATIC_PACKET);
			}
			// Navigate through Manor windows
			else if (_command.startsWith("manor_menu_select"))
			{
				final IBypassHandler manor = BypassHandler.getInstance().getHandler("manor_menu_select");
				if (manor != null)
				{
					manor.useBypass(_command, activeChar, null);
				}
			}
			else if (_command.startsWith("_bbs"))
			{
				if (Config.ENABLE_COMMUNITY_BOARD)
				{
					if (!CommunityServerThread.getInstance().sendPacket(new RequestShowCommunityBoard(activeChar.getObjectId(), _command)))
						activeChar.sendPacket(SystemMessageId.CB_OFFLINE);
				}
				else
				{
					CommunityBoard.getInstance().handleCommands(getClient(), _command);
				}
			}
			else if (_command.startsWith("bbs"))
			{
				if (Config.ENABLE_COMMUNITY_BOARD)
				{
					if (!CommunityServerThread.getInstance().sendPacket(new RequestShowCommunityBoard(activeChar.getObjectId(), _command)))
					{
						activeChar.sendPacket(SystemMessageId.CB_OFFLINE);
					}
				}
				else
				{
					CommunityBoard.getInstance().handleCommands(getClient(), _command);
				}
			}
			else if (_command.startsWith("_mail"))
			{
				if (!CommunityServerThread.getInstance().sendPacket(new RequestShowCommunityBoard(activeChar.getObjectId(), "_bbsmail")))
				{
					activeChar.sendPacket(SystemMessageId.CB_OFFLINE);
				}
			}
			else if (_command.startsWith("_friend"))
			{
				if (!CommunityServerThread.getInstance().sendPacket(new RequestShowCommunityBoard(activeChar.getObjectId(), "_bbsfriend")))
				{
					activeChar.sendPacket(SystemMessageId.CB_OFFLINE);
				}
			}
			else if (_command.startsWith("Quest "))
			{
				if (!activeChar.validateBypass(_command))
					return;
				
				String p = _command.substring(6).trim();
				int idx = p.indexOf(' ');
				if (idx < 0)
				{
					activeChar.processQuestEvent(p, "");
				}
				else
				{
					activeChar.processQuestEvent(p.substring(0, idx), p.substring(idx).trim());
				}
			}
			else if (_command.startsWith("_match"))
			{
				String params = _command.substring(_command.indexOf("?") + 1);
				StringTokenizer st = new StringTokenizer(params, "&");
				int heroclass = Integer.parseInt(st.nextToken().split("=")[1]);
				int heropage = Integer.parseInt(st.nextToken().split("=")[1]);
				int heroid = Hero.getInstance().getHeroByClass(heroclass);
				if (heroid > 0)
				{
					Hero.getInstance().showHeroFights(activeChar, heroclass, heroid, heropage);
				}
			}
			else if (_command.startsWith("_diary"))
			{
				String params = _command.substring(_command.indexOf("?") + 1);
				StringTokenizer st = new StringTokenizer(params, "&");
				int heroclass = Integer.parseInt(st.nextToken().split("=")[1]);
				int heropage = Integer.parseInt(st.nextToken().split("=")[1]);
				int heroid = Hero.getInstance().getHeroByClass(heroclass);
				if (heroid > 0)
				{
					Hero.getInstance().showHeroDiary(activeChar, heroclass, heroid, heropage);
				}
			}
			else
			{
				final IBypassHandler handler = BypassHandler.getInstance().getHandler(_command);
				if (handler != null)
				{
					handler.useBypass(_command, activeChar, null);
				}
				else
				{
					_log.log(Level.WARNING, getClient() + " sent not handled RequestBypassToServer: [" + _command + "]");
				}
			}
		}
		catch (Exception e)
		{
			_log.log(Level.WARNING, getClient() + " sent bad RequestBypassToServer: \"" + _command + "\"", e);
			if (activeChar.isGM())
			{
				StringBuilder sb = new StringBuilder(200);
				sb.append("<html><body>");
				sb.append("Bypass error: " + e + "<br1>");
				sb.append("Bypass command: " + _command + "<br1>");
				sb.append("StackTrace:<br1>");
				for (StackTraceElement ste : e.getStackTrace())
					sb.append(ste.toString() + "<br1>");
				sb.append("</body></html>");
				// item html
				NpcHtmlMessage msg = new NpcHtmlMessage(0, 12807);
				msg.setHtml(sb.toString());
				msg.disableValidation();
				activeChar.sendPacket(msg);
			}
		}
	}
	
	/**
	 * @param activeChar
	 */
	private static void comeHere(L2PcInstance activeChar)
	{
		L2Object obj = activeChar.getTarget();
		if (obj == null)
			return;
		if (obj instanceof L2Npc)
		{
			L2Npc temp = (L2Npc) obj;
			temp.setTarget(activeChar);
			temp.getAI().setIntention(CtrlIntention.AI_INTENTION_MOVE_TO, new L2CharPosition(activeChar.getX(), activeChar.getY(), activeChar.getZ(), 0));
		}
	}
	
	@Override
	public String getType()
	{
		return _C__23_REQUESTBYPASSTOSERVER;
	}
}
