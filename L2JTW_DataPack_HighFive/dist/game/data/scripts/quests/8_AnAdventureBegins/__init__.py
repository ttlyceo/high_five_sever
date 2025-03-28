# Created by CubicVirtuoso
# Any problems feel free to drop by #l2j-datapack on irc.freenode.net

import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "8_AnAdventureBegins"

# NPCs
JASMINE = 30134
ROSELYN = 30355
HARNE   = 30144

# ITEM
ROSELYNS_NOTE = 7573

# REWARDS
ADENA      = 57
SCROLL_OF_ESCAPE_GIRAN = 7559
MARK_OF_TRAVELER       = 7570

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [ROSELYNS_NOTE]

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event == "30134-03.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "30355-02.htm" :
			st.giveItems(ROSELYNS_NOTE,1)
			st.set("cond","2")
			st.playSound("ItemSound.quest_middle")
		elif event == "30144-02.htm" :
			st.takeItems(ROSELYNS_NOTE,-1)
			st.set("cond","3")
			st.playSound("ItemSound.quest_middle")
		elif event == "30134-06.htm" :
			st.giveItems(SCROLL_OF_ESCAPE_GIRAN,1)
			st.giveItems(MARK_OF_TRAVELER, 1)
			st.unset("cond")
			st.exitQuest(False)
			st.playSound("ItemSound.quest_finish")
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
		elif id == State.CREATED :
			if npcId == JASMINE and cond == 0 :
				if player.getRace().ordinal() == 2 :
					htmltext = "30134-01.htm"
					st.exitQuest(1)
					if player.getLevel() >= 3 :
						htmltext = "30134-02.htm"
					else :
						htmltext = "30134-01.htm"
						st.exitQuest(1)
		elif id == State.STARTED : 
			if npcId == ROSELYN and cond :
				if st.getQuestItemsCount(ROSELYNS_NOTE) == 0 :
					htmltext = "30355-01.htm"
				else :
					htmltext = "30355-03.htm"
			elif npcId == JASMINE :
				if cond == 1 :
					htmltext = "30134-04.htm"
				elif cond == 3 :
					htmltext = "30134-05.htm"
			elif npcId == HARNE :
				if cond == 2 and st.getQuestItemsCount(ROSELYNS_NOTE) > 0 :
					htmltext = "30144-01.htm"
				elif cond == 3 :
					htmltext = "30144-03.htm"
		return htmltext

QUEST		= Quest(8,qn,"冒險的開始")

QUEST.addStartNpc(JASMINE)

QUEST.addTalkId(JASMINE)
QUEST.addTalkId(ROSELYN)
QUEST.addTalkId(HARNE)