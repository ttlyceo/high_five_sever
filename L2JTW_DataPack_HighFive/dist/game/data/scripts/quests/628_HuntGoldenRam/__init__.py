# Hunt of the Golden Ram Mercenary Force
# Made by Polo - Have fun!..... fix & addition by t0rm3nt0r and LEX
# update by pmq
# High Five 20-02-2011
import sys
from com.l2jserver import Config 
from com.l2jserver.gameserver.datatables import SkillTable
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "628_HuntGoldenRam"

# �ħL �d�i��
# 31554-c1.htm
#kahman_c1 = "<html><body>�ħL�d�i���G<br>�ڭ̬O�����϶ħL�ΡI���g�M������S�@�_�b�ƺC���𥴹L�M�I�ڪ��S�̡A�d�i�����B�����|�[�A�����@�W�Ԥh�b���̭ˤU�C�����F��{�b�@�w�b����߼ڪ����K�U�N�ۡC<br>���g�|���a���了�`���S�����W�A����ڤ��b�԰��C�A�Q���Q��aģ�������ϧ̥S�A�M�ڭ̤@�_�԰��ڡH<br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31554-c2.htm
#kahman_c2 = "<html><body>�ħL�d�i���G<br>�@�A�A�ӰաI�A�A���\�����Ϥ��W�ߤF�u�q���ԪG�C���d�i���u�ߨتA�A�����ơI<br>��o��h�A�a�a���Ҧ��Τl���N�������@�Ѭ���A�Ʊ�A�~��[�o�I<br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31554-04.htm
kahman_04 = "<html><body>�ħL�d�i���G<br>�쩳�b�F����I�Y�Q�������a�������϶ħL�Τ��������ܡA�N�o�h�d�㪺�h�A�y���䥬�L�S�q��d�ݫ�A����<font color=\"LEVEL\">100�ӫ䥬�L�S�q��d�ݪ��Ҵ�</font>�~��I�h�a�A�h�L�ڡI</body></html>"
# 31554-05.htm
kahman_05 = "<html><body>�ħL�d�i���G<br>�^�ӰաA�h�L�ڡI��A�����q��d�ݪ��Q��F�ܡH�S����O���H�O���藍�ন�������϶ħL�Ϊ��S�̪��I<br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_06\">�N100�ӫ䥬�L�S�q��d�ݪ��Ҵߥ浹�L</a></body></html>"
# 31554-06.htm
kahman_06 = "<html><body>�ħL�d�i���G<br>���W�F�A�h�L�ڡI�Y�O�A�A�N�����������϶ħL�Τ��S�̪��R�����I<br>�n�A���h�o<font color=\"LEVEL\">�����Ϫ��лx - �s�L</font>�a�I�q�{�b�_�A�A�N�O�ڭ̶����϶ħL�Ϊ��S�̤F�C���ߧA�I<br>���L�h�L�ڡA�Y�Q������U�L���ܡA�n�ܪ���j�~��I�i�h�d�㪺�h�A�Q��䥬�L�S�q��d�ݻP���h�q��d�ݫ�A��������<font color=\"LEVEL\">""100""�ӫ䥬�L�S�q��d�ݪ��Ҵ߻P100�ӥ��h�q��d�ݫ᪺�Ҵ�</font>�~��I<br>�s�o�ص{�ת����Ȥ]���৹�����ܡA�N���t������U�L�I<br></body></html>"
# 31554-07.htm
kahman_07 = "<html><body>�ħL�d�i���G<br>�Q���������Ϫ���U�L���ܡA�n�ܪ���j�~��I�i�h�d�㪺�h�A�Q��䥬�L�S�q��d�ݻP���h�q��d�ݫ�A��������<font color=\"LEVEL\">100�ӫ䥬�L�S�q��d�ݪ��Ҵ߻P100�ӥ��h�q��d�ݫ᪺�Ҵ�</font>�~��I<br>�s�o�ص{�ת����Ȥ]���৹�����ܡA�N���t������U�L�I<br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_08\">�u�{�b�n�W�Գ��I�v</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_09\">�u����U�L������A�ðh�X�����϶ħL�ΡC�v</a></body></html>"
# 31554-08.htm
kahman_08 = "<html><body>�ħL�d�i���G<br>�N�O�o�غ믫�I��Ĥ襴�˧a�A���˧a�I�H�����Ϥ��W���W�߸U�a�I</body></html>"
# 31554-09.htm
kahman_09 = "<html><body>�ħL�d�i���G<br>�n�������a�������϶ħL�Τ@���A���O����²�檺�Ʊ��I�Y�{�b��󪺸ܡA�A�H��֩w�|�ᮬ�I�]�i��n���s�ѥ[�J�ΦҸաI�Y�ϳo�ˤ]�Q�n�h�X�ڭ̪��ħL�ζܡH<br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_10\">�T�w�n�h�X</a></body></html>"
# 31554-10.htm
kahman_10 = "<html><body>�ħL�d�i���G<br>����u���C</body></html>"
# 31554-11.htm
kahman_11 = "<html><body>�ħL�d�i���G<br>�u�F���_�I�G�M�O���g�ʾԪ��i�h�I�Y�O�A�A�N���Q���㦳���������϶ħL�κ�U�����I<br>�n�A���h�o<font color=\"LEVEL\">�����Ϫ��лx - ��U�L</font>�a�I���ߧA�A�ԤͰڡI</body></html>"
# 31554-12.htm
kahman_12 = "<html><body>�ħL�d�i���G<br>�ԤͰڡA�b�A������ȮɭY�ݭn�������ܡA�N�h����ȧL���R�R�P�ɵ��L�Ȭf�J����a�I<br>���R�R�|���]�k�A�Ȭf�J����|�Ϊ�������U�A�C<br>�o�q�ɶ��A���\�Z�۷�X��A�p�G�Q���ħL¾�쪺�ܡA�N��ڥd�i�����a�C<br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_08\">�u�{�b�n�W�Գ��I�v</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam kahman_09\">�u�ڭn���ħL¾��C�v</a></body></html>"
#
# �ħL���ɵ��L �Ȭf�J����
# 31555-c1.htm
#abercrombie_c1 = "<html><body>�ħL���ɵ��L�Ȭf�J����G<br>�u�r�A�u���H�·СI�A�S�ݨ��ڦ��ܡH�I�{�b�����I�ħL�����N�w�g���Y�k�աC�ڥi�S�����I���A�o�˪��~�ӤH�I<br>�p�G�Q�[�J�ڭ̶����϶ħL�ΡA�h�䨺�䪺�d�i���a�C�쩳~�ݦb�o�i�c���h�A�a�a��������n�Ȫ��C����~�R�W�ڡI<br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31555-01.htm
#abercrombie_01 = "<html><body>�ħL���ɵ��L�Ȭf�J����G<br>�w����{�I�q�`���O�o�ˡA�b�o�i�c���h�A�a�a�`�O���e������ɵ��~�A�ҥH�N�o�򨯭W�C�ӭ��諸�Ǫ��]���O�O�H�Y�k����~����o�_����t���ɭԦ��ӮƷQ�쪺�C�쩳~���Ǥp���ٯ�Ȧh��~�b�b�o�˽a�m���[�����S����~�u�����դW�Y���Q�k�աH<br>������S�˦۫����ħL�����ɭԤ��O�o�˪��I���ҿפZ�Ƭ����A���O�ܤֵ���U�ǳƤ@�U����r�֦a���M��������I<br>�n�A���n�䪺�F��ܡH���@�U�A�ڬݬݥؿ��C��F�A��ɹ��a�ӤF�a�H<br><a action=\"bypass -h npc_%objectId%_multisell 6281\">�N�����Ϫ��ɹ��洫���ɵ��~</a><br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31555-02.htm
#abercrombie_02 = "<html><body>�ħL���ɵ��L�Ȭf�J����G<br>ť�����Ѥ]�ܼF�`�a�H�u�r�A�o�ħL�Ϊ��B�~�����~�Q�A�����F�H�����A���L�s�b�o���Y�k���a�賣�ߤF�ԥ\�A�ө��B�F�C<br>�n�A���Q�n���F��ܡH���޻��a�C�ҿ׳o�ǸӦ����ɵ��~���M�S���h�֡A���O���Ȭf������|�ɤO�Ӭ����C��F�A��ɹ��a�ӤF�a�H<br><a action=\"bypass -h npc_%objectId%_multisell 6282\">�N�����Ϫ��ɹ��洫���ɵ��~</a><br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
#
# �ħL����ȧL ���R�R
# 31556-c1.htm
#selina_c1 = "<html><body>�ħL����ȧL���R�R�G<br>��...�A�r�C�A�J���ݩ�o�����϶ħL�ΡA�S���O�ڪ��k�B�ͧa�H�O�Чڦn�ܡH�@�H<br>�A�Q�䴩�ħL���ܡH����A�h��ݰ_�ӭ��c���b�~�H���̧a�C</body></html>"
# 31556-c2.htm
#selina_c2 = "<html><body>�ħL����ȧL���R�R�G<br>���A�A�[�J�ڭ̳����F�ܡH����...<br>�ڥs���R�R�A�O��ȧL�C�Цh���СC<br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31556-c3.htm
#selina_c3 = "<html><body>�ħL����ȧL���R�R�G<br>�A�r�A�i���]�n�A���]�n���U����a�C�A�o�˴����O�˪��^�Ӫ��ܡA�s���쪺�H��ı�o���n�N���...�I<br>���L�A���W�A�F�C�������A�A�j�a��ı�o���@�I���Ʊ�C�ڤ]�Q���]�k���A�p�p����...���ݭn�F�誺�ܾ��޻��C<br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31556-01.htm
selina_01 = "<html><body>�ħL����ȧL���R�R�G<br>�A�r�A�i���]�n�A���]�n���U����a�C�A�o�˴����O�˪��^�Ӫ��ܡA�s���쪺�H��ı�o���n�N���...�I<br>���L�A���W�A�F�C�������A�A�j�a��ı�o���@�I���Ʊ�C�ڤ]�Q���]�k���A�p�p����...���ݭn�F�誺�ܾ��޻��C<br><a action=\"bypass -h Quest 628_HuntGoldenRam 1\">�z�I�����G�ݭn�����Ϫ��ɹ� 2��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 2\">�����O��G�ݭn�����Ϫ��ɹ� 2��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 3\">�O�q�j�ơG�ݭn�����Ϫ��ɹ� 3��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 4\">�F������G�ݭn�����Ϫ��ɹ� 3��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 5\">�g�Ԥh��G�ݭn�����Ϫ��ɹ� 3��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 6\">�l������G�ݭn�����Ϫ��ɹ� 3��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 7\">�]�O�ʤơG�ݭn�����Ϫ��ɹ� 6��</a><br><a action=\"bypass -h Quest 628_HuntGoldenRam 8\">�t�׿E�o�G�ݭn�����Ϫ��ɹ� 6��</a><br><a action=\"bypass -h npc_%objectId%_Quest\">����</a></body></html>"
# 31556-02.htm
selina_02 = "<html><body>�ħL����ȧL���R�R�G<br>�کҹB�Ϊ��]�O�O�ħL�ΰ]�����@�����C�ҥH���A����K�O�����z�I�i���U�]�k�C�o��I<font color=\"LEVEL\">�����Ϫ��ɹ�</font>�����N���C�Y����񴵶����������ȡA�N�|�o��ɹ��������S�C�а��ѦҡC</body></html>"

#Npcs
KAHMAN      = 31554  # �ħL �d�i��
ABERCROMBIE = 31555  # �ħL���ɵ��L �Ȭf�J����
SELINA      = 31556  # �ħL����ȧL ���R�R
NPCS        = range(31554,31557)

#Items
RECRUIT         = 7246  # �����Ϫ��лx-�s�L
SOLDIER         = 7247  # �����Ϫ��лx-��U�L
CHITIN          = 7248  # �䥬�L�S�q��d�ݪ��Ҵ�
CHITIN2         = 7249  # ���h�q��d�ݪ��Ҵ�
GOLDEN_RAM_COIN = 7251  # �����Ϫ��ɹ�

#chances
MAX = 100
CHANCE={
    21508:50, # �䥬�L�S�q��d��
    21509:43, # �䥬�L�S�q��d�ݤu�H
    21510:52, # �䥬�L�S�q��d�ݤh�L
    21511:57, # ���ʫ䥬�L�S�q��d��
    21512:75, # ���ʫ䥬�L�S�q��d��
    21513:50, # ���h�q��d��
    21514:43, # ���h�q��d�ݤu�H
    21515:52, # ���h�q��d�ݤh�L
    21516:53, # ���ʥ��h�q��d��
    21517:74  # ���ʥ��h�q��d��
}
#"event number":[Buff Id,Buff Level,Cost]
BUFF={
"1":[4404,2,2], # �z�I�����G�ݭn�����Ϫ��ɹ� 2��
"2":[4405,2,2], # �����O��G�ݭn�����Ϫ��ɹ� 2��
"3":[4393,3,3], # �O�q�j�ơG�ݭn�����Ϫ��ɹ� 3��
"4":[4400,2,3], # �F������G�ݭn�����Ϫ��ɹ� 3��
"5":[4397,1,3], # �g�Ԥh��G�ݭn�����Ϫ��ɹ� 3��
"6":[4399,2,3], # �l������G�ݭn�����Ϫ��ɹ� 3��
"7":[4401,1,6], # �]�O�ʤơG�ݭn�����Ϫ��ɹ� 6��
"8":[4402,2,6], # �t�׿E�o�G�ݭn�����Ϫ��ɹ� 6��
}

#needed count
count = 100

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = range(7246,7250)

	def onAdvEvent (self,event,npc,player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		if str(event) in BUFF.keys():
			skillId,level,coins=BUFF[event]
			if st.getQuestItemsCount(GOLDEN_RAM_COIN) >= coins :
				st.takeItems(GOLDEN_RAM_COIN,coins)
				npc.setTarget(player)
				npc.doCast(SkillTable.getInstance().getInfo(skillId,level))
				htmltext = selina_01
			else :
				htmltext = selina_02
		elif event == "31554-03.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "kahman_06" :
			htmltext = kahman_06
			st.takeItems(CHITIN,-1)
			st.giveItems(RECRUIT,1)
			st.set("cond","2")
			st.playSound("ItemSound.quest_middle")
		elif event == "kahman_10" :
			htmltext = kahman_10
			st.exitQuest(1)
			st.playSound("ItemSound.quest_giveup")
		# �ħL �d�i��
#		elif event == "kahman_c1" :
#			htmltext = kahman_c1
#		elif event == "kahman_c2" :
#			htmltext = kahman_c2
		elif event == "kahman_04" :
			htmltext = kahman_04
		elif event == "kahman_05" :
			htmltext = kahman_05
		elif event == "kahman_06" :
			htmltext = kahman_06
		elif event == "kahman_07" :
			htmltext = kahman_07
		elif event == "kahman_08" :
			htmltext = kahman_08
		elif event == "kahman_09" :
			htmltext = kahman_09
		elif event == "kahman_10" :
			htmltext = kahman_10
		elif event == "kahman_11" :
			htmltext = kahman_11
		elif event == "kahman_12" :
			htmltext = kahman_12
		# �ħL���ɵ��L �Ȭf�J����
#		elif event == "abercrombie_c1" :
#			htmltext = abercrombie_c1
#		elif event == "abercrombie_01" :
#			htmltext = abercrombie_01
#		elif event == "abercrombie_02" :
#			htmltext = abercrombie_02
		# �ħL����ȧL ���R�R
#		elif event == "selina_c1" :
#			htmltext = selina_c1
#		elif event == "selina_c2" :
#			htmltext = selina_c2
#		elif event == "selina_c3" :
#			htmltext = selina_c3
		elif event == "selina_01" :
			htmltext = selina_01
		elif event == "selina_02" :
			htmltext = selina_02
		return htmltext

	def onTalk(self, npc, player) :
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st :return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		chitin1 = st.getQuestItemsCount(CHITIN)
		chitin2 = st.getQuestItemsCount(CHITIN2)

		if id == State.CREATED :
			if npcId == KAHMAN and cond == 0 :
				if player.getLevel() >= 66 :
					htmltext = "31554-02.htm"
				else :
					htmltext = "31554-01.htm"
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == KAHMAN :
				if cond == 1 :
					if chitin1 >= 100 :
						htmltext = kahman_05
					else:
						htmltext = kahman_04
				elif cond == 2 :
					if chitin1 >= 100 and chitin2 >= 100 :
						htmltext = kahman_11
						st.takeItems(RECRUIT,-1)
						st.giveItems(SOLDIER,1)
						st.takeItems(CHITIN,-1)
						st.takeItems(CHITIN2,-1)
						st.set("cond","3")
						st.playSound("ItemSound.quest_middle")
					else :
						htmltext = kahman_07
				elif cond == 3 :
					htmltext = kahman_12
#			elif npcId == ABERCROMBIE :
#				if cond == 2 :
#					htmltext = abercrombie_01
#				elif cond == 3 :
#					htmltext = abercrombie_02
			elif npcId == SELINA :
				if cond == 3 :
					htmltext = selina_01
		return htmltext

	def onFirstTalk(self, npc, player) :
		st = player.getQuestState(qn)
		if not st :
			st = self.newQuestState(player)

		npcId = npc.getNpcId()
		cond = st.getInt("cond")

		if npcId == KAHMAN :
#			if cond in [1] :
#				return "31554-c1.htm"
			if cond in [2,3] :
				return "31554-c2.htm"
		elif npcId == ABERCROMBIE :
			if cond in [1] :
				return "31555-c1.htm"
			elif cond == 2 :
				return "31555-01.htm"
			elif cond == 3 :
				return "31555-02.htm"
		elif npcId == SELINA :
			if cond in [1] :
				return "31556-c1.htm"
			elif cond == 2 :
				return "31556-c2.htm"
			elif cond == 3 :
				return "31556-c3.htm"
		player.setLastQuestNpcObject(npc.getObjectId())
		npc.showChatWindow(player)
		return ""

	def onKill(self,npc,player,isPet):
		partyMember = self.getRandomPartyMemberState(player, State.STARTED)
		if not partyMember : return
		st = partyMember.getQuestState(qn)
		if st :
			if st.getState() == State.STARTED :
				npcId = npc.getNpcId()
				cond = st.getInt("cond")
				chance = CHANCE[npcId]*Config.RATE_QUEST_DROP
				numItems, chance = divmod(chance,MAX)
				if self.getRandom(100) <chance :
					numItems = numItems + 1
				item = 0
				if cond in [1,2] and npcId in range(21508,21513):
					item = CHITIN       
				elif cond == 2 and npcId in range(21513,21518):
					item = CHITIN2
				if item != 0 and numItems >= 1 :
					prevItems = st.getQuestItemsCount(item)
					if count > prevItems :
						if count <= (prevItems + numItems) :
							numItems = count - prevItems
							st.playSound("ItemSound.quest_middle")
						else :
							st.playSound("ItemSound.quest_itemget")
						st.giveItems(item,int(numItems))
		return

QUEST		= Quest(628,qn,"�����Ϫ����y")

QUEST.addStartNpc(KAHMAN)

for i in NPCS:
	QUEST.addFirstTalkId(i)
for i in NPCS:
	QUEST.addTalkId(i)

for mob in range(21508,21518):
	QUEST.addKillId(mob)