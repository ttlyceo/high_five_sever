# By L2J_JP SANDMAN
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "654_JourneytoaSettlement"

# NPC
SPIRIT   = 31453  # �L�W���F��
# MOB
TARGET_1 = 21294  # �s���ܦ�
TARGET_2 = 21295  # �s���ܦϥ���
# ITEM
ITEM     = 8072   # �ܦϥ֭�
# REWARD
SCROLL   = 8073   # �ܵY���F�����ɯ}�G��

class Quest (JQuest) :

	def __init__(self,id,name,descr): 
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [ITEM]

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		if event == "31453-2.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "31453-3.htm" :
			st.set("cond","2")
			st.playSound("ItemSound.quest_middle")
		elif event == "31453-5.htm" :
			st.giveItems(SCROLL,1)
			st.takeItems(ITEM,1)
			st.playSound("ItemSound.quest_finish")
			st.exitQuest(1)
			st.unset("cond")
		return htmltext

	def onTalk (Self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st: return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.CREATED:
			preSt = player.getQuestState("119_LastImperialPrince")
			if npcId == SPIRIT and cond == 0 :
				if preSt.getState() == State.COMPLETED :
					if player.getLevel() >= 74 :
						htmltext = "31453-1.htm"
					else :
						htmltext = "31453-0.htm" # rocknow �ץ�
						st.exitQuest(1)
				else :
					htmltext = "<html><body>�����������u<font color=\"LEVEL\">�̫᪺�Ӥl</font>�v�����ȡC</body></html>"
					st.exitQuest(1)
		elif id == State.STARTED:
			if npcId == SPIRIT :
				if cond == 1 :
					htmltext = "31453-2.htm"
				elif cond == 3 :
					htmltext = "31453-4.htm"
		return htmltext

	def onKill (self,npc,player,isPet) :
		st = player.getQuestState(qn)
		if not st: return
		npcId = npc.getNpcId()
		if st.getInt("cond") == 2 and self.getRandom(100) < 5 :
			st.set("cond","3")
			st.giveItems(ITEM,1)
			st.playSound("ItemSound.quest_middle")
		return

QUEST		= Quest(654,qn,"�ﱵ�̲ת�����")

QUEST.addStartNpc(SPIRIT)
QUEST.addTalkId(SPIRIT)
QUEST.addKillId(TARGET_1)
QUEST.addKillId(TARGET_2)