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
package quests.Q289_NoMoreSoupForYou;

import com.l2jserver.gameserver.model.actor.L2Npc;
import com.l2jserver.gameserver.model.actor.instance.L2PcInstance;
import com.l2jserver.gameserver.model.quest.Quest;
import com.l2jserver.gameserver.model.quest.QuestState;
import com.l2jserver.gameserver.model.quest.State;
import com.l2jserver.gameserver.util.Util;

public class Q289_NoMoreSoupForYou extends Quest
{
	public static final int STAN = 30200;
	public static final int RATE = 5;
	public static final int SOUP = 15712;
	
	public static final String qn = "289_NoMoreSoupForYou";
	
	private static final int[] MOBS =
	{
		18908,
		22779,
		22786,
		22787,
		22788
	};
	
	private static final int[][] WEAPONS =
	{
		{
			10377,
			1
		},
		{
			10401,
			1
		},
		{
			10401,
			2
		},
		{
			10401,
			3
		},
		{
			10401,
			4
		},
		{
			10401,
			5
		},
		{
			10401,
			6
		}
	};
	
	private static final int[][] ARMORS =
	{
		{
			15812,
			1
		},
		{
			15813,
			1
		},
		{
			15814,
			1
		},
		{
			15791,
			1
		},
		{
			15787,
			1
		},
		{
			15784,
			1
		},
		{
			15781,
			1
		},
		{
			15778,
			1
		},
		{
			15775,
			1
		},
		{
			15774,
			5
		},
		{
			15773,
			5
		},
		{
			15772,
			5
		},
		{
			15693,
			5
		},
		{
			15657,
			5
		},
		{
			15654,
			5
		},
		{
			15651,
			5
		},
		{
			15648,
			5
		},
		{
			15645,
			5
		}
	};
	
	public Q289_NoMoreSoupForYou(int id, String name, String descr)
	{
		super(id, name, descr);
		
		addStartNpc(STAN);
		addTalkId(STAN);
		
		for (int i : MOBS)
		{
			addKillId(i);
		}
	}
	
	public static void main(String[] args)
	{
		new Q289_NoMoreSoupForYou(289, qn, "No More Soup For You");
	}
	
	@Override
	public String onAdvEvent(String event, L2Npc npc, L2PcInstance player)
	{
		String htmltext = event;
		QuestState st = player.getQuestState(qn);
		if (st == null)
		{
			return htmltext;
		}
		int b = getRandom(18);
		int c = getRandom(7);
		
		if (npc.getNpcId() == STAN)
		{
			if (event.equalsIgnoreCase("30200-03.htm"))
			{
				st.set("cond", "1");
				st.setState(State.STARTED);
				st.playSound("ItemSound.quest_accept");
			}
			else if (event.equalsIgnoreCase("30200-05.htm"))
			{
				if (st.getQuestItemsCount(SOUP) >= 500)
				{
					st.giveItems(WEAPONS[c][0], WEAPONS[c][1]);
					st.takeItems(SOUP, 500);
					st.playSound("ItemSound.quest_accept");
					htmltext = "30200-04.htm";
				}
				else
				{
					htmltext = "30200-07.htm";
				}
			}
			else if (event.equalsIgnoreCase("30200-06.htm"))
			{
				if (st.getQuestItemsCount(SOUP) >= 100)
				{
					st.giveItems(ARMORS[b][0], ARMORS[b][1]);
					st.takeItems(SOUP, 100);
					st.playSound("ItemSound.quest_accept");
					htmltext = "30200-04.htm";
				}
				else
				{
					htmltext = "30200-07.htm";
				}
			}
		}
		return htmltext;
	}
	
	@Override
	public String onTalk(L2Npc npc, L2PcInstance player)
	{
		String htmltext = "<html><body>目前沒有執行任務，或條件不符。</body></html>";
		QuestState st = player.getQuestState(qn);
		if (st == null)
		{
			return htmltext;
		}
		
		if (npc.getNpcId() == STAN)
		{
			switch (st.getState())
			{
				case State.CREATED:
					QuestState _prev = player.getQuestState("252_ItSmellsDelicious");
					if ((_prev != null) && _prev.isCompleted() && (player.getLevel() >= 82))
					{
						htmltext = "30200-01.htm";
					}
					else
					{
						htmltext = "30200-00.htm";
					}
					break;
				case State.STARTED:
					if (st.getInt("cond") == 1)
					{
						if (st.getQuestItemsCount(SOUP) >= 100)
						{
							htmltext = "30200-04.htm";
						}
						else
						{
							htmltext = "30200-03.htm";
						}
					}
					break;
			}
		}
		return htmltext;
	}
	
	@Override
	public String onKill(L2Npc npc, L2PcInstance player, boolean isPet)
	{
		QuestState st = player.getQuestState(getName());
		int npcId = npc.getNpcId();
		if ((st == null) || (st.getState() != State.STARTED))
		{
			return null;
		}
		if (Util.contains(MOBS, npcId))
		{
			st.giveItems(SOUP, 1 * RATE);
			st.playSound("ItemSound.quest_itemget");
		}
		return super.onKill(npc, player, isPet);
	}
}
