# Made by BiTi! v0.2
# v0.2.1 by DrLecter
import sys
from com.l2jserver import Config
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest

qn = "637_ThroughOnceMore"

#Drop rate
DROP_CHANCE=90
#Npc
FLAURON = 32010
#Items
VISITOR_MARK,FADEDMARK,NECROHEART,MARK = 8064,8065,8066,8067

class Quest (JQuest) :

 def __init__(self,id,name,descr):
     JQuest.__init__(self,id,name,descr)
     self.questItemIds = [NECROHEART]

 def onAdvEvent (self,event,npc, player) :
    htmltext = event
    st = player.getQuestState(qn)
    if not st : return
    if htmltext == "32010-03.htm" :
       st.set("cond","1")
       st.setState(State.STARTED)
       st.playSound("ItemSound.quest_accept")
    elif event == "32010-10.htm" :
       st.exitQuest(1)
    return htmltext

 def onTalk (self, npc, player):
   htmltext = "<html><body>目前沒有執行任務，或條件不符。</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext

   id = st.getState()
   cond = st.getInt("cond")
   if id == State.CREATED :
      if player.getLevel()>72 and st.getQuestItemsCount(FADEDMARK) :
         htmltext = "32010-02.htm"
      elif player.getLevel()>72 and st.getQuestItemsCount(VISITOR_MARK) :
         htmltext = "32010-01a.htm"
         st.exitQuest(1)
      elif player.getLevel()> 72 and st.getQuestItemsCount(MARK) :
         htmltext = "32010-0.htm"
         st.exitQuest(1)
      else:
         htmltext = "32010-01.htm"
         st.exitQuest(1)
   elif id == State.STARTED :
       if cond == 2 and st.getQuestItemsCount(NECROHEART)==10:
          htmltext = "32010-05.htm"
          st.takeItems(NECROHEART,10)
          st.takeItems(FADEDMARK,1)
          st.giveItems(MARK,1)
          st.giveItems(8273,10)
          st.exitQuest(1)
          st.playSound("ItemSound.quest_finish")
       else :
          htmltext = "32010-04.htm"
   return htmltext

 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if st :
     if st.getState() == State.STARTED :
       count = st.getQuestItemsCount(NECROHEART)
       if count < 10 :
          chance = DROP_CHANCE * Config.RATE_QUEST_DROP
          numItems, chance = divmod(int(chance),100)
          if st.getRandom(100) < chance : 
             numItems += 1
          if numItems :
             if count + numItems >= 10 :
                numItems = 10 - count
                st.playSound("ItemSound.quest_middle")
                st.set("cond","2")
             else:
                st.playSound("ItemSound.quest_itemget")
             st.giveItems(NECROHEART,int(numItems))
   return

QUEST       = Quest(637,qn,"再次往那門扉之後")

QUEST.addStartNpc(FLAURON)

QUEST.addTalkId(FLAURON)

for mob in range(21565,21568):
    QUEST.addKillId(mob)