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
package custom.Blessing;

import com.l2jserver.gameserver.instancemanager.QuestManager;
import com.l2jserver.gameserver.model.actor.L2Npc;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.quest.Quest;
import com.l2jserver.gameserver.model.quest.QuestState;
import com.l2jserver.gameserver.network.SystemMessageId;
import com.l2jserver.gameserver.network.serverpackets.SystemMessage;

/**
 *�iID�j   �iITEM_NAME�j
 * 17094	�`��S���n		���t�`��S���n�����ߡA���D��i�H���ɦۤv��������10�C�L�k����Υ��C
 * 17095	�`��S�F�|-1�p��	1~19	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����1~19�ϥΡC�L�k����Υ��C
 * 17096	�`��S�F�|-1.5�p��	1~19	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����1~19�ϥΡC�L�k����Υ��C
 * 17097	�`��S�F�|-2�p��	1~19	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����1~19�ϥΡC�L�k����Υ��C
 * 17098	�`��S�F�|-2.5�p��	1~19	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����1~19�ϥΡC�L�k����Υ��C
 * 17099	�`��S�F�|-3�p��	1~19	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����1~19�ϥΡC�L�k����Υ��C
 * 17100	�`��S�F�|-1�p��	20~39	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����20~39�ϥΡC�L�k����Υ��C
 * 17101	�`��S�F�|-1.5�p��	20~39	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����20~39�ϥΡC�L�k����Υ��C
 * 17102	�`��S�F�|-2�p��	20~39	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����20~39�ϥΡC�L�k����Υ��C
 * 17103	�`��S�F�|-2.5�p��	20~39	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����20~39�ϥΡC�L�k����Υ��C
 * 17104	�`��S�F�|-3�p��	20~39	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����20~39�ϥΡC�L�k����Υ��C
 * 17105	�`��S�F�|-1�p��	40~51	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����40~51�ϥΡC�L�k����Υ��C
 * 17106	�`��S�F�|-1.5�p��	40~51	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����40~51�ϥΡC�L�k����Υ��C
 * 17107	�`��S�F�|-2�p��	40~51	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����40~51�ϥΡC�L�k����Υ��C
 * 17108	�`��S�F�|-2.5�p��	40~51	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����40~51�ϥΡC�L�k����Υ��C
 * 17109	�`��S�F�|-3�p��	40~51	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����40~51�ϥΡC�L�k����Υ��C
 * 17110	�`��S�F�|-1�p��	52~60	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����52~60�ϥΡC�L�k����Υ��C
 * 17111	�`��S�F�|-1.5�p��	52~60	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����52~60�ϥΡC�L�k����Υ��C
 * 17112	�`��S�F�|-2�p��	52~60	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����52~60�ϥΡC�L�k����Υ��C
 * 17113	�`��S�F�|-2.5�p��	52~60	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����52~60�ϥΡC�L�k����Υ��C
 * 17114	�`��S�F�|-3�p��	52~60	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����52~60�ϥΡC�L�k����Υ��C
 * 17115	�`��S�F�|-1�p��	61~75	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����61~75�ϥΡC�L�k����Υ��C
 * 17116	�`��S�F�|-1.5�p��	61~75	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����61~75�ϥΡC�L�k����Υ��C
 * 17117	�`��S�F�|-2�p��	61~75	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����61~75�ϥΡC�L�k����Υ��C
 * 17118	�`��S�F�|-2.5�p��	61~75	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����61~75�ϥΡC�L�k����Υ��C
 * 17119	�`��S�F�|-3�p��	61~75	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����61~75�ϥΡC�L�k����Υ��C
 * 17120	�`��S�F�|-1�p��	76~79	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����76~79�ϥΡC�L�k����Υ��C
 * 17121	�`��S�F�|-1.5�p��	76~79	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����76~79�ϥΡC�L�k����Υ��C
 * 17122	�`��S�F�|-2�p��	76~79	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����76~79�ϥΡC�L�k����Υ��C
 * 17123	�`��S�F�|-2.5�p��	76~79	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����76~79�ϥΡC�L�k����Υ��C
 * 17124	�`��S�F�|-3�p��	76~79	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����76~79�ϥΡC�L�k����Υ��C
 * 17125	�`��S�F�|-1�p��	80~85	�i�H�����`��S����1�p�ɪ��`��S�F�|�C�ȭ�����80~85�ϥΡC�L�k����Υ��C
 * 17126	�`��S�F�|-1.5�p��	80~85	�i�H�����`��S����1.5�p�ɪ��`��S�F�|�C�ȭ�����80~85�ϥΡC�L�k����Υ��C
 * 17127	�`��S�F�|-2�p��	80~85	�i�H�����`��S����2�p�ɪ��`��S�F�|�C�ȭ�����80~85�ϥΡC�L�k����Υ��C
 * 17128	�`��S�F�|-2.5�p��	80~85	�i�H�����`��S����2.5�p�ɪ��`��S�F�|�C�ȭ�����80~85�ϥΡC�L�k����Υ��C
 * 17129	�`��S�F�|-3�p��	80~85	�i�H�����`��S����3�p�ɪ��`��S�F�|�C�ȭ�����80~85�ϥΡC�L�k����Υ��C
 */

/**
 * Event Code for "Blessing"
 * @author  Gnat
 * Update by pmq 12-10-2010
 */
public class Blessing extends Quest
{
	private static final int BLESSING               = 32783;    // ���֪����x
	private static final int NEVITS_VOICE           = 17094;    // �`��S���n
	private static final int NEVITS_HOURGLASS       = 17129;    // �`��S�F�|

	private static final int ADENA                  = 57;       // ����
	private static final int NEVITS_VOICE_PRICE     = 100000;   // �`��S���n����
	private static final int NEVITS_VOICE_TIME      = 20;       // �`��S���n�i�A�R�ɶ��i�w�p�ɬ����j
	private static final int NEVITS_HOURGLASS_PRICE = 5000000;  // �`��S�F�|����
	private static final int NEVITS_HOURGLASS_TIME  = 20;       // �`��S�F�|�i�A�R�ɶ��i�w�p�ɬ����j

	public Blessing(int questId, String name, String descr)
	{
		super(questId, name, descr);
		addStartNpc(BLESSING);
		addFirstTalkId(BLESSING);
		addTalkId(BLESSING);
	}

	@Override
	public String onAdvEvent(String event, L2Npc npc, L2PcInstance player)
	{
		String htmltext = "";
		QuestState st = player.getQuestState(getName());
		Quest q = QuestManager.getInstance().getQuest(getName());

		htmltext = event;
		if (event.equalsIgnoreCase("voice"))
		{
			long _curr_time = System.currentTimeMillis();
			String value = q.loadGlobalQuestVar(player.getAccountName());
			long _reuse_time = value == "" ? 0 : Long.parseLong(value);
			if (_curr_time > _reuse_time)
			{
				if (st.getQuestItemsCount(ADENA) > NEVITS_VOICE_PRICE)
				{
					st.takeItems(ADENA, NEVITS_VOICE_PRICE);
					st.giveItems(NEVITS_VOICE, 1);
					q.saveGlobalQuestVar(player.getAccountName(), Long.toString(System.currentTimeMillis() + (NEVITS_VOICE_TIME * 3600000)));
					htmltext = "";
				}
				else
					htmltext = "<html><body>���֪����x�G<br>�z���n�N�ڤ߻�F�A���z�n���m�������n���٤��Ӱ��O�C��U�h�x�H�̪����|�@�������z���}�ۡA���z����O��U���ɭԡA���H�ɨӧ�ڡC�@�������ֻP�z�P�b...</body></html>";
			}
			else
			{
				long _remaining_time = (_reuse_time - _curr_time) / 1000;
				int hours = (int) _remaining_time / 3600;
				int minutes = ((int) _remaining_time % 3600) / 60;
				if (hours > 0)
				{
					SystemMessage sm = SystemMessage.getSystemMessage(SystemMessageId.ITEM_PURCHASABLE_IN_S1_HOURS_S2_MINUTES);
					sm.addNumber(hours);
					sm.addNumber(minutes);
					player.sendPacket(sm);
					htmltext = "";
				}
				else if (minutes > 0)
				{
					SystemMessage sm = SystemMessage.getSystemMessage(SystemMessageId.ITEM_PURCHASABLE_IN_S1_MINUTES);
					sm.addNumber(minutes);
					player.sendPacket(sm);
					htmltext = "";
				}
				else
				{
					// Little glitch. There is no SystemMessage with seconds only.
					// If time is less than 1 minute player can buy scrolls
					if (st.getQuestItemsCount(ADENA) > NEVITS_VOICE_PRICE)
					{
						st.takeItems(ADENA, NEVITS_VOICE_PRICE);
						st.giveItems(NEVITS_VOICE, 1);
						q.saveGlobalQuestVar(player.getAccountName(), Long.toString(System.currentTimeMillis() + (NEVITS_VOICE_TIME * 3600000)));
						htmltext = "";
					}
					else
						htmltext = "<html><body>���֪����x�G<br>�z���n�N�ڤ߻�F�A���z�n���m�������n���٤��Ӱ��O�C��U�h�x�H�̪����|�@�������z���}�ۡA���z����O��U���ɭԡA���H�ɨӧ�ڡC�@�������ֻP�z�P�b...</body></html>";
				}
			}
		}
		else if (event.equalsIgnoreCase("hourglass"))
		{
			long _curr_time = System.currentTimeMillis();
			String value = q.loadGlobalQuestVar(player.getAccountName());
			long _reuse_time = value == "" ? 0 : Long.parseLong(value);
			if (_curr_time > _reuse_time)
			{
				if (st.getQuestItemsCount(ADENA) > NEVITS_HOURGLASS_PRICE)
				{
					st.takeItems(ADENA, NEVITS_HOURGLASS_PRICE);
					st.giveItems(NEVITS_HOURGLASS, 1);
					q.saveGlobalQuestVar(player.getAccountName(), Long.toString(System.currentTimeMillis() + (NEVITS_HOURGLASS_TIME * 3600000)));
					htmltext = "";
				}
				else
					htmltext = "<html><body>���֪����x�G<br>�z���n�N�ڤ߻�F�A���z�n���m�������n���٤��Ӱ��O�C��U�h�x�H�̪����|�@�������z���}�ۡA���z����O��U���ɭԡA���H�ɨӧ�ڡC�@�������ֻP�z�P�b...</body></html>";
			}
			else
			{
				long _remaining_time = (_reuse_time - _curr_time) / 1000;
				int hours = (int) _remaining_time / 3600;
				int minutes = ((int) _remaining_time % 3600) / 60;
				if (hours > 0)
				{
					SystemMessage sm = SystemMessage.getSystemMessage(SystemMessageId.ITEM_PURCHASABLE_IN_S1_HOURS_S2_MINUTES);
					sm.addNumber(hours);
					sm.addNumber(minutes);
					player.sendPacket(sm);
					htmltext = "";
				}
				else if (minutes > 0)
				{
					SystemMessage sm = SystemMessage.getSystemMessage(SystemMessageId.ITEM_PURCHASABLE_IN_S1_MINUTES);
					sm.addNumber(minutes);
					player.sendPacket(sm);
					htmltext = "";
				}
				else
				{
					// Little glitch. There is no SystemMessage with seconds only.
					// If time is less than 1 minute player can buy scrolls
					if (st.getQuestItemsCount(ADENA) > NEVITS_HOURGLASS_PRICE)
					{
						st.takeItems(ADENA, NEVITS_HOURGLASS_PRICE);
						st.giveItems(NEVITS_HOURGLASS, 1);
						q.saveGlobalQuestVar(player.getAccountName(), Long.toString(System.currentTimeMillis() + (NEVITS_HOURGLASS_TIME * 3600000)));
						htmltext = "";
					}
					else
						htmltext = "<html><body>���֪����x�G<br>�z���n�N�ڤ߻�F�A���z�n���m�������n���٤��Ӱ��O�C��U�h�x�H�̪����|�@�������z���}�ۡA���z����O��U���ɭԡA���H�ɨӧ�ڡC�@�������ֻP�z�P�b...</body></html>";
				}
			}
		}

		return htmltext;
	}

	@Override
	public String onFirstTalk(L2Npc npc, L2PcInstance player)
	{
		String htmltext = "";
		QuestState st = player.getQuestState(getName());
		if (st == null)
		{
			Quest q = QuestManager.getInstance().getQuest(getName());
			st = q.newQuestState(player);
		}
		if (player.getLevel() <= 19)
			htmltext = "32783-l1.htm";
		if (player.getLevel() >= 20 && player.getLevel() <= 39)
			htmltext = "32783-l2.htm";
		if (player.getLevel() >= 40 && player.getLevel() <= 51)
			htmltext = "32783-l3.htm";
		if (player.getLevel() >= 52 && player.getLevel() <= 60)
			htmltext = "32783-l4.htm";
		if (player.getLevel() >= 61 && player.getLevel() <= 75)
			htmltext = "32783-l5.htm";
		if (player.getLevel() >= 76 && player.getLevel() <= 79)
			htmltext = "32783-l6.htm";
		if (player.getLevel() >= 80 && player.getLevel() <= 85)
			htmltext = "32783-l7.htm";
		return htmltext;
	}

	public static void main(String[] args)
	{
		new Blessing(-1, "Blessing", "custom");
	}
}