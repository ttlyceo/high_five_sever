# quest by zerghase
# Update by pmq 09-07-2010

import sys
from com.l2jserver import Config 
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "42_HelpTheUncle"

# NPC
WATERS     = 30828
SOPHYA     = 30735
# ITEM
TRIDENT    = 291
MAP_PIECE  = 7548
MAP        = 7549
PET_TICKET = 7583
# MOBs
MONSTER_EYE_DESTROYER = 20068
MONSTER_EYE_GAZER     = 20266
# ETC
MAX_COUNT = 30

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event == "1":
			htmltext="30828-01.htm"
			st.set("cond","1")
			st.playSound("ItemSound.quest_accept")
			st.setState(State.STARTED)
		elif event == "3" and st.getQuestItemsCount(TRIDENT):
			htmltext = "30828-03.htm"
			st.takeItems(TRIDENT,1)
			st.set("cond","2")
			st.playSound("ItemSound.quest_accept")
		elif event == "4" and st.getQuestItemsCount(MAP_PIECE) >= MAX_COUNT :
			htmltext = "30828-05.htm"
			st.takeItems(MAP_PIECE,MAX_COUNT)
			st.giveItems(MAP,1)
			st.set("cond","4")
			st.playSound("ItemSound.quest_accept")
		elif event == "5" and st.getQuestItemsCount(MAP):
			htmltext = "30735-06.htm"
			st.takeItems(MAP,1)
			st.set("cond","5")
			st.playSound("ItemSound.quest_accept")
		elif event == "7" :
			htmltext = "30828-07.htm"
			st.giveItems(PET_TICKET,1)
			st.unset("cond")
			st.exitQuest(False)
			st.playSound("ItemSound.quest_finish")
		return htmltext

	def onTalk(self, npc, player):
		htmltext="<html><body>目前沒有執行任務，或條件不符。</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId=npc.getNpcId()
		id = st.getState()
		cond=st.getInt("cond")

		if id == State.COMPLETED :
			htmltext = "<html><body>這是已經完成的任務。</body></html>"
		elif id == State.CREATED:
			if npcId == WATERS and cond == 0 :
				if player.getLevel() >= 25 :
					htmltext = "30828-00.htm"
				else:
					htmltext = "30828-00a.htm"
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == WATERS :
				if cond == 1 :
					if not st.getQuestItemsCount(TRIDENT):
						htmltext = "30828-01a.htm"
					else :
						htmltext = "30828-02.htm"
				elif cond == 2 :
					htmltext = "30828-03a.htm"
				elif cond == 3 :
					htmltext = "30828-04.htm"
				elif cond == 4 :
					htmltext = "30828-05a.htm"
				elif cond == 5 :
					htmltext = "30828-06.htm"
			elif npcId == SOPHYA :
				if cond == 4 and st.getQuestItemsCount(MAP):
					htmltext = "30735-05.htm"
				elif cond == 5:
					htmltext = "30735-06a.htm"
		return htmltext

	def onKill(self,npc,player,isPet):
		st = player.getQuestState(qn)
		if not st : return
		if st.getState() != State.STARTED : return

		npcId = npc.getNpcId()
		cond = st.getInt("cond")
		if cond == 2 :
			numItems,chance = divmod(100*Config.RATE_QUEST_DROP,100)
			if self.getRandom(100) < chance :
				numItems = numItems +1  
			pieces = st.getQuestItemsCount(MAP_PIECE)
			if pieces + numItems >= MAX_COUNT :
				numItems = MAX_COUNT - pieces
				if numItems != 0 :
					st.set("cond","3")
					st.playSound("ItemSound.quest_middle")
			else :
				st.playSound("ItemSound.quest_itemget")
			st.giveItems(MAP_PIECE,int(numItems))
		return

QUEST		= Quest(42,qn,"幫幫叔叔吧!")

QUEST.addStartNpc(WATERS)

QUEST.addTalkId(WATERS)
QUEST.addTalkId(SOPHYA)

QUEST.addKillId(MONSTER_EYE_DESTROYER)
QUEST.addKillId(MONSTER_EYE_GAZER)