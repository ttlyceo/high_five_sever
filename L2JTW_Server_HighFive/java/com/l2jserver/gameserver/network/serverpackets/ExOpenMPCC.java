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
 *
 * @author  chris_00
 *
 * opens the CommandChannel Information window
 *
 */
public class ExOpenMPCC extends L2GameServerPacket
{
	
	private static final String _S__FE_25_EXOPENMPCC = "[S] FE:12 ExOpenMPCC";
	
	@Override
	protected void writeImpl()
	{
		writeC(0xfe);
		writeH(0x12);
		
	}
	
	@Override
	public String getType()
	{
		return _S__FE_25_EXOPENMPCC;
	}
	
}
