# 2010-06-26 by Gnacik
# Based on official server Franz
# update by pmq
# High Five 12-2-2011
import sys
from com.l2jserver.gameserver.ai                    import CtrlIntention
from com.l2jserver.gameserver.model.quest           import State
from com.l2jserver.gameserver.model.quest           import QuestState
from com.l2jserver.gameserver.model.quest.jython    import QuestJython as JQuest
from com.l2jserver.gameserver.network.serverpackets import ExStartScenePlayer
from com.l2jserver.gameserver.network.serverpackets import NpcSay

qn = "193_SevenSignDyingMessage"

# NPCs
HOLLINT       = 30191  # �j���x �N���L�S
CAIN          = 32569  # ���x �ͦ]
ERIC          = 32570  # ���Įv ��O�J
ATHEBALDT     = 30760  # �j���F�� �ȤӪk�S��
SHILENSEVIL   = 27343  # �u�Y������
# ITEMS
JACOB_NECK    = 13814  # ���U������
DEADMANS_HERB = 13816  # ���̪��į�
SCULPTURE     = 14353  # �ðݪ��J��

# �j���x �N���L�S
# 30191-03.htm
hollint_03 = "<html><body>�j���x �N���L�S�G<br>�t�d���F�����O<font color=\"LEVEL\">���x�ͦ]</font>�C<br>�L�b<font color=\"LEVEL\">�ڷ竰�������񪺼��F������</font>����C<br>�٦��A�ڦb������w���ĤJ���֪���ë�A�o�Ʊ��]�бz�O�ѤF��i���x�ͦ]�C<br>�@����Ī����ֻP�z�P�b...</body></html>"
#
# ���x �ͦ]
# 32569-01.htm
cain_01 = "<html><body>���x �ͦ]�G<br>���M�|���ӭ��ͤH�ӧ�ڡA�ݨӦb�o�@�W���Y�Ө����A�S���@�ӥͩR���h�F�L�����~...<br>��A�A�O�Ӭ����|�漢�F�����O�H�i�D�ڨ��s�h�ߧa�C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_02\">�ڬO�e���|�涮�U�����F��</a></body></html>"
# 32569-02.htm
cain_02 = "<html><body>���x �ͦ]�G<br>�����x�H�u�O�_�ǰ�...�e�X�Ѥ~��赲���F�@�Ӽ��F���A�]�O�P�]�I���ӤH����L���t�@�ӸG�H�����x..<br>�A���S���@�ӫ����x���F�O�ܡH�I..��..<br>�O�֤��ЧA�L�Ӫ��H<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_03\">�ڬO�g�Ѥj���x�N���L�S���йL�Ӫ�</a></body></html>"
# 32569-03.htm
cain_03 = "<html><body>���x �ͦ]�G<br>�A�����O�ڷ竰���j���x�N���L�S�ܡH<br>�o�򻡡A�o�����������x�O�b�t�d�l���ڷ竰��P�]�I���ӤH�����������o�C<br>�W�������O���F�S���������x�O..<br>�J�M�O�ѧA���|�漢�F���A����Ĥ@�ӵo�{���骺�H���ӴN�O�A�a�C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_04\">�O���A�S��</a></body></html>"
# 32569-04.htm
cain_04 = "<html><body>���x �ͦ]�G<br>�A�u�O���H�浽��..���L�b�i�漢�F�����e�A�ڭ̦��Ӱ��D�s�b�C<br>���F�b���F�������I�����ܡA�N�n�Ψ�s��<font color=\"LEVEL\">�u���̪��į�v</font>���F��...���̪��|�檺���F���Ӧh�A�ҥH�į�]���Χ��F�C<br>�A�[�W�A�����n�e�Ӧ��̪��į�<font color=\"LEVEL\">���Įv��O�J</font>�S��𥼨�...<br>�L�֩w�O���F�Ķ����_���į�A�ѤF�ڪ��e�U�C<br>�A�h���O�J�A���ڻ��<font color=\"LEVEL\">�u���̪��į�v</font>�n�ܡH���F�|�漢�F���A�����n�����̪��į�~��C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_05\">�ڷ|���A������̪��į�^��</a></body></html>"
# 32569-05.htm
cain_05 = "<html><body>���x �ͦ]�G<br>���§A�I����A����h��<font color=\"LEVEL\">���Įv��O�J</font>�A<br>�M��A�ɶq�h����@��<font color=\"LEVEL\">�u���̪��į�v</font>�C<br>�ڷQ�L���ӷ|�b<font color=\"LEVEL\">���먦</font>������A�]�����Ӧa��H�X���öQ���į�ӻD�W�C<br>�٦��A�p�G�A���a�Ӧ��̪��򪫡A�N�⥦�浹�ڧa�C<br>�@�I�I�I�b�򪫤W���o�ۯ��t���𮧡A�ݨ��N���L�S�w�N�����̯��֪���ë�ĤJ�F�䤤�C���\�O�N���L�S�C<br>����A�A�N�֥h��^�į�a�C</body></html>"
# 32569-06.htm
cain_06 = "<html><body>���x �ͦ]�G<br>���n�����A�֥h��b<font color=\"LEVEL\">���먦</font>����<font color=\"LEVEL\">���Įv��O�J</font>�A<br>�ӥB���n�ѤF��^<font color=\"LEVEL\">�u���̪��į�v</font>�I�I�I</body></html>"
# 32569-07.htm
cain_07 = "<html><body>���x �ͦ]�G<br>�a�^<font color=\"LEVEL\">���̪��į�</font>�աA�⥦�浹�ڧa�C<br>�u�O���W�A�F�C����ڭ̴N�ӥ����a�|�漢�F���C<br>�a�L�Ӥ@�I�A�M��H�@�۪��߶}�l�|�漢�F���a�C����A�ǳƦn�F�ܡH<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage 9\">�O���A�ǳƦn�F</a></body></html>"
# 32569-08.htm
cain_08 = "<html><body>���x �ͦ]�G<br>�u�_��...�A�]�ݨ�F�ܡH<br>��ڧ���m�첽�®ɡC�����¤W�誽�Ī��R�����c���¦���K...<br>�۱q�|�漢�F���H�ӡA�q�ӨS���o�͹L�o�˪��Ʊ��I�I�I<br>�u�Q���z���¦���K���N�q..�p�G���O�t�����̱j�P�����@...���N��ܱ��H�Ǫ����c�𮧿Ķi�F�򪫤���...<br>�`���A�̦n�٬O�o�J���[��o�Ӷ���C<br>�x�I�I�I���өǤH�O�֡H�I�I<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_09\">�����P��</a></body></html>"
# 32569-09.htm
cain_09 = "<html><body>���x �ͦ]�G<br>��M�_�X�Ӫ����өǤH�O����H<br>�n�ӧ����ڭ̤F�I�I�I�Ʊ��ڭ̵y��A�͡I�I�I<br>��Ȥ���O�n�B�z�����өǤH�I�I�I</body></html>"
# 32569-10.htm
cain_10 = "<html><body>���x �ͦ]�G<br>���M�|�Q�ǤH��ŧ...�q���夤���o�¦�𮧫�A�ǤH�N�X�{�F�C<br>�i��b�o���`���I��A���ӻݭn�d�����T��..�S���A�n���O����<font color=\"LEVEL\">���e���T��</font>�C<br>�ڦb�Q�A��ڱN�o�����m�W���®ɡA���Ѩ㦳���c�𮧥B���Ī��¦���K�A�n���N�P���ӨӾ��������ǤH���s�e�ʡC<br>�ڻ{���o�O���U�Q�n���o�����ۤv�M<font color=\"LEVEL\">�����x�̦��`</font>���u�ۡA�ҥH�L���t����j�N�@������A�~�|�ިӨ��өǤ�C<br>�Ө��өǤH�N�O���F����ӯu�۳Q���o�A�ҥH�~�|�ӷm�ܨ��Ӷ���C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_11\">�~��ť�G��</a></body></html>"
# 32569-11.htm
cain_11 = "<html><body>���x �ͦ]�G<br>�����x�̪��s�򦺤`�ƥ�M���өǤH..�H�γs���ӥX�{�b���F�������N�Q����...<br>�ӥB�ܤ��کҽլd�����G�A�M�A�|�Q�o���o��Ʊ�...�γ\�]���໡�O�ӯº骺���M..<br>���L�A�A��ť���L����<font color=\"LEVEL\">�C�ʦL</font>���Ʊ��ܡH<br>�S���A�N�O���F�ʦL�ۡA<font color=\"LEVEL\">�����M�����������v��</font>�C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_12\">�ڦ�ť���L</a></body></html>"
# 32569-12.htm
cain_12 = "<html><body>���x �ͦ]�G<br>���A�ڬO���ݩ󾤩������K�F���C<br>�{�b�|�ѧڨӾ�����F�������x�A�]�O�]���������������{���A�̪�o�ͪ��i�ê��s�򦺤`�ƥ�M�C�ʦL���s�e�ʡC<br>�ӥB�A���P�O�o�q���������ݡA���ӨӾ��������ǤH�A�ש�b���ѥX�{�F�C<br>�M��A�������өǤH���A�A�N�O�ڭ̾����o�@��D�֦����i���H�C<br>����...�n���n�M�ڭ̾����@�_�X�@�H�`ı�o�n�O�N�o�˿��L�A�A�ڤ@�w�|�D�`�ᮬ���C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage cain_13\">�ڷQ�n�@�_�X�@</a></body></html>"
# 32569-13.htm
cain_13 = "<html><body>���x �ͦ]�G<br>�Ӧn�F�I�I�I�I�A�@�w�O�ӳ̨ΤH��A�Ӵ��o�s�򦺤`�ƥ�M�C�ʦL�������s�e�ʡC<br>�H�ڳo�L�z���w����O�]����P����O�C<br>�ӡA����h���X�t�d�ڭ̾����x�ƪ�<font color=\"LEVEL\">�j���F�� �ȤӪk�S��</font>�A�L�b���o�̤�����<font color=\"LEVEL\">�ڷ竰��</font>�C<br>�h��L�A�çi�D�L�O�ѧڤ��йL�Ӫ��C<br>�����d�b���媺���e���T���M�ǤH���Ʊ��A�ڷ|�A���I��s�A�M��t�~�V�ȤӪk�S�봣��լd���i�C<br>����A���֥h��<font color=\"LEVEL\">�j���F�� �ȤӪk�S��</font>�a�C<br>�٦��@�I�I�I�I���өǤH�γ\�|���ܧA�A�ҥH�ȥ��n�[�򨾳ƫ��I�I�I�I</body></html>"
#
# ���Įv ��O�J
# 32570-01.htm
eric_01 = "<html><body>���Įv ��O�J�G<br>����Q�F�H��ڳo�h�a�����Įv���ƶܡH<br>�Y�Q�n�T�]�A�ڬݧA�O�ն]�@��C�ھ֦����A�]�u���L�O�o�X�گ�}�F�C<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage eric_02\">�ڬO�����x�ͦ]���e�U�ӨӪ�</a></body></html>"
# 32570-02.htm
eric_02 = "<html><body>���Įv ��O�J�G<br>���x�ͦ]�H�u�r�I�I�I�I�V�|�A�ڳ��M�ѱo�@���G�b�C<br>�@�W�~���ڡA�Ʊ��۵M�N�O���M�F...<br>�ڤ@�ߴM��u���F���t�\��v..���M�⥦���ѤF�C<br>���A�N�O�ӻ���ͦ]�e�U���u���̪��į�v���ܡH<br>�ӡA�u���̪��į�v�b�o�̡C���֮��h�浹�ͦ]�A�M�ᶶ�K��L���n��p�C</body></html>"
# 32570-03.htm
eric_03 = "<html><body>���Įv ��O�J�G<br>�W�~���F�A�H�ɳ��|���O���M�Ʊ����ɭ�...<br>�A�٨S�X�o�ڡH<br>���ֱN�į���浹�ͦ]�C</body></html>"
#
# �j���F�� �ȤӪk�S��
# 30760-01.htm
athebaldt_01 = "<html><body>�j���F�� �ȤӪk�S��G<br>�A�O���x�ͦ]���йL�Ӫ��H�@�I�I��ӬO�A�ڡC�ڱq�ͦ]���̤w��ť������A<br>�ͦ]�ٻ��F�ܦh�����A���n�ܩO�C<br>�ڦ��ܦh�Ʊ��Q�nť�A���A�ӥB�]�Q�����Ať�C<br>���O�b�����e�A�ڷQ������·N�A�P�§A����U���x�ͦ]�A���F�ڭ̾����ݭn�լd���Ʊ��C<br>�A�|�����ڭ̾��������¶ܡH<br><a action=\"bypass -h Quest 193_SevenSignDyingMessage athebaldt_02\">�ڷ|�ۤ߱���</a></body></html>"
# 30760-02.htm
athebaldt_02 = "<html><body>�j���F�� �ȤӪk�S��G<br>�ӡA�����ڭ̪����§a�C<br>����A�ڷQ�A�]�Ӳ֤F�A���P�ȳ~���ҹy��A�A�ӧ�ڧa�C<br>�����C�ʦL���Ʊ��A�ڦ��ܦh�ܭn��A���C</body></html>"

class Quest (JQuest) :
	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [JACOB_NECK, DEADMANS_HERB, SCULPTURE]

	def onAdvEvent(self, event, npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		if event == "30191-02.htm" :
			st.set("cond","1")
			st.setState(State.STARTED)
			st.giveItems(JACOB_NECK, 1)
			st.playSound("ItemSound.quest_accept")
		elif event == "cain_05" :
			htmltext = cain_05
			st.set("cond","2")
			st.takeItems(JACOB_NECK,1)
			st.playSound("ItemSound.quest_middle")
		elif event == "eric_02" :
			htmltext = eric_02
			st.set("cond","3")
			st.giveItems(DEADMANS_HERB, 1)
			st.playSound("ItemSound.quest_middle")
		elif event.isdigit() :
			if int(event) == 9 :
				st.takeItems(DEADMANS_HERB,1)
				st.set("cond","4")
				st.playSound("ItemSound.quest_middle")
				player.showQuestMovie(int(event))
				return ""
		elif event == "cain_09" :
			htmltext = cain_09
			npc.broadcastPacket(NpcSay(npc.getObjectId(),0,npc.getNpcId(),"�u" + player.getName() + "�v�I�ڭ̱o���˨��өǤH�A�ڷ|�ɥ��O�����A���I"))
			monster = self.addSpawn(SHILENSEVIL, 82624, 47422, -3220, 0, False, 60000, True)
			monster.broadcastPacket(NpcSay(monster.getObjectId(),0,monster.getNpcId(),"���Ӫ��~���D�H���O�A��..."))
			monster.setRunning()
			monster.addDamageHate(player,0,999)
			monster.getAI().setIntention(CtrlIntention.AI_INTENTION_ATTACK, st.getPlayer())
		elif event == "cain_13" :
			htmltext = cain_13
			st.set("cond","6")
			st.takeItems(SCULPTURE,1)
			st.playSound("ItemSound.quest_middle")
		elif event == "athebaldt_02" :
			htmltext = athebaldt_02
			st.addExpAndSp(52518015,5817677)
			#st.addExpAndSp(25000000,2500000)  # ��½�� �g���
			st.unset("cond")
			st.setState(State.COMPLETED)
			st.exitQuest(False)
			st.playSound("ItemSound.quest_finish")
		#  �j���x �N���L�S
		elif event == "hollint_03" :
			htmltext = hollint_03
		#  ���x �ͦ]
		elif event == "cain_01" :
			htmltext = cain_01
		elif event == "cain_02" :
			htmltext = cain_02
		elif event == "cain_03" :
			htmltext = cain_03
		elif event == "cain_04" :
			htmltext = cain_04
		elif event == "cain_05" :
			htmltext = cain_05
		elif event == "cain_06" :
			htmltext = cain_06
		elif event == "cain_07" :
			htmltext = cain_07
		elif event == "cain_08" :
			htmltext = cain_08
		elif event == "cain_09" :
			htmltext = cain_09
		elif event == "cain_10" :
			htmltext = cain_10
		elif event == "cain_11" :
			htmltext = cain_11
		elif event == "cain_12" :
			htmltext = cain_12
		elif event == "cain_13" :
			htmltext = cain_13
		#  ���Įv ��O�J
		elif event == "eric_01" :
			htmltext = eric_01
		elif event == "eric_02" :
			htmltext = eric_02
		elif event == "eric_03" :
			htmltext = eric_03
		#  �j���F�� �ȤӪk�S��
		elif event == "athebaldt_01" :
			htmltext = athebaldt_01
		elif event == "athebaldt_02" :
			htmltext = athebaldt_02
		return htmltext

	def onTalk (self, npc, player) :
		htmltext = Quest.getNoQuestMsg(player)
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			htmltext = Quest.getAlreadyCompletedMsg(player)
		elif id == State.CREATED :
			if npcId == HOLLINT and cond == 0 :
				first = player.getQuestState("192_SevenSignSeriesOfDoubt")
				if first and first.getState() == State.COMPLETED and player.getLevel() >= 79 :
					htmltext = "30191-01.htm"
				else :
					htmltext = "30191-00.htm"
					st.exitQuest(True)
		elif id == State.STARTED :
			if npcId == HOLLINT :
				if cond == 1 :
					htmltext = hollint_03
			elif npcId == CAIN :
				if cond == 1 :
					htmltext = cain_01
				elif cond == 2 :
					htmltext = cain_06
				elif cond == 3 :
					htmltext = cain_07
				elif cond == 4 :
					htmltext = cain_08
				elif cond == 5 :
					htmltext = cain_10
			elif npcId == ERIC :
				if cond == 2 :
					htmltext = eric_01
				elif cond == 3 :
					htmltext = eric_03
			elif npcId == ATHEBALDT :
				if cond == 6:
					htmltext = athebaldt_01
		return htmltext

	def onKill(self, npc, player, isPet) :
		st = player.getQuestState(qn)
		if not st : return
		if npc.getNpcId() == SHILENSEVIL and st.getInt("cond") == 4 :
			npc.broadcastPacket(NpcSay(npc.getObjectId(),0,npc.getNpcId(),"�u" + player.getName() + "�v�I�{�b�ڴN���A�@�B..���L�A�ڤ@�w�|���A���C"))
			npc.broadcastPacket(NpcSay(32569,0,32569,"�ܦn�A�u" + player.getName() + "�v�C�ܰ��������o�W�A�C"))
			st.giveItems(SCULPTURE, 1)
			st.set("cond", "5")
			st.playSound("ItemSound.quest_middle")
		return

QUEST	= Quest(193,qn,"�C�ʦL�A���e���T��")

QUEST.addStartNpc(HOLLINT)
QUEST.addTalkId(HOLLINT)
QUEST.addTalkId(CAIN)
QUEST.addTalkId(ERIC)
QUEST.addTalkId(ATHEBALDT)
QUEST.addKillId(SHILENSEVIL)