# Made by Hawkin
# update by pmq
# High Five 20-02-2011
import sys
from com.l2jserver import Config
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "629_CleanUpTheSwampOfScreams"

#NPC
CAPTAIN = 31553 # 傭兵隊長 比斯
#ITEMS
CLAWS   = 7250  # 司塔卡拓之爪
COIN    = 7251  # 黃金羊的銅幣
RECRUIT = 7246  # 黃金羊的標誌-新兵
SOLDIER = 7247  # 黃金羊的標誌-精銳兵

#CHANCES
MAX=1000
CHANCE={
    21508:500,
    21509:431,
    21510:521,
    21511:576,
    21512:746,
    21513:530,
    21514:538,
    21515:545,
    21516:553,
    21517:560
}

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [CLAWS]

	def onAdvEvent (self,event,npc,player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		if event == "31553-1.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "31553-3.htm" :
			if st.getQuestItemsCount(CLAWS) >= 100 :
				st.takeItems(CLAWS,100)
				st.giveItems(COIN,20)
			else :
				htmltext = "31553-3a.htm"
		elif event == "31553-5.htm" :
			st.playSound("ItemSound.quest_finish")
			st.exitQuest(1)
		return htmltext

	def onTalk(self, npc, player) :
		htmltext = "<html><body>目前沒有執行任務，或條件不符。</body></html>"
		st = player.getQuestState(qn)
		if not st :return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.CREATED :
			if npcId == CAPTAIN and cond == 0 :
				if player.getLevel() >= 66 :
					htmltext = "31553-0.htm"
				else:
					htmltext = "31553-0a.htm"
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == CAPTAIN :
				if cond == 1 :
					if st.getQuestItemsCount(CLAWS) >= 100 :
						htmltext = "31553-2.htm"
					else :
						htmltext = "31553-1a.htm"
		return htmltext

	def onFirstTalk(self, npc, player) :
		st = player.getQuestState(qn)
		if not st :
			st = self.newQuestState(player)

		npcId = npc.getNpcId()
		cond = st.getInt("cond")

		if npcId == CAPTAIN :
			if (st.getQuestItemsCount(RECRUIT) or st.getQuestItemsCount(SOLDIER)):
				return "31553-c1.htm"
		player.setLastQuestNpcObject(npc.getObjectId())
		npc.showChatWindow(player)
		return None

	def onKill(self,npc,player,isPet):
		partyMember = self.getRandomPartyMemberState(player, State.STARTED)
		if not partyMember : return
		st = partyMember.getQuestState(qn)
		if st :
			if st.getState() == State.STARTED :
				prevItems = st.getQuestItemsCount(CLAWS)
				random = self.getRandom(MAX)
				chance = CHANCE[npc.getNpcId()]*Config.RATE_QUEST_DROP
				numItems, chance = divmod(chance,MAX)
				if random < chance :
					numItems += 1
				st.giveItems(CLAWS,int(numItems))
				if int(prevItems+numItems)/100 > int(prevItems)/100 :
					st.playSound("ItemSound.quest_middle")
				else:
					st.playSound("ItemSound.quest_itemget")
		return

QUEST		= Quest(629,qn,"掃蕩悲鳴的沼澤")

QUEST.addStartNpc(CAPTAIN)
QUEST.addFirstTalkId(CAPTAIN)
QUEST.addTalkId(CAPTAIN)

for mobs in range(21508,21518) :
	QUEST.addKillId(mobs)