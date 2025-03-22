# pmq
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "10270_BirthOfTheSeed"

# ���ȸ��
#	10270	1	�ؤl�����L	�լd��������	�_��Ǵ��P���p�X��a���h�L���p�մ��n�D�����������ئa�Ϫ��լd�A�å�N�b�e�����Ӧa�褧�e�A���h���X�_��Ǵ��P���p�X��a���԰��k�v�����^���F�ѸԱ��C\n	0															0															-186109	242500	2550	75	0	3	�԰��k�v �����^��	0	1	1	32563	-186692	243539	2613	�S�����󭭨�	�_��Ǵ��P���p�X��a���h�L���p�մ��A���b�M��t�d���榳���������ؽլd���_�I�a�A�ӥB�ٻ����n���˾԰��k�v�����^���Ҵ��Ϊ��}�����إD�n�a�Ϫ��u���H�A�M��a�^���ҡC	0																																																																						0						0	0	0	285	0	3	57	-1000	-1001									3	41677	251602	25244	
#	10270	2	�ؤl�����L	���c���Ҿ�	�_��Ǵ��P���p�X��a���԰��k�v�����^�����D�A���F�o�즳���������ت������A���n�h���y�������ت��Ǫ��A�æ������ҡC\n\n�n�y�����ؼЩǪ�-��u �Jù�}�w���B��u �J�����w���B�J�����Ǵ�\n	3	13868	13869	13870												3	1	1	1												0	0	0	75	0	3	��������	1	1	1	32563	-186692	243539	2613	�S�����󭭨�	�_��Ǵ��P���p�X��a���h�L���p�մ��A���b�M��t�d���榳���������ؽլd���_�I�a�A�ӥB�ٻ����n���˾԰��k�v�����^���Ҵ��Ϊ��}�����إD�n�a�Ϫ��u���H�A�M��a�^���ҡC	0																																																																						0						0	0	0	285	0	3	57	-1000	-1001									3	41677	251602	25244	
#	10270	3	�ؤl�����L	�����^�����G��	�԰��k�v�����^�����O�ݭn�@�Ǯɶ��ӽլd�q�������رa�^�Ӫ����ҡC�o�Ǯɶ����ӴN�t���h�F�A�A�h��L��ͬݬݡC\n	0															0															-186109	242500	2550	75	0	3	�԰��k�v �����^��	0	1	1	32548	-186399	242412	2550	�S�����󭭨�	�_��Ǵ��P���p�X��a���h�L���p�մ��A���b�M��t�d���榳���������ؽլd���_�I�a�A�ӥB�ٻ����n���˾԰��k�v�����^���Ҵ��Ϊ��}�����إD�n�a�Ϫ��u���H�A�M��a�^���ҡC	0																																																																						0						0	0	0	285	0	3	57	-1000	-1001									3	41677	251602	25244	
#	10270	4	�ؤl�����L	�P�����̪��۹J	�_��Ǵ��P���p�X��a���԰��k�v�����^�����D�A���F�o�즳���������ا����䪺�����A���n�h����b���K���Ҫ��u�Y�����q�纸���ȡC�_��Ǵ��P���p�X��a���h�L�z�񪾹D�p���F�L���Ҧb���B�A�h��L�a�C\n	0															0															-185090	242809	1577	75	0	3	�h�L �z��	0	1	1	32563	-186692	243539	2613	�S�����󭭨�	�_��Ǵ��P���p�X��a���h�L���p�մ��A���b�M��t�d���榳���������ؽլd���_�I�a�A�ӥB�ٻ����n���˾԰��k�v�����^���Ҵ��Ϊ��}�����إD�n�a�Ϫ��u���H�A�M��a�^���ҡC	0																																																																						0						0	0	0	285	0	3	57	-1000	-1001									3	41677	251602	25244	
#	10270	5	�ؤl�����L	�������g�D	�z�L�u�Y�����q�纸���ȱo��F�Q�n�������C�^�h�V�_��Ǵ��P���p�X��a���԰��k�v�����^�����i�o�Ӥ��e�C\n	0															0															-186109	242500	2550	75	0	3	�԰��k�v �����^��	0	1	1	32563	-186692	243539	2613	�S�����󭭨�	�_��Ǵ��P���p�X��a���h�L���p�մ��A���b�M��t�d���榳���������ؽլd���_�I�a�A�ӥB�ٻ����n���˾԰��k�v�����^���Ҵ��Ϊ��}�����إD�n�a�Ϫ��u���H�A�M��a�^���ҡC	0																																																																						0						0	0	0	285	0	3	57	-1000	-1001									3	41677	251602	25244	

#NPC
NPC = 32563

class Quest (JQuest) :

	def __init__(self,id,name,descr):
		JQuest.__init__(self,id,name,descr)
		self.questItemIds = []

	def onAdvEvent (self,event,npc, player) :
		htmltext = event
		st = player.getQuestState(qn)
		if not st : return

	def onTalk (self,npc,player):
		htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
		st = player.getQuestState(qn)
		if not st : return htmltext

		npcId = npc.getNpcId()
		id = st.getState()
		cond = st.getInt("cond")

		if id == State.COMPLETED :
			if npcId == 32563 :
				htmltext = "32563-0a.htm"
		elif id == State.CREATED :
			if npcId == 32563 and cond == 0 :
				if player.getLevel() >= 75 :
					htmltext = "32563-01.htm"
					st.exitQuest(1) 
				else :
					htmltext = "32563-00.htm"
					st.exitQuest(1) 
		return htmltext

QUEST		= Quest(10270,qn,"�ؤl�����L")

QUEST.addStartNpc(NPC)

QUEST.addTalkId(NPC)
