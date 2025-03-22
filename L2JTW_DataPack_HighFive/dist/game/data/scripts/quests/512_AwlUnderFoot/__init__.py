# Update by pmq 28-08-2010

import sys
from java.lang                                      import System
from com.l2jserver                                  import Config
from com.l2jserver.gameserver                       import ThreadPoolManager
from com.l2jserver.gameserver.datatables            import NpcTable
from com.l2jserver.gameserver.datatables            import SpawnTable
from com.l2jserver.gameserver.instancemanager       import FortManager
from com.l2jserver.gameserver.instancemanager       import InstanceManager
from com.l2jserver.gameserver.model.actor.instance  import L2PcInstance
from com.l2jserver.gameserver.model.entity          import Fort
from com.l2jserver.gameserver.model.entity          import Instance
from com.l2jserver.gameserver.model.quest           import State
from com.l2jserver.gameserver.model.quest           import QuestState
from com.l2jserver.gameserver.model.quest.jython    import QuestJython as JQuest
from com.l2jserver.gameserver.network               import SystemMessageId
from com.l2jserver.gameserver.network.serverpackets import SystemMessage
from com.l2jserver.gameserver.util                  import Util
from com.l2jserver.util                             import Rnd

qn = "512_AwlUnderFoot"

QuestId = 512
QuestName = "AwlUnderFoot"
QuestDesc = "Access Castle Dungeon"

#NPC
WARDEN = [ 36403, 36404, 36405, 36406, 36407, 36408, 36409, 36410, 36411 ]

#MONSTER TO KILL -- Only last 3 Raids (lvl ordered) from 162, drop DL_MARK
RAIDS1 = [ 25546, 25549, 25552 ]
RAIDS2 = [ 25553, 25554, 25557, 25560 ]
RAIDS3 = [ 25563, 25566, 25569 ]

#QUEST ITEMS
DL_MARK = 9798

#REWARDS
KNIGHT_EPALUETTE = 9912

#MESSAGES
warden_exchange = "<html><body>�ʺ��޲z���G<br>�A�w�g�B�z���a�U�ʺ��}�ǤF�ܡH�F�o�n�I<br>���±z�����U�A�Ѱ��F��ڭ̪��¯١C<br>�o�̬O�M�h���ӳ����ӿաC<br>�A�i�H�V�c���]�k�v�洫��������ɵ��~�C<br>...<br>�z�Q�~��D�ԶܡH<br><br><a action=\"bypass -h Quest 512_AwlUnderFoot continue\">���Q�~��</a><br><a action=\"bypass -h Quest 512_AwlUnderFoot quit\">�ڭn���</a></body></html>"
quest_no = "<html><body>�ʺ��޲z���G<br><center><font color=\"FF0000\">�]�\��|����ˡI�^</font></center></body></html>"
warden_no = "<html><body>�ʺ��޲z���G<br>���z���ǳƤ@�U�A�^�ӮɡA�Шӧ�ڧa...</body></html>"
rumor = "<html><body>�ʺ��޲z���G<br>��t��ԥd���M�O�ڪ������A���]�|�v�T�{��ͬ��C���{�b�o�ˡA�V�O���O�ɶ��A�x�b��ԥd��4�W�լd���V�|�B��M�I�C�бz���I�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot quest_no\">�бN�ڰe�쨺�Ӧa��</a></body></html>"
warden_ask = "<html><body>�ʺ��޲z���G<br>�@...<br>�]�����[����Q��m���t�G�A�L�h�Q�}�T���Ǫ�-�a�U�ʺ����}��-�̡A�ثe�U�ۧΦ��դO�C<br>�b�a�U���ʺ����A�Ǫ��̨ϥΥu���L�̯������B���ʪ����K�q�D�A�ӳo�ǯ��K�q�D�p�j����몺����s���C<br>��ť���o�ǳq�D�]�P�a�W�Ǫ��̴x�����a�ϳs���b�@�_�O�C<br>�p���x���n��a�U�@�ɤ��D���v���դO��´�A�O�ѹL�h�Q�}�T���Ǫ��̩Ҳզ����A�ӥB�٦s�b�۩w�����šFť�������a�U�ϰ�O�ѧ󰪦a�쪺�]���̴x�����A�ӭn��a�U�h�Ѹ��C�a�쪺�]���̦���C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_ask1\">���ҥH�a�U�ʺ����Ǫ��̤��_�X�S�A�N��A��򩺰Q...</a></body></html>"
warden_ask1 = "<html><body>�ʺ��޲z���G<br>�S���C<br>�ҥH�ڭ̤~�|�V������_�I�a�̨D�U...<br>��M�Ať������¾�쪺�Բ��a�P�Ǫ̡B�]�k�v�̡A���b�M�D�i�ä[�ʸѨM�o���D����k�C<br>���O�]���դO�U��������������O���F���D�A�ҥH�i�檺���Ӷ��Q�C<br>�`���A�b�ѨM��ץX�Ӥ��e�A�u�n�~��h���Q�F�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_ask2\">�ڸӰ��Ǥ���O�H</a></body></html>"
warden_ask2 = "<html><body>�ʺ��޲z���G<br>�L�h�b�o�a�U�ʺ����]���̩M���Q���������A�����L�j�W�Ҫ��԰��C<br>�u�O���E�P���԰�...<br>���賣���˺G���C<br>�ҥH�P�쮣�ߪ��]���̤]�����������N���a�U�ʺ����ۮa�몺�i�X�F�C<br>���L��ӫ��a�U�ʺ������򦳬y�J���O�L�h�}�Ǫ��j���]���A�H�T�H�ղզ����@�s���a�U�ʺ��ڸs�C<br>�������t�ѡA���@�w�O�b�d���򳱿ѧa�C<br>�N�·Ы_�I�a�z�N<font color=\"LEVEL\">�T�H��</font>�����h��A���˲զ��a�U�ʺ��}�Ǳڸs���Ҧ��]���a�C<br>�N�̫�@�ժ�����Ǫ�������a�^<font color=\"LEVEL\">���a�U�ʺ��]�������ų��H��</font>���ܡA�ڴN��I�M�h�ӳ����z�C<br>�Q���M�h�ӳ��i�H�V�c���]�k�v�洫��������ɵ��~�C<br>��F�A�٦�...<br>��ثe����o����i���a�U�ʺ��}�ǭ��⦳<font color=\"LEVEL\">�������`�����C�B�ʳ����n�e�B�}�a�̥[��</font>�C<br>�i�z�L�ڶi�J���a�U�ʺ��C<br>���N���U�z�F�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot status\">�߰ݫ����a�U�ʺ����p</a></body></html>"
CastleWarden = "<html><body>�ʺ��޲z���G<br><br>�o�̬O�M�I���a�C�Y�S���Q�n�ܱo��j���N�ӡA�ЧO�b�o����r�d�C<br><br><a action=\"bypass -h Quest 512_AwlUnderFoot rumor\">��ť�즳����t��ԥd������</a><br><a action=\"bypass -h Quest 512_AwlUnderFoot enter\">���ڶi�J�ʺ��a</a><br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_quest.htm\">����</a></body></html>"
default = "<html><body>�ʺ��޲z���G<br>�ثe�S��������ȡA�α��󤣲šC</body></html>"
nolvl = "<html><body>�ʺ��޲z���G<br>�ګܷP�«_�I�a�z�Q�n��U���߷N�A���ڤ]�O�����n�몺�@���A�i���Ʊ�����O���Ū�����������J�I�ҡC<br>�p���������޲z�d���]�O�ڪ�¾�ȡC<br>�b�����o¾�Ȥ��e�A�ڤ]���O�ӥw�\�������_�I�a�C<br�H�e�����߳��ӬݡA�_�I�a�z����O�٤����������Q���ȡC<br>�h�i�m��O��A�ӧ�ڧa�C<br>(�u������70�H�W�~�i�H���檺���ȡC)</body></html>"
noitem = "<html><body>�ʺ��޲z���G<br>�A�w�g�^�ӶܡH<br1>�A������F�ڪ��n�D�C�A�S���a�U�ʺ��]�������ų��H���C</body></html>"
wrongcastle = "<html><body>�ʺ��޲z���G<br>(�֦����������������������~����檺���ȡC)</body></html>"
noclan = "<html><body>�ʺ��޲z���G<br>�A�O�֡H�n�����b����������W�椺...<br>(�֦����������������������~����檺���ȡC)</body></html>"
finish = "<html><body>�ʺ��޲z���G<br>�ڡA�ک��աC�G�M�A�ڨS���ݿ��H...<br>���§A���o�̰����@���C<br>�p�G�A�Q�A�����X���⪺�ܡA�ڭ̷|�D�`�P�E�C<br>���A�ȳ~�r�֡I</body></html>"
noparty = "<html><body>�i�J�ʺ�������O�A���զ�2�W�H�W������A�ӥB�Ҧ�������������b�i����Ȥ~��C�٦��A�}�l�V�m��A�ܤ֦b4�p�ɤ����L�k�W�[�B�~���V�m�C</body></html>"
#noleader = "<html><body>�ʺ��޲z���G<br>���F�b�԰����ͦs�A�̭��n���O��������p���ɦۤv������A��M�A�b��ԥd���N��ɱz���H�A�]�|�O�����C�ҥH�A�ګD�`�L�������ɤH���C�z�������O" + str(pln) + "�A�h�N�z�������Шӳo��a�C<br>(�u�������~��չ϶i�J�C)</body></html>"
warden_quest = "<html><body>�ʺ��޲z���G<br>�ڬO�o�ӫ������a�U�ʺ��޲z���C�o�Ӧa�U�ʺ��Ǫ��}��̪�Q�o�{���C<br>�ڪ��D��L�����]���o�˪��a�U�ʺ��C�ڪ��d���O�n�O���o�Ӧa�U�ʺ��Ϧw���C<br>�����A�o�N�X�G�O�i�����Ǫ��X�{�M�����b�a�c���@�y�����A���O�ܡH<br>�������O�A�ڭ̮ڥ��L�k��W�B�z�o�Ӥu�@�C<br>�ڭ̻ݭn�_�I�a�����U�C<br>��M�A�ڭ̷|��I���z�S�ҡC<br><br><a action=\"bypass -h Quest 512_AwlUnderFoot start\">�ڷ|���A��</a><br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_no\">�ڤ��O�{�b</a></body></html>"
warden_yes = "<html><body>�ʺ��޲z���G<br>�i�J���a�U�ʺ���A�N�a�U�ʺ��}�����h�a�C<br>�_�I�a�z�����n�N<font color=\"LEVEL\">�T�H��</font>�����h��A���˲զ��a�U�ʨƥ}�Ǳڸs���Ҧ��]���~��C<br>�N�̫�@�ժ�����Ǫ�������A�a�^���a�U�ʺ��]�������ų��H�����ܡA�ڴN��I�M�h�ӳ����z�C<br>�Q���M�h�ӳ��i�H�V�c���]�k�v�洫��������ɵ��~�C<br>��F�A�٦�...<br>��ثe����o����i���a�U�ʺ��}�ǭ��⦳<font color=\"LEVEL\">�������`�����C�B�ʳ����n�e�B�}�a�̥[��</font>�C<br>�i�z�L�ڶi�J���a�U�ʺ��C<br>���N���U�z�F�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot enter\">���D�F�A�{�b�N�X�o</a><br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_ask\">�a�U�ʺ����Ǫ��̬O��诫�t�H</a></body></html>"

class PyObject:
	pass

def Reward(st) :
	if st.getState() == State.STARTED :
		if st.getRandom(9) > 5 : #No retail info about drop quantity. Guesed 1-2. 60% for 1 and 40% for 2 
			st.giveItems(DL_MARK, int(2 * Config.RATE_QUEST_DROP))
			st.playSound("ItemSound.quest_itemget")
		elif st.getRandom(9) < 6  :
			st.giveItems(DL_MARK, int(1 * Config.RATE_QUEST_DROP))
			st.playSound("ItemSound.quest_itemget") 

def checkConditions(player, new):
	party = player.getParty()
	if not party:
		player.sendPacket(SystemMessage(SystemMessageId.NOT_IN_PARTY_CANT_ENTER))
		return False
	for partyMember in party.getPartyMembers().toArray():
		if not partyMember.getLevel() >= 70:
			player.sendPacket(SystemMessage(SystemMessageId.PARTY_EXCEEDED_THE_LIMIT_CANT_ENTER))
			return False
		if not partyMember.isInsideRadius(player, 1000, False, False):
			sm = SystemMessage(SystemMessageId.C1_IS_IN_LOCATION_THAT_CANNOT_BE_ENTERED)
			sm.addCharName(partyMember)
			player.sendPacket(sm)
			return False
	return True

def teleportplayer(self, player, teleto):
	player.setInstanceId(teleto.instanceId)
	player.teleToLocation(teleto.x, teleto.y, teleto.z)
	pet = player.getPet()
	if pet != None :
		pet.setInstanceId(teleto.instanceId)
		pet.teleToLocation(teleto.x, teleto.y, teleto.z)
	return

def enterInstance(self, player, template, teleto):
	instanceId = 0
	if not checkEnter(self, player) :
		return 0
	party = player.getParty()
	#check for other instances of party members
	if party :
		for partyMember in party.getPartyMembers().toArray():
			st = partyMember.getQuestState(qn)
			if st :
				id = st.getState()
				if not id == State.STARTED :
					player.sendPacket(SystemMessage.sendString(partyMember.getName() + "������S���i����ȡC"))
					return 0
			else :
				player.sendPacket(SystemMessage.sendString(partyMember.getName() + "������S���i����ȡC"))
				return 0
			if partyMember.getInstanceId() != 0:
				instanceId = partyMember.getInstanceId()
				if debug: print "Rim Pailaka: found party member in instance:" + str(instanceId)
		else :
			if player.getInstanceId() != 0:
				instanceId = player.getInstanceId()
	#exising instance
	if instanceId != 0:
		if not checkConditions(player, False):
			return 0
		foundworld = False
		for worldid in self.world_ids:
			if worldid == instanceId:
				foundworld = True
		if not foundworld:
			player.sendPacket(SystemMessage.sendString("�A�������w�i�J�䥦���Y�ɦa�ϡC"))
			return 0
		teleto.instanceId = instanceId
		teleportplayer(self, player, teleto)
		return instanceId
	#new instance
	else:
		if not checkConditions(player, True):
			return 0
		instanceId = InstanceManager.getInstance().createDynamicInstance(template)
		if not instanceId in self.world_ids:
			world = PyObject()
			world.rewarded = []
			world.instanceId = instanceId
			self.worlds[instanceId] = world
			self.world_ids.append(instanceId)
			self.currentWorld = instanceId
			print "Rim Pailaka: started. " + template + " Instance: " + str(instanceId) + " created by player: " + str(player.getName())
			self.saveGlobalQuestVar("512_NextEnter", str(System.currentTimeMillis() + 14400000))
			raidid = 1
			spawnRaid(self, world, raidid)
		#teleports player
		teleto.instanceId = instanceId
		for partyMember in party.getPartyMembers().toArray():
			st = partyMember.getQuestState(qn)
			st.set("cond", "1")
			playerName = partyMember.getName()
			teleportplayer(self, partyMember, teleto)
		return instanceId
	return instanceId

def exitInstance(self, npc) :
	if self.worlds.has_key(npc.getInstanceId()):
		world = self.worlds[npc.getInstanceId()]
		instanceObj = InstanceManager.getInstance().getInstance(self.currentWorld)
		instanceObj.setDuration(60000)
		instanceObj.removeNpcs()

def spawnRaid(self, world, raid) :
	if raid == 1 :
		spawnid = RAIDS1[Rnd.get(0, 2)]
	elif raid == 2 :
		spawnid = RAIDS2[Rnd.get(0, 3)]
	elif raid == 3 :
		spawnid = RAIDS3[Rnd.get(0, 2)]
	spawnedNpc = self.addSpawn(spawnid, 12161, -49144, -3000, 0, False, 0, False, world.instanceId)

def checkEnter(self, player) :
	entertime = self.loadGlobalQuestVar("512_NextEnter")
	if entertime.isdigit() :
		remain = long(entertime) - System.currentTimeMillis()
		if remain <= 0 :
			return True
		else :
			timeleft = remain / 60000
			player.sendPacket(SystemMessage.sendString("�q�{�b�_�N�|����i�J�Y�ɦa�ϡG�u�����a�U�ʺ��v�C�U�@�����i���ɶ��ٳ�" + str(timeleft) + "�����C"))
			return False
	else :
		return True

def checkLeader(player) :
	party = player.getParty()
	if not party:
		player.sendPacket(SystemMessage(SystemMessageId.NOT_IN_PARTY_CANT_ENTER))
		return False
	elif not player.getParty().isLeader(player):
		player.sendPacket(SystemMessage(SystemMessageId.ONLY_PARTY_LEADER_CAN_ENTER))
		return False
	else :
		return True

class Quest (JQuest) :
	def __init__(self, id, name, descr):
		JQuest.__init__(self, id, name, descr)
		self.questItemIds = [DL_MARK]
		self.worlds = {}
		self.world_ids = []
		self.currentWorld = 0

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return
		if event == "start" :
			htmltext = warden_yes
			st.set("cond", "1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "quit" :
			htmltext = finish
			st.playSound("ItemSound.quest_finish")
			st.exitQuest(1)
		elif event == "continue" :
			htmltext = warden_yes
		elif event == "warden_no" :
			st.set("cond", "0")
			htmltext = warden_no
		elif event == "default" :
			htmltext = default
		elif event == "warden_yes" :
			htmltext = warden_yes
		elif event == "warden_ask" :
			htmltext = warden_ask
		elif event == "warden_ask1" :
			htmltext = warden_ask1
		elif event == "warden_ask2" :
			htmltext = warden_ask2
		elif event == "rumor" :
			htmltext = rumor
		elif event == "quest_no" :
			htmltext = quest_no
		elif event == "leave" :
			htmltext = ""
			if checkLeader(player) :
				exitInstance(self, npc)
				htmltext = "Instance deleted!"
		elif event == "status" :
			entertime = self.loadGlobalQuestVar("512_NextEnter")
			if entertime.isdigit() :
				remain = long(entertime) - System.currentTimeMillis()
				if remain <= 0 :
					htmltext = "<html><body>�ʺ��޲z���G<br>�a�U�ʺ����m���A�A�{�b�i�H�i�J�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_yes\">��^</a></body></html>"
				else :
					timeleft = remain / 60000
					if timeleft > 180 :
						htmltext = "<html><body>�ʺ��޲z���G<br>�a�U�ʺ��{�b���H�D�Ԥ��C�ݥL�����}�ɡA�M��A�դ@���C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_yes\">��^</a></body></html>"
					else :
						htmltext = "<html><body>�ʺ��޲z���G<br>�q�{�b�_�N�|����i�J�Y�ɦa�ϡG�u�����a�U�ʺ��v�C�U�@�����i���ɶ��ٳ� <font color=\"LEVEL\">" + str(timeleft) + "</font> �����C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_yes\">��^</a></body></html>"
			else :
				htmltext = "<html><body>�ʺ��޲z���G<br>�a�U�ʺ����m���A�A�{�b�i�H�i�J�C<br><a action=\"bypass -h Quest 512_AwlUnderFoot warden_yes\">��^</a></body></html>"
		elif event == "enter" :
			party = player.getParty()
			if not party:
				htmltext = noparty
			elif not player.getParty().isLeader(player):
				pln = player.getParty().getLeader().getName()
				htmltext = "<html><body>�ʺ��޲z���G<br>���F�b�԰����ͦs�A�̭��n���O��������p���ɦۤv������A��M�A�b��ԥd���N��ɱz���H�A�]�|�O�����C�ҥH�A�ګD�`�L�������ɤH���C�z�������O" + str(pln) + "�A�h�N�z�������Шӳo��a�C<br>(�u�������~��չ϶i�J�C)</body></html>"
			else :
				tele = PyObject()
				tele.x = 11740
				tele.y = -49148
				tele.z = -3000
				enterInstance(self, player, "RimPailakaCastle.xml", tele)
				htmltext = ""
		return htmltext

	def onTalk (self, npc, player):
		htmltext = default
		st = player.getQuestState(qn)
		if not st : return htmltext
	
		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		CASTLEID = npc.getCastle().getOwnerId()
		CLAN = player.getClan()

		if id == State.CREATED :
			if npcId in WARDEN and cond == 0 :
				if CLAN :
					CLANID = CLAN.getClanId()
				else :
					htmltext = noclan
					return htmltext
				if not CASTLEID == CLANID :
					htmltext = wrongcastle
					return htmltext
				if st :
					if player.getLevel() >= 70 :
						htmltext = warden_quest
					else :
						htmltext = nolvl
						st.exitQuest(1)
		elif id == State.STARTED :
			if npcId in WARDEN :
				if cond == 1 :
					count = st.getQuestItemsCount(DL_MARK)
					if count > 0 :
						htmltext = warden_exchange
						st.takeItems(DL_MARK, count)
						st.giveItems(KNIGHT_EPALUETTE, count * 162)
					elif count == 0 :
						htmltext = warden_yes
		return htmltext

	def onKill(self, npc, player, isPet) :
		npcId = npc.getNpcId()
		partyMembers = [player]
		party = player.getParty()
		if npc.getInstanceId() in self.worlds:
			world = self.worlds[npc.getInstanceId()]
		if npcId in RAIDS3 :
			#If is party, give item to all party member who have quest
			if party :
				partyMembers = party.getPartyMembers().toArray()
				for player in partyMembers :
					st = player.getQuestState(qn)
					if st :
						Reward(st)
			else :
				st = player.getQuestState(qn)
				if st :
					Reward(st)
			if self.worlds.has_key(npc.getInstanceId()):
				world = self.worlds[npc.getInstanceId()]
				instanceObj = InstanceManager.getInstance().getInstance(self.currentWorld)
				instanceObj.setDuration(60000)
				instanceObj.removeNpcs()
		elif npcId in RAIDS1 :
			spawnRaid(self, world, 2)
		elif npcId in RAIDS2 :
			spawnRaid(self, world, 3)
		return

	def onFirstTalk(self, npc, player) :
		st = player.getQuestState(qn)
		if not st :
			st = self.newQuestState(player)
		npcId = npc.getNpcId()
		if npcId in WARDEN :
			htmltext = "CastleWarden.htm"
		return htmltext

# Quest class and state definition
QUEST = Quest(QuestId, str(QuestId) + "_" + QuestName, QuestDesc)

for npcId in WARDEN :
	QUEST.addStartNpc(npcId)
	QUEST.addTalkId(npcId)
	QUEST.addFirstTalkId(npcId)

for mobId in RAIDS1 :
	QUEST.addKillId(mobId)
for mobId in RAIDS2 :
	QUEST.addKillId(mobId)
for mobId in RAIDS3 :
	QUEST.addKillId(mobId)