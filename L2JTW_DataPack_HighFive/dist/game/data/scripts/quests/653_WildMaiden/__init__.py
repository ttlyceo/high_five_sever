# Made by DrLecter, based on a Polo script and a DoomIta contribution
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "653_WildMaiden"
#Npc
SUKI = 32013
GALIBREDO = 30181

#Items
SOE = 736

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)

	def onAdvEvent (self,event,npc,player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		if event == "32013-03.htm" :
			if st.getQuestItemsCount(SOE):
				st.set("cond","1")
				st.setState(State.STARTED)
				st.playSound("ItemSound.quest_accept")
				st.takeItems(SOE,1)
				npc.deleteMe()
			else :
				htmltext = "32013-04.htm"
		elif event == "32013-04a.htm" :
			st.exitQuest(1)
			st.playSound("ItemSound.quest_giveup")
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.CREATED:
			if npcId == SUKI and cond == 0 :
				if player.getLevel() >= 36 :
					htmltext = "32013-02.htm"
				else:
					htmltext = "32013-01.htm"
					st.exitQuest(1)
		elif id == State.STARTED:
			if npcId == GALIBREDO :
				if cond == 1 :
					htmltext = "30181-01.htm"
					st.giveItems(57,2883)
					st.playSound("ItemSound.quest_finish")
					st.exitQuest(1)
		return htmltext

QUEST		= Quest(653,qn,"�K�߿��y���֤k")

QUEST.addStartNpc(SUKI)

QUEST.addTalkId(SUKI)
QUEST.addTalkId(GALIBREDO)