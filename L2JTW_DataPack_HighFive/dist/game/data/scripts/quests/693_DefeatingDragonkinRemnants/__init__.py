# pmq
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "693_DefeatingDragonkinRemnants"

# ���ȸ��
# 693	1	�B�M�s�ڴݦs��	�B�M�ݦs��	�}�����ئa�Ϫ��ݦs�̺޲z��--�x�x��w��A��N�F�b����ɶ����B�M�s�ڴݦs�̪����ȡC�P�٦�̻��ߨ�O���Ĳv�a�����ݦs�̤���A�b����ɶ����}�a����J�f���˸m�C\n\n�n�y�����ؼЩǪ�-�ݱѭx �x�Ϊ��B�ݱѭx ��1�������B�ݱѭx ���s�����B�ݱѭx �B�L�B�ݱѭx �]�k�����B�ݱѭx �]�k�v�B�ݱѭx �]�k�h�L�B�ݱѭx �v���v�B�ݱѭx �кj�L\n	0															0															0	0	0	75	0	0	�}�����J�f	1	1	1	32527	-248525	250048	4307	�S�����󭭨�	�h�L�ɴ����x�x��w�紿�O�ө��۪��x�H�A�ɥ�����h�X�F�Գ��A�ثe���b�t�d�޲z�ݦs�̪�¾�ȡC�ѩ�L���w���гo�ӥ��ȡA��O���X�F�t������ĳ�C���ӫ�ĳ�N�O�n�P�s�ڴݦs�̹��...	0																																																																						0						0	0	0	285	1	1	-1002											1	0											

# NPC
Edric = 32527  # �x�x ��w��

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st: return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond") 

		if id == State.CREATED :
			if npcId == Edric and cond == 0 :
				if player.getLevel() >= 75 :
					htmltext = "32527-01.htm"
					st.exitQuest(1)
				else :
					htmltext = "<html><body><br><center><font color=\"FF0000\">�]���ȩ|����ˡI�^</font></center></body></html>"
					st.exitQuest(1)
		return htmltext

QUEST		= Quest(693,qn,"�B�M�s�ڴݦs��")

QUEST.addStartNpc(Edric)

QUEST.addTalkId(Edric)