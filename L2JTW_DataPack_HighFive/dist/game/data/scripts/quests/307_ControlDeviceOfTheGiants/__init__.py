# Created by pmq 20-09-2010

import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "307_ControlDeviceOfTheGiants"

# NPC
DROPH = 32711               # �G�H���I�a �w����
# L2RaidBoss
GORGOLOS          = 25467   # ���y���� �����ĭۥq
LAST_TITAN_UTENUS = 25470   # ���y���� �̫᪺�U���H �S�S�V��
GIANT_MARPANAK    = 25680   # ���y���� ���H ���������J
HEKATON_PRIME     = 25687   # ���y���� �¥d�S�쫬
# ITEM
CET_1_SHEET = 14829         # �}�]���I���� ��1��
CET_2_SHEET = 14830         # �}�]���I���� ��2��
CET_3_SHEET = 14831         # �}�]���I���� ��3��
# NpcId:[x,y,z] # name
RADAR  = { 25467:[0,0,0] }  # ���y���� �����ĭۥq
RADAR1 = { 25470:[0,0,0] }  # ���y���� �̫᪺�U���H �S�S�V��
RADAR2 = { 25680:[0,0,0] }  # ���y���� ���H ���������J
RADAR3 = { 25687:[0,0,0] }  # ���y���� �¥d�S�쫬

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)

	def onAdvEvent (self,event,npc,player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st: return

		if event == "32711-03.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		if event.isdigit() :
			htmltext = None
			npcId = int(event)
			if npcId in RADAR.keys():
				x,y,z = RADAR[npcId]
				st.addRadar(x,y,z)
				htmltext = "32711-06.htm"
			elif npcId in RADAR1.keys():
				x,y,z = RADAR1[npcId]
				st.addRadar(x,y,z)
				htmltext = "32711-07.htm"
			elif npcId in RADAR2.keys():
				x,y,z = RADAR2[npcId]
				st.addRadar(x,y,z)
				htmltext = "32711-08.htm"
			elif npcId in RADAR3.keys():
				x,y,z = RADAR3[npcId]
				st.addRadar(x,y,z)
				htmltext = "MISS"
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st: return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.CREATED :
			if npcId == DROPH and cond == 0 :
				if player.getLevel() >= 79 :
					htmltext = "32711-01.htm"
				else :
					htmltext = "32711-00.htm"
					st.exitQuest(1)
		elif id == State.STARTED:
			if npcId == DROPH :
				if cond == 1 :
					htmltext = "32711-09.htm"
		return htmltext

	def onKill (self,npc,player,isPet) :
		st = player.getQuestState(qn)
		if not st : return
		if st.getState() != State.STARTED : return
		npcId = npc.getNpcId()
		cond = st.getInt("cond")
		if cond == 1 :
			if npcId == GORGOLOS :
				st.giveItems(CET_1_SHEET,1)
				st.playSound("ItemSound.quest_itemget")
			elif npcId == LAST_TITAN_UTENUS :
				st.giveItems(CET_2_SHEET,1)
				st.playSound("ItemSound.quest_itemget")
			elif npcId == GIANT_MARPANAK :
				st.giveItems(CET_3_SHEET,1)
				st.playSound("ItemSound.quest_itemget")
			if st.getQuestItemsCount(CET_1_SHEET) >= 1 or st.getQuestItemsCount(CET_2_SHEET) >= 1 or st.getQuestItemsCount(CET_3_SHEET) >= 1 :
				st.set("cond","2")
				st.playSound("ItemSound.quest_accept")
		return

QUEST = Quest(307, qn, "���H�̪��Ϊv�˸m")

QUEST.addStartNpc(DROPH)
QUEST.addTalkId(DROPH)

QUEST.addKillId(GORGOLOS)
QUEST.addKillId(LAST_TITAN_UTENUS)
QUEST.addKillId(GIANT_MARPANAK)
#QUEST.addKillId(HEKATON_PRIME)