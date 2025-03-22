# Created by Gigiikun
# Update by pmq 16-09-2010

import sys
from com.l2jserver import Config
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "643_RiseandFalloftheElrokiTribe"
#Npc
Singsing = 32106
Karakawei = 32117
#Settings: drop chance in %
DROP_CHANCE = 75
#Mobs
PLAIN_DINOSAURS = [22200,22201,22202,22219,22203,22204,22205,22220,22208,22209,22210,22211,22212,22213,22221,22222,22226,22227]
#Item
BONES_OF_A_PLAINS_DINOSAUR = 8776
REWARDS = range(8712,8723)
# Singsing npc Html
# 32106-00
Singsing_A = "<html><body>���D�G<br>��~�_�I�a��~�b��M�i�����Ʊ��ܡH�o���o�̵o�{��l���q�A�ȤB��f�b�o�̶}�]�F�@�ӽX�Y�C<br>��M�o�a�誺�_�I�a�����W�[�A���߳o�̪��]�k�v�]�v���W�[�C<br>�ڭ̰��F�ǳƲ�A�]���ѫK�Q���A�ȵ��ӳX���a���H�A�ӥB�]�P��������C<br>�{�b���ѫ_�I�a�̻P�e�U�̭̪��pô�~�ȡC<br>��F�C�{�b������@�өe�U...<br>�@...<br>�ݨӳo�e�U��_�I�a�z���I�x����C<br>(�u���F�쵥��75�H�W�~�������ȡC)</body></html>"
# 32106-01
Singsing_B = "<html><body>���D�G<br>��~�_�I�a��~�b��M�i�����Ʊ��ܡH�o���o�̵o�{��l���q�A�ȤB��f�b�o�̶}�]�F�@�ӽX�Y�C<br>��M�o�a�誺�_�I�a�����W�[�A���߳o�̪��]�k�v�]�v���W�[�C<br>�ڭ̰��F�ǳƲ�A�]���ѫK�Q���A�ȵ��ӳX���a���H�A�ӥB�]�P��������C<br>�P�ɤ]���ѫ_�I�a�̻P�e�U�̭̪��pô�~�ȡC<br>��F�C�{�b������@�өe�U...<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_C\">�O����e�U�O�H</a></body></html>"
# 32106-02
Singsing_C = "<html><body>���D�G<br>�b�o��l���q�Ϯ��ۤӥj���ͪ�-���s�A�O�b�ȤB�j���ݤ��쪺�C�����Ѫ��]�k�v�̻��]���s�ѯ����Ȩe�̱j�����O�q�A�]�����P���H�êӧ@�ԹL�C�]�Y�ح�]�b�ȤB�j���w�g�������o�ǥͪ����b���a�Q�o�{�F�C<br>�b�X�Y����u���o�{����L�z���ͪ��A<br>�s������檺�]�k�v�����F��s�ݭn���ͪ������Y�C�p�G���Ѯ��s�a�^�������Y�A�ڱN���ʶR��F���e�U�H�C�z�n�����e�U�ܡH<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_D\">�ϰϨ��ؤp��...�ګַܼN���z</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_I\">���n�N��...�ڹ益���������߯g...�藍�_</a></body></html>"
# 32106-03
Singsing_D = "<html><body>���D�G<br>�ڡA�G�M�O�ӫ_�I�a�ڡC���y<font color=\"LEVEL\">�����s�B�����s�B�p�Y�s�B���ͮy�s</font>�̤���A���^<font color=\"LEVEL\">���쮣�s�����Y</font>�ڴN�|��F�������C<br>��F�A�P�o�q������������B�ͻ��A�������G�N�h�]�b�M��o���s�����Y�C�p�G�z������h�������G�N�h�a�C<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_E\">�����G�N�h�Ҧb����m�O�H</a></body></html>"
# 32106-04
Singsing_E = "<html><body>���D�G<br>�������G�N�h�b���a�n�誺��l������n�����@�өt�q�C�]���ƥ��~�Ӫ̡A�ҥH�u��z�L��l����n�������P�������_�ޤ������s�S�����A�s��<font color=\"LEVEL\">�کԩ_��</font>�������Ԥh�~��i�J���t�q�C</body></html>"
# 32106-05
Singsing_F = "<html><body>���D�G<br>���֧⮣�s�����Y�����^�ӧa�A�����@���b�ʩO�C<br>�n���O�]���S�����s�����Y�L�k�i���s...<br>���O�Y�N�n�b�̯��ګ��]�k��|�o���s���e�O�C<br>�бz�A�h�V�O�I<br>���y<font color=\"LEVEL\">�����s�B�����s�B�p�Y�s�B���ͮy�s</font>�̤���A���^<font color=\"LEVEL\">���쮣�s�����Y</font>�N�i�H�F�C</body></html>"
# 32106-05a
Singsing_G = "<html><body>���D�G<br>�@�I�z���^<font color=\"LEVEL\">���쮣�s�����Y</font>�աC�����^�Ӫ�<font color=\"LEVEL\">���쮣�s�����Y</font>�A�ﲦ��檺��s�|���ܤj�����U�C<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_H\">�N���^�����쮣�s�����Y�洫������</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_J\">���u�N�����쪺���쮣�s�����Y�����浹�����G�N�h�v</a></body></html>"
# 32106-06
Singsing_H = "<html><body>���D�G<br>�ڡA�o�ӧڷ|�n�n���áC�@�w�|��F������檺�C�����@�w�|�ܳ��w�C<br>�o�O�e�U���O�ΡC���M���h���]�бz���U�C<br>�n�~�򱵨��e�U�ܡH<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_L\">�~��u�@</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_I\">�����F</a></body></html>"
# 32106-07
Singsing_I = "<html><body>���D�G<br>�ڡA�O�ܡC��_�I�a�z�ӻ��A�o�y�q�n�����O�ӥO�z�ΪA���a��C�o�̦��ܦh�z�Q�����������X�S��... (�o�ˤ]�s�_�I�a�ڡH)</body></html>"
# 32106-08
Singsing_J = "<html><body>���D�G<br>��~��ӳo�˰�...�@...��<font color=\"LEVEL\">���쮣�s�����Y</font>�浹�֨��O�_�I�a�z�ۤv�i�����M�w...���O���������Q�бz���s�Ҽ{�@�U�C<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_E\">�����G�N�h�b���̡H</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Singsing_K\">�z�L�����G�N�h�i�H�o��Ǥ���H</a><br></body></html>"
# 32106-08a
Singsing_K = "<html><body>���D�G<br>ť���V�������G�N�h�̥�I���쮣�s�����Y300�Ӫ��ܡA�N���H���o��<font color=\"LEVEL\">���F�s�@A�ůS�ŪZ��������</font>�C<br>�ӥB�A�̪��ٻ��O�|��<font color=\"LEVEL\">S80���b</font>�@�����y�~�O�C�o�ǪF��̷Ӫ��~�N�|�n�D���쮣�s�����Y100~300�ӥ��k�C<br>���O�A�p�G�z�L�ڪ��ܡA�N���ݸg�L�·Ъ�����A�u�n�H<font color=\"LEVEL\">����</font>�N��洫�F�C�ҥH�бz�V���Ҽ{�A�O���X���ۤv�ᮬ����ܡC</body></html>"
# 32106-09
Singsing_L = "<html><body>���D�G<br>���·бz�~��V�O�C���y<font color=\"LEVEL\">�����s�B�����s�B�p�Y�s�B���ͮy�s</font>����A���^<font color=\"LEVEL\">���쮣�s�����Y</font>�N�i�H�F�C</body></html>"
# Singsing npc Html
# 32117-01
Karakawei_A = "<html><body>�d�ԥd���G<br>�ڻ��ڭ̤@�ڬO���F�ʵ��s�����|�ߩȪ��ӥj�j�O�ͩR��-���s�A���j���k���u�Y�ҬD��X����j�رڡC���O�����q��ɰ_�u�Y��ڭ̪���ë�S���^���C<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_B\">�߰ݬ�����S���^��</a></body></html>"
# 32117-02
Karakawei_B = "<html><body>�d�ԥd���G<br>���ӧڭ̤]���ӲM���C���D�ڭ̤@�ڦ����줰�򤣩����Ʊ��ܡH���ޫ�ˡA�ڭ̺رڤ@�w�n��_�u�Y�����d�C���h���d���ڭ̤@���ܪ��V�ӶV���z...�ͯf...�ٳQ�ڭ̩Һʵ������s����...�رڥ��������I�ܡC<br>�~�Ӫ��_�I�a�ڡA�ڭ̬��F�v¡�ڭ̺����`�����f�A�H�ά��F�|���_�u�Y�����d�������A�ݭn���~...<br>���F�ڭ̡A�A�i�H���X<font color=\"LEVEL\">���쮣�s�����Y</font>�ܡH�p�G��U�ڭ̧�����_���d�������A����ڷ|���A�̥Ω�s�@�Z�������ơA�Ӭ��F�v���f����U�ڭ̻s�@�ħ����ܡA�ڷ|���A�Ω�s�@�Z�����s�@���b�ӳ����A�C<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_D\">�бN���쮣�s�����Y300�ӥΩ�u�����v�W</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_F\">�бN���쮣�s�����Y�ά��u�ħ��v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_H\">��A�̨���l�رڪ����`�S���򿳽�A�H�A�K�a</a></body></html>"
# 32117-02a
Karakawei_C = "<html><body>�d�ԥd���G<br>�O���ɭԪ��_�I�a��...�A�ӧ�ڭ̤@�ڬO����ơH<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_A\">�߰ݦ����C���iù�@�ڪ������I�`</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_D\">�бN���쮣�s�����Y300�ӥΩ�u�����v�W</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_F\">�бN���쮣�s�����Y�ά��u�ħ��v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe Karakawei_H\">��A�̨���l�رڪ����`�S���򿳽��H�A�K�a</a></body></html>"
# 32117-03
Karakawei_D = "<html><body>�d�ԥd���G<br>Thank you, adventurer...<br>I can now perform the ritual.<br>(Karakawei softly chants and seems to lose consciousness.)<br>....<br>....<br>....<br>....<br>(Suddenly, his eyes open!)<br>Ah, I feel that Shilen is satisfied with the ritual!<br>Thank you, adventurer...<br>Please accept this as a token of our appreciation. I also ask that you bring back those bones of the dinosaurs from the plains so that we may continue with these rituals!</body></html>"
# 32117-04
Karakawei_E = "<html><body>�d�ԥd���G<br>���F�����ݭn<font color=\"LEVEL\">300�ӥ��쮣�s�����Y</font>�C�p�G�N���������F�ơA���λ��O�o��u�Y�����d�A�i��|����a���I�I�I<br>���I�h���y<font color=\"LEVEL\">�����s�B�����s�B�p�Y�s�B���ͮy�s</font>����A�a�^<font color=\"LEVEL\">���쮣�s�����Y300��</font>�^�ӡI�I�I</body></html>"
# 32117-05
Karakawei_F = "<html><body>�d�ԥd���G<br>�p�G���F�v���ڭ̪��f�A���X���쮣�s�����Y���ܡA�ڷ|���Ө��Ӽƶq��I�A�X�z���S�ҡC<br>�A�Q�n��ܤ���O�H<br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 1\">���X���쮣�s�����Y400�ӫ�A����u�s�@���b-�ʦL�����¥~��]60%�^�v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 2\">���X���쮣�s�����Y250�ӫ�A����u�s�@���b-�ʦL�����ª����]60%�^�v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 3\">���X���쮣�s�����Y200�ӫ�A����u�s�@���b-�ʦL�������Y�T�]60%�^�v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 4\">���X���쮣�s�����Y134�ӫ�A����u�s�@���b-�ʦL�����¤�M�]60%�^�v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 5\">���X���쮣�s�����Y134�ӫ�A����u�s�@���b-�ʦL�����¾c�]60%�^�v</a><br><a action=\"bypass -h Quest 643_RiseandFalloftheElrokiTribe 6\">���X���쮣�s�����Y287�ӫ�A����u�s�@���b-�ʦL�����²ŦL�]60%�^�v</a></body></html>"
# 32117-06
Karakawei_G = "<html><body>�d�ԥd���G<br>���F�s�@�ľ��A�ݭn�Ψ쨬�������쮣�s�����Y�C�ڭ̤��O���F�Q�q�A�ӬO���F�ͦs�~�|�i�������A�]���A��Q�P�ڭ̰Q���ٻ��C�p�G�S���T�O���T���ƶq�A���N�S���ҿת�����C<br>���֥h���y<font color=\"LEVEL\">�����s�B�����s�B�p�Y�s�B���ͮy�s</font>����A����������<font color=\"LEVEL\">���쮣�s�����Y</font>�^�ӡI�I�I</body></html>"
# 32117-08
Karakawei_H = "<html><body>�d�ԥd���G<br>�@...�O���۱i���~�Ӫ�...�p�G���_�ڭ̺رڱq�e���O�q...�N���|����o�ثݹJ...<br>�ڡA�ڡA�u�Y��...<br>�p�G�S�ƻ������}�o�̡I�I�I</body></html>"

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = [BONES_OF_A_PLAINS_DINOSAUR]

	def onAdvEvent (self,event,npc,player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

		count = st.getQuestItemsCount(BONES_OF_A_PLAINS_DINOSAUR)
		if event == "Singsing_D" :
			htmltext = Singsing_D
			st.set("cond","1")
			st.setState(State.STARTED)
			st.playSound("ItemSound.quest_accept")
		elif event == "Singsing_H" :
			htmltext = Singsing_H
			st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,-1)
			st.giveItems(57,count*1374)
		elif event == "Singsing_I" :
			htmltext = Singsing_I
			st.playSound("ItemSound.quest_finish")
			st.exitQuest(1)
		elif event == "Karakawei_D" :
			if count >= 300 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,300)
				st.rewardItems(REWARDS[st.getRandom(len(REWARDS))],5)
				htmltext = Karakawei_D
			else :
				htmltext = Karakawei_E
		elif event == "1" :
			if count >= 400 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,400)
				st.giveItems(9492,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "2" :
			if count >= 250 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,250)
				st.giveItems(9493,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "3" :
			if count >= 200 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,200)
				st.giveItems(9494,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "4" :
			if count >= 134 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,134)
				st.giveItems(9495,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "5" :
			if count >= 134 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,134)
				st.giveItems(9496,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "6" :
			if count >= 287 :
				st.takeItems(BONES_OF_A_PLAINS_DINOSAUR,287)
				st.giveItems(10115,1)
				htmltext = Karakawei_F
			else :
				htmltext = Karakawei_G
		elif event == "Singsing_A" :
			htmltext = Singsing_A
		elif event == "Singsing_B" :
			htmltext = Singsing_B
		elif event == "Singsing_C" :
			htmltext = Singsing_C
		elif event == "Singsing_D" :
			htmltext = Singsing_D
		elif event == "Singsing_E" :
			htmltext = Singsing_E
		elif event == "Singsing_F" :
			htmltext = Singsing_F
		elif event == "Singsing_G" :
			htmltext = Singsing_G
		elif event == "Singsing_H" :
			htmltext = Singsing_H
		#elif event == "Singsing_I" :
		#	htmltext = Singsing_I
		elif event == "Singsing_J" :
			htmltext = Singsing_J
		elif event == "Singsing_K" :
			htmltext = Singsing_K
		elif event == "Singsing_L" :
			htmltext = Singsing_L
		elif event == "Karakawei_A" :
			htmltext = Karakawei_A
		elif event == "Karakawei_B" :
			htmltext = Karakawei_B
		elif event == "Karakawei_C" :
			htmltext = Karakawei_C
		elif event == "Karakawei_D" :
			htmltext = Karakawei_D
		elif event == "Karakawei_E" :
			htmltext = Karakawei_E
		elif event == "Karakawei_F" :
			htmltext = Karakawei_F
		elif event == "Karakawei_G" :
			htmltext = Karakawei_G
		elif event == "Karakawei_H" :
			htmltext = Karakawei_H
		return htmltext

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st: return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		count = st.getQuestItemsCount(BONES_OF_A_PLAINS_DINOSAUR)
		if id == State.CREATED :
			if npcId == 32106 and cond == 0 :
				if player.getLevel() >= 75 :
					htmltext = Singsing_B
				else :
					htmltext = Singsing_A
					st.exitQuest(1)
		elif id == State.STARTED :
			if npcId == 32106 and cond == 1 :
				if count == 0 :
					htmltext = Singsing_F
				else :
					htmltext = Singsing_G
			elif npcId == 32117 and cond == 1 :
				if count == 0 :
					htmltext = Karakawei_A
				else :
					htmltext = Karakawei_C
		return htmltext

	def onKill (self, npc, player,isPet):
		partyMember = self.getRandomPartyMember(player,"1")
		if not partyMember: return
		st = partyMember.getQuestState(qn)
		if st :
			if st.getState() == State.STARTED :
				npcId = npc.getNpcId()
				cond = st.getInt("cond")
				count = st.getQuestItemsCount(BONES_OF_A_PLAINS_DINOSAUR)
				if cond == 1 :
					chance = DROP_CHANCE*Config.RATE_QUEST_DROP
					numItems, chance = divmod(chance,100)
					if self.getRandom(100) < chance : 
						numItems += 1
					if numItems :
						st.playSound("ItemSound.quest_itemget")
						st.giveItems(BONES_OF_A_PLAINS_DINOSAUR,int(numItems))
		return

QUEST		= Quest(643,qn,"�C���iù�@�ڪ������I�`")

QUEST.addStartNpc(32106)

QUEST.addTalkId(32106)
QUEST.addTalkId(32117)

for mob in PLAIN_DINOSAURS :
	QUEST.addKillId(mob)