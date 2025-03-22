# Made by Kerberos v1.0 on 2008/07/31
# this script is part of the Official L2J Datapack Project.
# Visit http://www.l2jdp.com/forum/ for more details.
# update by pmq
# High Five Part4 04-04-2011
import sys
from com.l2jserver.gameserver.ai import CtrlIntention
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jserver.gameserver.network.serverpackets import NpcSay

qn = "60_GoodWorkReward"

BYPASS = {
1:"<a action=\"bypass -h Quest 60_GoodWorkReward WL\">�ħL</a><br><a action=\"bypass -h Quest 60_GoodWorkReward GL\">�C���h</a>",
4:"<a action=\"bypass -h Quest 60_GoodWorkReward PA\">�t�M�h</a><br><a action=\"bypass -h Quest 60_GoodWorkReward DA\">���M�h</a>",
7:"<a action=\"bypass -h Quest 60_GoodWorkReward TH\">�_���y�H</a><br><a action=\"bypass -h Quest 60_GoodWorkReward HK\">�N��</a>",
11:"<a action=\"bypass -h Quest 60_GoodWorkReward SC\">�N�h</a><br><a action=\"bypass -h Quest 60_GoodWorkReward NM\">���F�k�v</a><br><a action=\"bypass -h Quest 60_GoodWorkReward WA\">�k�]</a>",
15:"<a action=\"bypass -h Quest 60_GoodWorkReward BS\">�D��</a><br><a action=\"bypass -h Quest 60_GoodWorkReward PP\">����</a>",
19:"<a action=\"bypass -h Quest 60_GoodWorkReward TK\">�t���M�h</a><br><a action=\"bypass -h Quest 60_GoodWorkReward SS\">�C�N�֤H</a>",
22:"<a action=\"bypass -h Quest 60_GoodWorkReward PW\">�j�a���</a><br><a action=\"bypass -h Quest 60_GoodWorkReward SR\">�Ȥ�C�L</a>",
26:"<a action=\"bypass -h Quest 60_GoodWorkReward SP\">�G�N�֤H</a><br><a action=\"bypass -h Quest 60_GoodWorkReward ES\">������</a>",
29:"<a action=\"bypass -h Quest 60_GoodWorkReward EE\">����</a>",
32:"<a action=\"bypass -h Quest 60_GoodWorkReward SK\">�u�Y�M�h</a><br><a action=\"bypass -h Quest 60_GoodWorkReward BD\">�C�b�R��</a>",
35:"<a action=\"bypass -h Quest 60_GoodWorkReward AW\">�`�W���</a><br><a action=\"bypass -h Quest 60_GoodWorkReward PR\">��v�C�L</a>",
39:"<a action=\"bypass -h Quest 60_GoodWorkReward SH\">�g�G�N�h</a><br><a action=\"bypass -h Quest 60_GoodWorkReward PS\">��v�l��h</a>",
42:"<a action=\"bypass -h Quest 60_GoodWorkReward SE\">�u�Y����</a>",
45:"<a action=\"bypass -h Quest 60_GoodWorkReward DT\">�}�a��</a>",
47:"<a action=\"bypass -h Quest 60_GoodWorkReward TR\">�ɧg</a>",
50:"<a action=\"bypass -h Quest 60_GoodWorkReward OL\">�Q�D</a><br><a action=\"bypass -h Quest 60_GoodWorkReward WC\">�Ԩg</a>",
54:"<a action=\"bypass -h Quest 60_GoodWorkReward BH\">����y�H</a>",
56:"<a action=\"bypass -h Quest 60_GoodWorkReward WS\">�Ԫ��u�K</a>"
}

CLASSES = {
"AW":[36,[2673,3172,2809]],
"BD":[34,[2627,3172,2762]],
"BH":[55,[2809,3119,3238]],
"BS":[16,[2721,2734,2820]],
"DA":[6,[2633,2734,3307]],
"DT":[46,[2627,3203,3276]],
"EE":[30,[2721,3140,2820]],
"ES":[28,[2674,3140,3336]],
"GL":[2,[2627,2734,2762]],
"HK":[9,[2673,2734,3293]],
"NM":[13,[2674,2734,3307]],
"OL":[51,[2721,3203,3390]],
"PA":[5,[2633,2734,2820]],
"PP":[17,[2721,2734,2821]],
"PR":[37,[2673,3172,3293]],
"PS":[41,[2674,3172,3336]],
"PW":[23,[2673,3140,2809]],
"SC":[12,[2674,2734,2840]],
"SE":[43,[2721,3172,2821]],
"SH":[40,[2674,3172,2840]],
"SK":[33,[2633,3172,3307]],
"SP":[27,[2674,3140,2840]],
"SR":[24,[2673,3140,3293]],
"SS":[21,[2627,3140,2762]],
"TH":[8,[2673,2734,2809]],
"TK":[20,[2633,3140,2820]],
"TR":[48,[2627,3203,2762]],
"WA":[14,[2674,2734,3336]],
"WC":[52,[2721,3203,2879]],
"WL":[3,[2627,2734,3276]],
"WS":[57,[2867,3119,3238]]
}

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [10867,10868]
		self.isNpcSpawned = 0

	def onAdvEvent (self,event,npc,player) :
		if event == "npc_cleanup" :
			self.isNpcSpawned = 0
			npc.broadcastPacket(NpcSay(27340,0,npc.getNpcId(),"�A�B��u�n�A�U���ڷ|�A�ӧ�A���C"))
			return
		st = player.getQuestState(qn)
		if not st: return
		htmltext = event
		if event == "31435-03.htm" :
			st.set("cond","1")
			st.playSound("ItemSound.quest_accept")
			st.setState(State.STARTED)
		elif event == "31435-05.htm" :
			st.set("cond","4")
			st.playSound("ItemSound.quest_middle")
		elif event == "31435-08.htm" :
			st.set("cond","9")
			st.playSound("ItemSound.quest_middle")
		elif event == "32487-02.htm" and self.isNpcSpawned == 0:
			npc = st.addSpawn(27340,72590,148100,-3312,60000)
			npc.broadcastPacket(NpcSay(npc.getObjectId(),0,npc.getNpcId(),"�u" + player.getName() + "�v" + "! �h���a�A�n�ǴN�ǧA���n�_�ߡC"))
			npc.setRunning()
			npc.addDamageHate(st.getPlayer(),0,999)
			npc.getAI().setIntention(CtrlIntention.AI_INTENTION_ATTACK, st.getPlayer())
			self.isNpcSpawned = 1
			self.startQuestTimer("npc_cleanup",59000,npc, None)
		elif event == "32487-06.htm" :
			st.set("cond","8")
			st.playSound("ItemSound.quest_middle")
			st.takeItems(10868,-1)
		elif event == "30081-03.htm" :
			st.set("cond","5")
			st.playSound("ItemSound.quest_middle")
			st.takeItems(10867,-1)
		elif event == "30081-05.htm" :
			st.set("cond","6")
			st.playSound("ItemSound.quest_middle")
		elif event == "30081-08.htm" :
			if st.getQuestItemsCount(57) >= 3000000 :
				st.takeItems(57,3000000)
				st.giveItems(10868,1)
				st.set("cond","7")
				st.playSound("ItemSound.quest_middle")
			else :
				htmltext = "30081-07.htm"
		elif event == "31092-05.htm" :
			st.exitQuest(False)
			st.playSound("ItemSound.quest_finish")
			text = BYPASS[player.getClassId().getId()]
			htmltext = "<html><body>�]�I���a�U�ӤH�G<br>�����ƹ��A�A�٬O�⥦�ѤF�a...<br>�ڻ��L�|���A��¾�����I�A�Q�n��¾�����@��¾�~�O�H�D�D�ݧa...<br>"+text+"</body></html>"
		elif event == "31092-06.htm" :
			text = BYPASS[player.getClassId().getId()]
			htmltext = "<html><body>�]�I���a�U�ӤH�G<br>�p�G�Ҽ{�n�F�A���N���ֿ�ܤ@�U�a�C�A�Q�n���@��¾�~�O�H<br>"+text+"</body></html>"
		elif event in CLASSES.keys():
			newclass,req_item=CLASSES[event]
			adena = 0
			for i in req_item :
				if not st.getQuestItemsCount(i):
					st.giveItems(i,1)
				else :
					adena = adena + 1
			if adena == 3 :
				return "31092-06.htm"
			if adena > 0 :
				st.giveAdena(adena*1000000,True)
			htmltext = "31092-05.htm"
			st.set("onlyone","1")
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			if npcId == 31435 :
				htmltext = "<html><body>�o�O�w�g���������ȡC</body></html>"
			elif npcId == 31092 :
				if player.getClassId().level() == 1 and not st.getInt("onlyone"):
					htmltext = "31092-04.htm"
				else:
					htmltext = "31092-07.htm"
		elif id == State.CREATED :
			if npcId == 31435 and cond == 0 :
				if player.getLevel() < 39 or player.getClassId().level() != 1 or player.getRace().ordinal() == 5 :
					htmltext = "31435-00.htm"
					st.exitQuest(1)
				else :
					htmltext = "31435-01.htm"
		elif id == State.STARTED:
			if npcId == 31435 :
				if cond in [1,2]:
					htmltext = "31435-03a.htm"
				elif cond == 3 :
					htmltext = "31435-04.htm"
				elif cond == 4 :
					htmltext = "31435-06.htm"
				elif cond in [5,6,7] :
					htmltext = "31435-06a.htm"
				elif cond == 8 :
					htmltext = "31435-07.htm"
				elif cond == 9 :
					htmltext = "31435-09.htm"
					st.set("cond","10")
					st.playSound("ItemSound.quest_middle")
				elif cond == 10 :
					htmltext = "31435-10.htm"
			elif npcId == 32487 :
				if cond == 1 :
					if self.isNpcSpawned == 0 :
						htmltext = "32487-01.htm"
					else:
						htmltext = "<html><body>���J�G<br>�᭱..�p�߫᭱�C</body></html>"
				elif cond == 2 :
					htmltext = "32487-03.htm"
					st.set("cond","3")
					st.playSound("ItemSound.quest_middle")
				elif cond == 3 :
					htmltext = "32487-04.htm"
				elif cond == 7 :
					htmltext = "32487-05.htm"
				elif cond == 8 :
					htmltext = "32487-06.htm"
			elif npcId == 30081 :
				if cond == 4 :
					htmltext = "30081-01.htm"
				elif cond == 5 :
					htmltext = "30081-04.htm"
				elif cond == 6 :
					htmltext = "30081-06.htm"
				elif cond == 7 :
					htmltext = "30081-09.htm"
			elif npcId == 31092 :
				if cond == 10 :
					if player.getClassId().level() == 1 :
						htmltext = "31092-01.htm"
					else:
						htmltext = "31092-06.htm"
						st.exitQuest(False)
						st.playSound("ItemSound.quest_finish")
						st.giveAdena(3000000, False)
						st.set("onlyone","1")
		return htmltext

	def onKill(self,npc,player,isPet):
		self.cancelQuestTimer("npc_cleanup", npc, None)
		self.isNpcSpawned = 0
		st = player.getQuestState(qn)
		if not st : return
		if st.getState() != State.STARTED : return
		npcId = npc.getNpcId()
		cond = st.getInt("cond")
		if npcId == 27340 and cond == 1 :
			string = "�S�Q��|�o��j�A�ڥ���F�C"
			npc.broadcastPacket(NpcSay(npc.getObjectId(),0,npc.getNpcId(),string))
			st.giveItems(10867,1)
			st.set("cond","2")
			st.playSound("ItemSound.quest_middle")
		return

QUEST		= Quest(60,qn,"���檺����")

QUEST.addStartNpc(31092)
QUEST.addStartNpc(31435)

QUEST.addTalkId(30081)
QUEST.addTalkId(31092)
QUEST.addTalkId(31435)
QUEST.addTalkId(32487)

QUEST.addKillId(27340)