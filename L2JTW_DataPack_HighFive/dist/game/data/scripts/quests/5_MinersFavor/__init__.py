# Made by Mr. Have fun! Version 0.2
# Update by pmq 30-06-2010

import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "5_MinersFavor"

# NPCs
BOLTER = 30554
SHARI  = 30517
GARITA = 30518
REED   = 30520
BRUNON = 30526

# ITEMS 
BOLTERS_LIST         = 1547
MINING_BOOTS         = 1548
MINERS_PICK          = 1549
BOOMBOOM_POWDER      = 1550
REDSTONE_BEER        = 1551
BOLTERS_SMELLY_SOCKS = 1552
 
# REWARD 
NECKLACE = 906
 
class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [MINING_BOOTS, MINERS_PICK, BOOMBOOM_POWDER, REDSTONE_BEER, BOLTERS_LIST, BOLTERS_SMELLY_SOCKS]

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event == "30554-03.htm" :
			st.giveItems(BOLTERS_LIST,1)
			st.giveItems(BOLTERS_SMELLY_SOCKS,1)
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "30526-02.htm" :
			st.takeItems(BOLTERS_SMELLY_SOCKS,-1)
			st.giveItems(MINERS_PICK,1)
			st.playSound("ItemSound.quest_itemget")
			if st.getQuestItemsCount(BOLTERS_LIST) and (st.getQuestItemsCount(MINING_BOOTS) + st.getQuestItemsCount(MINERS_PICK) + st.getQuestItemsCount(BOOMBOOM_POWDER) + st.getQuestItemsCount(REDSTONE_BEER) >= 4) :
				st.set("cond","2")
				st.playSound("ItemSound.quest_middle")
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>目前沒有執行任務，或條件不符。</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			htmltext = "<html><body>這是已經完成的任務。</body></html>"
		elif id == State.CREATED:
			if npcId == BOLTER and cond == 0 :
				if player.getLevel() >= 2 :
					htmltext = "30554-02.htm"
				else:
					htmltext = "30554-01.htm"
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == SHARI :
				if cond == 1 and st.getQuestItemsCount(BOLTERS_LIST) :
					if st.getQuestItemsCount(BOOMBOOM_POWDER) == 0 :
						htmltext = "30517-01.htm"
						st.giveItems(BOOMBOOM_POWDER,1)
						st.playSound("ItemSound.quest_itemget")
					else:
						htmltext = "30517-02.htm"
				elif cond == 2 :
					htmltext = "30517-02.htm"
			elif npcId == GARITA :
				if cond == 1 and st.getQuestItemsCount(BOLTERS_LIST) :
					if st.getQuestItemsCount(MINING_BOOTS) == 0 :
						htmltext = "30518-01.htm"
						st.giveItems(MINING_BOOTS,1)
						st.playSound("ItemSound.quest_itemget")
					else:
						htmltext = "30518-02.htm"
				elif cond == 2 :
					htmltext = "30518-02.htm"
			elif npcId == REED :
				if cond == 1 and st.getQuestItemsCount(BOLTERS_LIST) :
					if st.getQuestItemsCount(REDSTONE_BEER) == 0 :
						htmltext = "30520-01.htm"
						st.giveItems(REDSTONE_BEER,1)
						st.playSound("ItemSound.quest_itemget")
					else:
						htmltext = "30520-02.htm"
				elif cond == 2 :
					htmltext = "30520-02.htm"
			elif npcId == BRUNON :
				if cond == 1 and st.getQuestItemsCount(BOLTERS_LIST) :
					if st.getQuestItemsCount(MINERS_PICK) == 0 :
						htmltext = "30526-01.htm"
					else:
						htmltext = "30526-03.htm"
				elif cond == 2 :
					htmltext = "30526-03.htm"
			elif npcId == BOLTER :
				if cond == 1 :
					htmltext = "30554-04.htm"
				elif cond == 2 :
					htmltext = "30554-06.htm"
					st.giveItems(57,2466)
					st.giveItems(NECKLACE,1)
					st.addExpAndSp(5672,446)
					st.unset("cond")
					st.exitQuest(False)
					st.playSound("ItemSound.quest_finish")
			if st.getQuestItemsCount(BOLTERS_LIST) and (st.getQuestItemsCount(MINING_BOOTS) + st.getQuestItemsCount(MINERS_PICK) + st.getQuestItemsCount(BOOMBOOM_POWDER) + st.getQuestItemsCount(REDSTONE_BEER) >= 4) :
				st.set("cond","2")
				st.playSound("ItemSound.quest_middle")
		return htmltext

QUEST		= Quest(5,qn,"礦工的囑託")

QUEST.addStartNpc(BOLTER)

QUEST.addTalkId(BOLTER)
QUEST.addTalkId(SHARI)
QUEST.addTalkId(GARITA)
QUEST.addTalkId(REED)
QUEST.addTalkId(BRUNON)
QUEST.addTalkId(BOLTER) 