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
package teleports.FreyaTeleport;

import com.l2jserver.gameserver.model.actor.L2Npc;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.quest.Quest;
import com.l2jserver.gameserver.model.quest.QuestState;

public class FreyaTeleport extends Quest
{
	private final static int NPC = 32734;

	public FreyaTeleport(int questId, String name, String descr)
	{
		super(questId, name, descr);
		addStartNpc(NPC);
		addTalkId(NPC);
	}

	@Override
	public String onTalk(L2Npc npc, L2PcInstance player)
	{
		String htmltext = "";
		QuestState st = player.getQuestState(getName());
		if (player.getLevel() >= 80)
			player.teleToLocation(-180218, 185923, -10576);
		else
			htmltext = "<html><body>�x�x �J�ܦ̴��G<br>���M���p���A����ı�o���a��A�ӻ��٬O�ܦM�I�C�ڻ{�������ӱN�öQ���ͩR�G�J���ҡA�ЧA�̸ѡC��M�A�p�G�A���i�@�ǹ�O���ܱo��j�����ܡA������H�ɳ��|�w��A�C<br>(�u��<font color=\"LEVEL\">����80</font>�H�W������~��i�J�f�����ءC)</body></html>";

		st.exitQuest(true);
		return htmltext;
	}

	public static void main(String[] args)
	{
		new FreyaTeleport(-1, "FreyaTeleport", "teleports");
	}
}