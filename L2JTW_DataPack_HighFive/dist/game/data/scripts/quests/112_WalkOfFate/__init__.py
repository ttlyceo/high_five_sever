# Created by Eyerobot, edited by Emperorc
import sys
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "112_WalkOfFate"

# ~~~~~ npcId list: ~~~~~
Livina            = 30572
Karuda            = 32017
# ~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~ itemId list: ~~~~~~
EnchantD            = 956
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

class Quest (JQuest) : 

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr) 

 def onAdvEvent (self,event,npc,player) :        
    st = player.getQuestState(qn)
    if not st: return
    htmltext = event
    cond = st.getInt("cond")
    if event == "32017-02.htm" and cond == 1 :
        st.giveItems(57,22308)
        st.giveItems(EnchantD,1)
        st.addExpAndSp(112876,5774)
        st.exitQuest(False)
        st.playSound("ItemSound.quest_finish")
    elif event == "30572-02.htm" :
        st.playSound("ItemSound.quest_accept")
        st.setState(State.STARTED)
        st.set("cond","1")
    return htmltext

 def onTalk (self,npc,player):        
    htmltext = "<html><body>目前沒有執行任務，或條件不符。</body></html>"
    st = player.getQuestState(qn)
    if not st : return htmltext
    state = st.getState()
    npcId = npc.getNpcId()
    cond = st.getInt("cond")
    if state == State.COMPLETED :
        htmltext = "<html><body>這是已經完成的任務。</body></html>"
    elif state == State.CREATED :
        if npcId == Livina :
            if player.getLevel() >= 20 :
               htmltext = "30572-01.htm"
            else:
               htmltext = "30572-00.htm"
               st.exitQuest(1)
    elif state == State.STARTED :
        if npcId == Livina :
            htmltext = "30572-03.htm"
        elif npcId == Karuda :
            htmltext = "32017-01.htm"
    return htmltext

QUEST = Quest(112,qn,"命運的一步")

QUEST.addStartNpc(Livina)

QUEST.addTalkId(Livina)
QUEST.addTalkId(Karuda)