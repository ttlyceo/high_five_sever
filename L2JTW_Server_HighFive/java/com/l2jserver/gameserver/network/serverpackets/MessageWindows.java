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
package com.l2jserver.gameserver.network.serverpackets;

/**
 * This class ...
 *
 * @version $Revision: 1.3.2.1.2.3 $ $Date: 2005/03/27 15:29:39 $
 */
public final class MessageWindows extends L2GameServerPacket
{
	private static final String _S__be_MessageWindows = "[S] be MessageWindows";
	
	int _id = 0;
	public MessageWindows(int id)
	{
		_id = id;
	}
	
	@Override
	protected void writeImpl()
	{
		writeC(0xfe);
		writeH(0xbe);
		writeC(0xe5);
		writeC(0x90);
		writeC(0x00);
		writeC(0x4c);
		writeD(0x00);
		
		
	}
	
	/* (non-Javadoc)
	 * @see com.l2jserver.gameserver.serverpackets.ServerBasePacket#getType()
	 */
	@Override
	public String getType()
	{
		return _S__be_MessageWindows;
	}
}