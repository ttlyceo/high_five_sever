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

import com.l2jserver.Config;
import com.l2jserver.gameserver.datatables.AdminTable;
import com.l2jserver.gameserver.handler.AdminCommandHandler;
import com.l2jserver.gameserver.handler.IAdminCommandHandler;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.util.GMAudit;
import com.l2jserver.gameserver.datatables.MessageTable;

/**
 * This class handles all GM commands triggered by //command
 *
 * @version $Revision: 1.3.4.2 $ $Date: 2005/03/27 15:29:29 $
 */
public final class SendBypassBuildCmd extends L2GameClientPacket
{
	private static final String _C__74_SENDBYPASSBUILDCMD = "[C] 74 SendBypassBuildCmd";

	public static final int GM_MESSAGE = 9;
	public static final int ANNOUNCEMENT = 10;
	
	private String _command;
	
	@Override
	protected void readImpl()
	{
		_command = readS();
		if (_command != null)
			_command = _command.trim();
	}
	
	@Override
	protected void runImpl()
	{
		L2PcInstance activeChar = getClient().getActiveChar();
		if(activeChar == null)
			return;
		
		String command = "admin_" + _command.split(" ")[0];
		
		IAdminCommandHandler ach = AdminCommandHandler.getInstance().getHandler(command);
		
		if (ach == null)
		{
			if ( activeChar.isGM() )
				/* Move To MessageTable For L2JTW
				activeChar.sendMessage("The command " + command.substring(6) + " does not exists!");
				*/
				activeChar.sendMessage(MessageTable.Messages[369].getExtra(1) + command.substring(6) + MessageTable.Messages[369].getExtra(2));
			
			_log.warning("No handler registered for admin command '" + command + "'");
			return;
		}
		
		if (!AdminTable.getInstance().hasAccess(command , activeChar.getAccessLevel()))
		{
			/* Move To MessageTable For L2JTW
			activeChar.sendMessage("You don't have the access right to use this command!");
			*/
			activeChar.sendMessage(370);
			_log.warning("Character " + activeChar.getName() + " tryed to use admin command " + command + ", but have no access to it!");
			return;
		}
		
		if (Config.GMAUDIT)
			GMAudit.auditGMAction(activeChar.getName()+" ["+activeChar.getObjectId()+"]", _command, (activeChar.getTarget() != null?activeChar.getTarget().getName():"no-target"));
		
		ach.useAdminCommand("admin_" + _command, activeChar);
	}
	
	@Override
	public String getType()
	{
		return _C__74_SENDBYPASSBUILDCMD;
	}
}
