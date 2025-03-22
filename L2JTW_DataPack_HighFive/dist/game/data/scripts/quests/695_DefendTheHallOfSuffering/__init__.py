#authoor by d0S

import sys

from com.l2jserver.gameserver.datatables import SkillTable
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "695_DefendTheHallOfSuffering"

# ���ȸ��
# 695	1	�W�h�ëǨ��m	���íW�h�ë�	�b�������ؤ��������ԫǡA�x�x�S���ڥq��N�F���íW�h�ëǪ����ȡC�����שҦ��ж������}�l���~�F��_���A�M��A�h�B�z���M�L���`�M�h�C\n\n�n�y�����ؼЩǪ�-��u �J�����w���B��u �Jù�}�w��\n	0															0															0	0	0	75	82	0	�W�h�ë�	1	1	1	32603	-183296	205715	-12896	�S�����󭭨�	�����x�θչϧ�^�Q�_�I�a�̩Ҧ��⪺�W�h�ëǡA�M���Ǧ��Q�n��_�O�q�C�]���b�������ئa�Ϫ����ԫǡA�x�x�S���ڥq���b�M��_�I�a�Ӫ���Ƶo�͡C	0																																																																						0						0	0	0	285	1	2	-1002	736										2	0	1										

#NPCs
Keucereus     = 32548
Tepios        = 32603
Tepiosinst    = 32530
Mouthofekimus = 32537

#items
Mark = 13691

class Quest (JQuest) :
	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		#self.questItemIds = [Mark]
		self.Lock = 0

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event == "32603-02.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			htmltext = "32603-03.htm"
		elif id == State.CREATED and npcId == Tepios and cond == 0:
			if player.getLevel() >= 75 and player.getLevel() <= 82 and st.getQuestItemsCount(Mark) == 1:
				htmltext = "32603-01.htm"
			elif player.getLevel() >= 75 and player.getLevel() <= 82 and st.getQuestItemsCount(Mark) == 0:
				htmltext = "32603-05.htm"
			else :
				htmltext = "32603-00.htm"
		elif id == State.STARTED and npcId == Mouthofekimus and cond == 1:
			htmltext = "32537-01.htm"
		elif id == State.STARTED and npcId == Tepiosinst and cond == 1:
			htmltext = "32530-01.htm"
			self.Lock = 1
		elif id == State.STARTED and npcId == Tepios and cond == 1:
			if self.Lock == 1:
				if st.getQuestItemsCount(Mark) == 1:
					htmltext = "32603-04.htm"
					st.exitQuest(True)
					st.giveItems(736,1)
				else :
					htmltext = "32603-04.htm"
					st.exitQuest(True)
					st.giveItems(736,1)
				st.playSound("ItemSound.quest_finish")
				self.Lock = 0
			else :
				htmltext = "32603-04.htm"
		return htmltext

QUEST		= Quest(695,qn,"�W�h�ëǨ��m")

QUEST.addStartNpc(Tepios)
QUEST.addTalkId(Tepios)
QUEST.addStartNpc(Mouthofekimus)
QUEST.addTalkId(Mouthofekimus)
QUEST.addTalkId(Tepiosinst)