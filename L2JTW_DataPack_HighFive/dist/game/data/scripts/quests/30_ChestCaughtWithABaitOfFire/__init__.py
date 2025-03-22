# Made by Ethernaly ethernaly@email.it
# cleanup by DrLecter for the Official L2J Datapack Project.
# Visit http://www.l2jdp.com/forum/ for more details.
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "30_ChestCaughtWithABaitOfFire"

# NPC
LINNAEUS = 31577
RUKAL    = 30629

# ITEM and REWARD
RED_TREASURE_BOX    = 6511
RUKAL_MUSICAL       = 7628
PROTECTION_NECKLACE = 916

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
  
	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event== "31577-02.htm" :
			st.set("cond","1")
			st.playSound("ItemSound.quest_accept")
			st.setState(State.STARTED)
		elif event == "31577-04a.htm" and st.getQuestItemsCount(RED_TREASURE_BOX) :
			htmltext="31577-04.htm"
			st.giveItems(RUKAL_MUSICAL, 1)
			st.takeItems(RED_TREASURE_BOX,-1)
			st.set("cond","2")
			st.playSound("ItemSound.quest_middle")
		elif event == "30629-02.htm" and st.getQuestItemsCount(RUKAL_MUSICAL) :
			htmltext = "30629-03.htm"
			st.giveItems(PROTECTION_NECKLACE, 1)
			st.takeItems(RUKAL_MUSICAL,-1)
			st.unset("cond")
			st.exitQuest(False)
			st.playSound("ItemSound.quest_finish")
		return htmltext

	def onTalk(self, npc, player):
		htmltext="<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId=npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			htmltext = "<html><body>�o�O�w�g���������ȡC</body></html>"
		elif id == State.CREATED :
			req = player.getQuestState("53_LinnaeusSpecialBait")
			if req :
				if player.getLevel() >= 61 and req == State.COMPLETED :
					htmltext = "31577-01.htm"
				else :
					htmltext = "31577-00.htm"
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == LINNAEUS :
				if cond == 1 :
					if st.getQuestItemsCount(RED_TREASURE_BOX) :
						htmltext = "31577-03.htm"
					else :
						htmltext = "31577-03a.htm"
				else :
					htmltext = "31577-05.htm"
			elif npcId == RUKAL :
				if cond == 1 :
					htmltext = "30629-01.htm"
		return htmltext

QUEST		= Quest(30,qn,"�H�����糨���c�l")

QUEST.addStartNpc(LINNAEUS)

QUEST.addTalkId(LINNAEUS)
QUEST.addTalkId(RUKAL)
