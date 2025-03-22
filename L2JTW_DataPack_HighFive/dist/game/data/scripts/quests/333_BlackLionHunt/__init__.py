#written by Rolarga
##################################FEEL FREE TO CHANGE IDs, REWARDS, PRICES, NPCs AND DROPDATAS THEY ARE JUST CUSTOM BY ME##################################

qn = "333_BlackLionHunt"

#Technical relatet Items
BLACK_LION_MARK = 1369
ADENA_ID = 57

#Drops & Rewards
CARGO_BOX1,CARGO_BOX2,CARGO_BOX3,CARGO_BOX4 = range(3440,3444)
UNDEAD_ASH,BLOODY_AXE_INSIGNIAS,DELU_FANG,STAKATO_TALONS = range(3848,3852)
SOPHIAS_LETTER1,SOPHIAS_LETTER2,SOPHIAS_LETTER3,SOPHIAS_LETTER4,LIONS_CLAW,LIONS_EYE,GUILD_COIN = range(3671,3678)
ALACRITY_POTION = 735
SCROLL_ESCAPE = 736
SOULSHOT_D = 1463
SPIRITSHOT_D = 2510
HEALING_POTION=1061
#Box rewards
GLUDIO_APPLE,CORN_MEAL,WOLF_PELTS,MONNSTONE,GLUDIO_WEETS_FLOWER,SPIDERSILK_ROPE,ALEXANDRIT,              \
SILVER_TEA,GOLEM_PART,FIRE_EMERALD,SILK_FROCK,PORCELAN_URN,IMPERIAL_DIAMOND,STATUE_SHILIEN_HEAD,         \
STATUE_SHILIEN_TORSO,STATUE_SHILIEN_ARM,STATUE_SHILIEN_LEG,COMPLETE_STATUE,FRAGMENT_ANCIENT_TABLE1,      \
FRAGMENT_ANCIENT_TABLE2,FRAGMENT_ANCIENT_TABLE3,FRAGMENT_ANCIENT_TABLE4,COMPLETE_TABLET = range(3444,3467)

#Price to Open a Box
OPEN_BOX_PRICE=650


#Lists
#List of all NPCs this Quest: Sophya,Redfoot,Rupio,Undinas(Shilien Temple),Lockirin(Dwarfen Village)
NPC=[30735,30736,30471,30130,30531,30737]
#List for some Item Groups
statue_list=[STATUE_SHILIEN_HEAD,STATUE_SHILIEN_TORSO,STATUE_SHILIEN_ARM,STATUE_SHILIEN_LEG]
tablet_list=[FRAGMENT_ANCIENT_TABLE1,FRAGMENT_ANCIENT_TABLE2,FRAGMENT_ANCIENT_TABLE3,FRAGMENT_ANCIENT_TABLE4]

#This Handels the Drop Datas npcId:[part,allowToDrop,ChanceForPartItem,ChanceForBox,PartItem]
#--Part, the Quest has 4 Parts 1=Execution Ground, 2=Partisan Hideaway 3=Near Giran Town, Delu Lizzards 4=Cruma Tower Area.
#--AllowToDrop --> if you will that the mob can drop, set allowToDrop==1. This is because not all mobs are really like official.
#--ChanceForPartItem --> set the dropchance for Ash in % for the mob with the npcId in same Line.
#--ChanceForBox --> set the dropchance for Boxes in % to the mob with the npcId in same Line. 
#--PartItem --> this defines wich Item should this Mob drop, because 4 Parts.. 4 Different Items.
DROPLIST={
#Execturion Ground - Part 1
20160:[1,1,67,29,UNDEAD_ASH],      #Neer Crawler
20171:[1,1,76,31,UNDEAD_ASH],      #Specter
20197:[1,1,89,25,UNDEAD_ASH],      #Sorrow Maiden
20200:[1,1,60,28,UNDEAD_ASH],      #Strain  
20201:[1,1,70,29,UNDEAD_ASH],      #Ghoul
20202:[1,0,60,24,UNDEAD_ASH],      #Dead Seeker (not official Monster for this Quest)
20198:[1,1,60,35,UNDEAD_ASH],      #Neer Ghoul Berserker
#Partisan Hideaway - Part 2
20207:[2,1,69,29,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Guerilla
20208:[2,1,67,32,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Raider
20209:[2,1,62,33,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Marksman
20210:[2,1,78,23,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Sergeant
20211:[2,1,71,22,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Captain
#Delu Lizzardmans near Giran - Part 3
20251:[3,1,70,30,DELU_FANG],        #Delu Lizardman
20252:[3,1,67,28,DELU_FANG],        #Delu Lizardman Scout
20253:[3,1,65,26,DELU_FANG],        #Delu Lizardman Warrior
20781:[3,0,69,31,DELU_FANG],        #Delu Lizardman Shaman (not official Monster for this Quest)
#Cruma Area - Part 4
20157:[4,1,66,32,STAKATO_TALONS],    #Marsh Stakato
20230:[4,1,68,26,STAKATO_TALONS],    #Marsh Stakato Worker
20232:[4,1,67,28,STAKATO_TALONS],    #Marsh Stakato Soldier
20234:[4,1,69,32,STAKATO_TALONS]    #Marsh Stakato Drone
}

######################################## DO NOT MODIFY BELOW THIS LINE ####################################################################################

#Messages
#technical relatet messages
html        = "<html><body>"
htmlend        = "</body></html>"
back        = "<a action=\"bypass -h Quest 333_BlackLionHunt f_more_help\">��^</a>"
#Sophya
sophia        = "�ħL���������:<br>"
#-Item information
p_redfoot      = html+sophia+"�p�w��...�ڭӤH��L�S������n�P�A���p�G�S���o�ӤH�Nı�o�D�`�i���C�L��¾�d�O�ǹF�x�Ϋ~���t�d�H�A���]�O�B�z����⪺�ԧQ�~���B�������C�ӥB�٬O�ڭ̶ħL�Ϊ��������C�L�����ܦh���Ϊ������A���ɧA�]�i�H�h�ݰݡC<br><a action=\"bypass -h Quest 333_BlackLionHunt p_trader_info\">�߰�����ӤH���|���Ʃy</a><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤������</a>"+htmlend
p_no_items      = html+sophia+"�·�S�̰ڡA�A�����ӬO�b�o�ӧ����ӬO�n�b�]���̾���Q���Գ��a�I<br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤������</a>"+htmlend
p_trader_info    = html+sophia+"�o�c�l���T�O�ȤB�ӷ~�P�����f���C�ݦL�b�c�l�W���L���N�i�H���D�C�p�G�Q��f�c�ٵ��L�̡A�N�h�����]�k���f�ө������|�|�����ڡC�L�O���ȤB�ӷ~�p�����ƪ��H�C <br><a action=\"bypass -h Quest 333_BlackLionHunt p_redfoot\">�߰�����p�w�����Ʃy</a><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤����</a>"+htmlend
p_both_info      = html+sophia+"�S�̡A���F�������ȡA���W�A�F�C�ڷ|�ھڧA�a�^�Ӫ����Ҽƶq��I���S�C<br>���L�A�o�c�l�O...�H�ݨӬO��^�F�ӤH���|��<font color=\"LEVEL\">�f���c�l</font>�C�ڭ̪������W�S�������^�f���c�l�����e�A�ҥH�S���q�ȧ�c�l�ٵ��ӤH�̡C���O�p�G�ٵ��ӤH���|�A�]�\�|�����S�������a�H<br>���p���Q���ӤH�̡A���N�h�����p�w���a�C�L�O�M���B�z����⪺�ԧQ�~���M�a�C<br><a action=\"bypass -h Quest 333_BlackLionHunt p_redfoot\">�߰�����p�w�����Ʃy </a><br><a action=\"bypass -h Quest 333_BlackLionHunt p_trader_info\">�߰�����ӤH���|���Ʃy</a><br> <a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤������</a>"+htmlend
p_only_item_info  = html+sophia+"�S�̡A���F�������ȡA���W�A�F�C�ڷ|�ھڧA�a�^�Ӫ����Ҽƶq��I���S�C<br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤������</a>"+htmlend
p_leave_mission    = html+sophia+"�o�q�ɶ����W�A�F�C�N��O��l�]�ݭn�𮧡C�b�����𮧡A�ɥR��q�a�C�����ħL�A�ަn�ۤv����O�O�򥻭n�D�C<br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">���Q�n����s����</a><br><a action=\"bypass -h Quest 333_BlackLionHunt r_exit\">�h�X�ħL��</a>"+htmlend
p_only_box_info    = html+sophia+"�S�̡A���F�������ȡA���W�A�F�C�ڷ|�ھڧA�a�^�Ӫ����Ҽƶq��I���S�C<br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">�������椤������</a>"+htmlend
p_first_eye      = html+sophia+"�еy���@�U�C�ڵ��A<font color=\"LEVEL\">��l����</font>�мm�C�o�O�@�������e�A�b�Գ��W�ҥߪ��ԥ\�C�t�~�o�����o���A���s���ɵ��~�C�O�԰��ɫܦ��Ϊ����ӫ~�A�n�n�n���áI����A�Ʊ椵��]���~��V�O�o��n���G�C"+htmlend
p_eye        = html+sophia+"�еy���@�U�C�ڵ��A<font color=\"LEVEL\">��l����</font>�мm�C�o�O�@�������e�A�b�Գ��W�ҥߪ��ԥ\�C�t�~�o�����o���A���s���ɵ��~�C�O�԰��ɫܦ��Ϊ����ӫ~�A�n�n�n���áI����A�Ʊ椵��]���~��V�O�o��n���G�C"+htmlend
#-exit messages
r_exit        = html+sophia+"�A���Q�n�h�X�·�ħL�ΡH��M�C�ӤH�����ۤv���Q�k�A�ڤ]���|�h�ݲz��...���O���@�I�A�n����...���A�o�ˬy�ۦn�Ԥ��媺�H�A�ħL�άO�ߤ@����ܡC�N��A�h�F�䥦�a��A�̲פ]�@�w�|�^��Գ��C<br>�`���A�p�G�A�@�w�n���}�ħL�ΡA�N�n���D�o��ơC�u�n�A�@�h�X���ܡA�N���A�O�·઺�ħL�F�A�]�����ȭn�k�ٶ·઺�лx�A�ӥB�]����A�ϥΧA�b�o�q�����H�·઺�ħL�����ҧQ�Ϊ��Ҧ��u�f�C��p���������F�f���c�l�B�u�Y�J���B�j�N�H�g���H������ұo�쪺���S�������u�f�A�O����A�ϥΪ��C�Y�Q�A�ϥγo���u�f���ܡA�o���s����·઺�лx�A�ҥH�A�V���Ҽ{�ݬݧa�C<br>�ڡA�٦��ھڧA�o�q���������Z�A�h����٬O�|�ӥI���A���C<br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">�~�򬰶ħL�ΰ���</a><br><a action=\"bypass -h Quest 333_BlackLionHunt exit\">�T�w�h�X�ħL��</a>"+htmlend
exit        = html+sophia+"�p�G�A���N�ӳo���M�A�ڤ]�N�����d�A�F�C�����·઺�лx��X�ӧa�C�i���ڭ̤������Ԥ����Y�]�즹����F�C�ڡA���}���e�Ч�o�Ӧ��U�C�o�O�A�b�ħL�ΥߤU�\�Z�����S�C�N��@�O����}�l�s�ͬ��������a�C����A�Ʊ�U���A�êӧ@�ԡA�A���C"+htmlend
#-Start
start_error1    = html+sophia+"���e�]���L�A�ڭ̥ثe�����ȬO��o�P�䪺�]���������C���O�ثe�ħL�Ϊ��D�O�Q������j�|�B�A�ҥH�L�O�譱�D�`�����C���h�]�u�ਾ���]����ŧ�������Ӥw�C�p�G�{�b���@���äj�n�Ԫ��å�̡A�u�Q���W���ΥL�̨ӸɥR�L�O...�I<br>(�u������25�H�W�ño��u�·઺�лx�v������~�i�H���檺���ȡC)"+htmlend
start_error2    = html+sophia+"���e�]���L�A�ڭ̥ثe�����ȬO��o�P�䪺�]���������C���O�ثe�ħL�Ϊ��D�O�Q������j�|�B�A�ҥH�L�O�譱�D�`�����C���h�]�u�ਾ���]����ŧ�������Ӥw�C�p�G�{�b���@���äj�n�Ԫ��å�̡A�u�Q���W���ΥL�̨ӸɥR�L�O...�I<br>�ݨӧA�n�����ܦh�P�]���̾԰����g��C�H�A�o��{�ת��ޭǡA���H�����ڭ̶ħL�Ϊ��@��...���W�h�W�A�p�G�Q�����ħL�Ϊ��@���A�N�����n�q�L�Y�ظզ͡C�p�G������A�N�h���@�U<font color=\"LEVEL\">�j�|�B�������p�ڪi���w</font>�����C�o��L���{�P�ña�^�·઺�лx�A�ڭ̴N�|���A���S�̨õ��A�M�ڭ̦@�P�԰������|�C<br>(�u������25�H�W�ño��u�·઺�лx�v������~�i�H���檺���ȡC)"+htmlend
start_start      = html+sophia+"�·�ħL�ΥS�̡̭A�ثe�ڭ̪����p�O�p���C�p���ҬҪ��A�ڭ̪����ȬO��o�P�䪺�]���������C���O�]���ħL�ΥD�O�����Q������j�|�B�A�ҥH�����]����ڤW���i��F�C���h�O�ਾ���]����ŧ�������Ӥw�C <br>���n�j�|�B���p�ڪi���w�������ӤF�R��ު��ħL�ΥS�̡A�ҥH���Ӱ��W�i�H�V�]���̪���a�o�ʧ����F�C�S�̰ڡA�Ʊ�A�]�ѥ[�o���Ԫ��C<br><a action=\"bypass -h Quest 333_BlackLionHunt start\">�����ѥ[�Ԫ�</a>"+htmlend
start_explain    = html+sophia+"�ܦn�I�I���F�@�q�ɶ����·�̡A�N�n�i���R�������s�}�l�M���y���F�I<br>�{�b�}�l�����@�U�Ԫp�C�ثe�ڭ̭n�𲤪��a�I��4�B�A�N�O�D���B�����ˮھڦa�B�n�������a�ϡB�٦��J�|���h�A�a�C�ثe�ڭ��٨S���M�]���̥�����W����O�A�ҥH�ڭ̭n���U�a�����H�ּƧL�O�c�����������A�δ����Ԫ��覡�����]���̡C<br><a action=\"bypass -h Quest 333_BlackLionHunt start_parts\">ť���U�a�Ϫ��԰�����</a>"+htmlend
start_parts      = html+sophia+"�Q�n���D�������ȡH<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p1_explanation\">�����b�D���W�������ͪ�</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p2_explanation\">�����b�����ˮھڦa�W���[�T</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p3_explanation\">�����b�n������a�Ϫ��w�|�h簤H</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p4_explanation\">�����b�J�|���h�A�a���h�A�q��d��</a>"+htmlend
start_ask_again    = html+sophia+"�·�S�̰ڡA�M�]���̪���Ԥw�g�}�l�F�I�b�o���԰����A�A�]���Ӫ�{�@�U�a�H<br><a action=\"bypass -h Quest 333_BlackLionHunt start_parts\">ť�����Ȼ���</a>"+htmlend
start_continue    = html+sophia+"�����Գ������ĤH�A�~���@�U�ӧQ���ַP�a�I"+htmlend
#-Part 1
p1_explanation    = html+sophia+"�����F�䪺�D���O�޻�d�s�n���������ˤ��a�C���ȴN�O�������̪������ͪ��̡C�ڻ��O�b�A���x�q�îɴ��A�ަ����H�̬��F���_�Ӵ_�ͪ������ͪ�...���M�A�ڭ̥u�ާ����ۤv�����ȴN�i�H�F�A���Pı�٬O���I��򪺡C <br><a action=\"bypass -h Quest 333_BlackLionHunt p1_t\">��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">ť���䥦�����Ȼ���</a>"+htmlend
p1_take        = html+sophia+"�n�����������ͪ���<font color=\"LEVEL\">���F�I�M�B�ջ�B���ǿ����B���ǿ������p�J�B���F�B�٦����Ͱ�</font>�C�����A�夣��o�A�����ͪ��Q�����ɷ|�Ʀ��@��ǡA�⨺�ǦǷ�@�O�ӧQ�����ұa�^�ӡC�N�|�ھکұa�^�Ӫ�<font color=\"LEVEL\">�����ͪ�����</font>��I���S�C�A���b�p�ڪi���w������U���L�ơA�����ҩM���S���W�w���Ӥw�g�M���F�a�H  <br> ���򻰺򰵦n�԰��ǳơA�V�D���X�o�a�C�@�w�n�V�Ҧ��H�ҩ��A�Y�ϬO�Һ������_�ͪ��`�F�A�]���O�ڭ̶·�ħL�Ϊ����I"+htmlend
#-Part 2
p2_explanation    = html+sophia+"���ȴN�O�����n�Ϧb��_�䰨�ᨦ����Ǧ�ȭx���C����Q���O��´ݦs�̪��Q�X�����C���O�c�W�L������{�g�D�����d�a�⪺��{�����Ԫ��[�T�C�e�̵��藍�O����e����I���C<br><a action=\"bypass -h Quest 333_BlackLionHunt p2_t\">��������</a> <br> <a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">ť���䥦�����Ȼ���</a>"+htmlend
p2_take        = html+sophia+"�A�n�������ĤH��<font color=\"LEVEL\">�[�T�������B�[�T�����L�B�[�T�����L�B�[�T�ƶ����A�٦��[�T����</font>�C<br>�@�������ĤH�����ұa�^���������лx�A<font color=\"LEVEL\">��{��������</font>�C�N�|�ھڱa�^�Ӫ����Ҽƶq��I���S�C�A���b�p�ڪi���w������U���L�ơA�����ҩM���S���W�w���Ӥw�g�M���F�a�H<br>���򻰺�V�����ˮھڦa�X�o�a�C�����ǵL�k�L�Ѫ��[�T�A�@�@�ڭ̶·�ħL�Ϊ�����I"+htmlend
#-Part 3
p3_explanation    = html+sophia+"�w�|�h簤H����a��ӬO�b�_���n��������C���O�̪񦳫ܦh�I�J�f����a�C���M�٤����D�e�̥u�O���F�Q�������A�٬O���F�i��j�W�Ҫ��i��ǳơA���i�H�T�w���O�e�̽T��O�]���Y�ӥت��Ӧb��ʡC�ڭ̪����ȴN�O�A�����e�̪��C�ӳ����A���L�̨㦳���߷P�A�åB�����L�̦b�o����n�ϤU�ӡC<br><a action=\"bypass -h Quest 333_BlackLionHunt p3_t\">��������</a> <br> <a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">ť���䥦�����Ȼ���</a>"+htmlend
p3_take        = html+sophia+"�A�n�������å릳<font color=\"LEVEL\">�w�|�h簤H�B�w�|�h簤H���u�B�٦��w�|�h簤H�Ԥh</font>�C�@�������ĤH���Ҩ�a�^<font color=\"LEVEL\">�w�|�h簤H����</font>�C���O�n�p�ߡC�e�̤�j�|�B����L�کήԧJ�ڻh簤H��[���r�n�ԡC<br>�N�|�ھڱa�^�Ӫ����Ҽƶq��I���S�C�A���b�p�ڪi���w������U���L�ơA�����ҩM���S���W�w���Ӥw�g�M���F�a�H <br>����A�{�b�N�V�Գ��X�o�a�C�h�����������Ǥ����Ѱ��a�p���h簤H�I"+htmlend
#-Part 4
p4_explanation    = html+sophia+"���ȴN�O��I�b�J�|���h�A�a�s�@�u�q��d�ݡv���_�Ǫ��]���C�A�����L�q��d�ݶܡH�e�̬O���o�����Τ@�ˡA�O�ϤH�P�칽�c���رڡC�e�̪�����]�q�b��w���Ҵ߻q�A�Ӥ⪢�y���۾W�Q�����l�C�ӥB�ʧ@�D�`�a�֡C�O����p�ݪ��å�C <br>�A�[�W�h�A�a�����j����λj��A�٦��ܦh�r�ަb���H����P�䪺�]���̡A�O�ӫ���������Ȫ��M�I�a�a�C<br><a action=\"bypass -h Quest 333_BlackLionHunt p4_t\">��������</a><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">ť���䥦�����Ȼ���</a>"+htmlend
p4_take        = html+sophia+"�A�n��I���ĤH��<font color=\"LEVEL\">�h�A�q��d�ݡB�h�A�q��d�ݤu�H�B�h�A�q��d�ݤh�L�B�٦����ʪh�A�q��d��</font>�C�@���ӧQ�����ұa�^�q��d�ݪ����C�N�p�H�����W�w�A�|�ھڧA�a�^�Ӫ����Ҽƶq��I���S�C <br>���򻰺򰵦n�԰��ǳơA�V�J�|���h�A�a�X�o�a�C�Ǧ����|���q��d�ݭ̪��D�ڭ̶·�ħL�Ϊ��F�`�I"+htmlend
#Redfoot
redfoot        = "�ħL�p�w��:<br>"
f_no_box      = html+redfoot+"�ޡI�S�̡I�A���{�b���b������ȬO�a�H���W�A�F�I������n���������Ʊ��ܡH<br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">�߰ݬO�_���i�Ϊ���T</a>"+htmlend
f_give_box      = html+redfoot+"�ޡI�S�̡I�A���{�b���b������ȬO�a�H���W�A�F�I������n���������Ʊ��ܡH<br>�c�l...�H�@�A��ӬO�ӤH�̪��f���c�l�ڡC����ڳo�̨ӬO���...�A�S���Q��c�l�ٵ��ӤH�̪��N��O�a�H�n�A���ڨ����A�}�o�c�l�C��M�c�l�̭����F������k�A�C���ڭn�����@�I��!�S�ҡC<font color=\"LEVEL\">650����</font>�N�t���h�F�C�N��@�O���}�c�l�����S�A�٦��[�W�u���K�����S�C<br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">�ШD���}�c�l</a><br>"+back+htmlend
f_rnd_list      = ["�e�X�ѰݹL�q�j�|�B�����^�Ӫ��T���ӤH�A�L�̻��̪����^�۷��I�Cť���[�T�ݦs�̪�����൥�۫I�����������|�A�ӥB�_��g��J�~�H�`�`�v�汰��...<br>ť���j�|�B����ĵ�æ㺸�˫��A���b�ߵJ�a��ۦ����ƪ��ħL...<br>",
             "�ݹL�s���^�n�������F��ܡH�O�i�s�񭵼֪����_���_�ۡCť���s�����֥��K���G�H�t�d�s�@���Ӧ^�n�����Cť���b�o�f������]���@��...<br>���L�n�s�@�^�n�������ܡA�N�ݭn�S�O�����СC�����гo�����F��A���쭵�֮a�N��o��a�H�N�O���ں��ڧ��ήR�R�L�o�˪��H��...<br>",
             "�o�ӧ������@�W�ڷQ��������̰��żp�v���~���H�C�L�s�������A�̪��W�ۭn�ѥ[�i���j�ɡA���b�ǳƷ��O�Cť���L���b�M�������L�����öQ�i�����ƪ��_�I�a...<br>",
             "ť�L�����ƺC���𪺶ǻ��ܡH�����Φb�𳻼Ӫ��ӫҤڷŪ��ƩO�H<br>�A�]���D�A�]���ѯ��ʦL�F�ڷšA�ҥH�֤]����i�h�𳻼ӡC���O�ھڳ̪�ť�쪺�ǻD�A���H���D�F�p��i�h���ж�����k�Cť���O�ȤB�����·t���F�Юv...<br>",
             "�A����h�]�Ǳo�ߦa�϶ܡH���ڴN�i�D�A�X�ӹ�ħL�����U�������a�I<br>�p�G�h���W�����������A�h���ӤH����۩�ĵ�íe����I�C���ӯ�o���ٺ⤣�������ȡC��F�A�٦�ť�����ӦW�s��ֵ�����K�h�Q�]���b��ħL�C<br>",
             "�p�G�A�O�Q�X�i����դO���g�D�A�ڷ|���A�@�ӧA�|�P���쪺��T�C�U�a����̪��I�᳣���䴩�L�̪��Q�ڡC�N�O�_�������J���������w���̭�B�٦��ڷ竰���j���F�ҨȤӪk�S��C��M�A���ǤH�]���O�O�����c���H�A���U������ӷ|���ҭn�D�a�H<br>",
             "�o�O���[�e�M�·t���F���|���H�̲�Ѫ��ɭ�ť�쪺����...ť���·t���F�ѩ^�u�Y�k���H����H�j�a�����D�ڡH�ڥi�O�Ĥ@��ť��...<br>���M�R���`�k��...�ڬO�u�������z�ѡC���O�q�h�L�·t���F�˪L���H�̨���ť���A�·t���F�̫سy���u�Y�����T��O�D�`�����Cť����b�����̪��`�W���q�̥������b�U�a�o�{���u�Y�k�����J���H<br>",
             "���[�e�ڰ�ť�F�K�K�E�X�ӸG�H���͸�...�G�H������A���ӬO�s�����Ѥ������a�H�`���A�L�ݰ_�ӫܫ�ۭn�b�M��O���ۥ��H�̶H�Τ�r����ѡC���M�ڨSť�M���A���n���O�O�������󥨤H�̬�ޤ譱�����j���K�C�ڤ@���H���G�H�u�O�����K�K�E�Ϊ̬ݦu�ܮw�����ơA�S�Q��t�a���ٷd�X�o��h��˨ӡC<br>",
             "ť���L���s�S���H�q���s�έ��s���Z����ƥX�Ӫ��i�R���p�s�Cť���d���޲z�������H���D�p���o���s�i���d���s�Ӿi...�n���s�w�ġC�p�G�A�]�Q�i���s���ܥh���@�����ӤH�a�I<br>",
             "�o�O���[�eť�쪺�����Ať�����ӥs���򦬶��j�N�ɹ���������´�C��}�l�٥H���O�b�������Ǥ��ȿ����������A��Ӥ~���D���ǩҦ������ɹ����ȫD�`���C�ӥBť���|���̫D�`�n���A�p�G�����F�öQ���ɹ��^�ӥL�̷|�����A���������~�O�H�L�̻��p�G�Q�[�J�L�̪��ɹ������|�A�N�n�h���y�H�������G�H���L�S�C<br>",
             "ť���ڷ窺�H������񦳭��F�l�Ҫ��N�v�C�L��B���L��s�y�X����A��{�@�檺�]�k�Ĥ�...�n�h�H���W�F�o���Ĥ�����C���_�Ǫ��O�A�����u�������{�@��C�C���D�O�u���u���u�����v�|�o��...<br>",
             "�N�I�a��@�I�C�ڷ|���A�ܦn����T�C�o�O�q�ӤH�̪��͸ܷ���ť�쪺�A���[�e�A�q�_�ɰe���f�����ȤB�ӷ~�P�����f�������A���ӶQ�����~�Q���F�C�O�s�ӫ��p�۪��_�ۡA�n���������Ȭ۷���H�Cť���O�Φb�˹��ӫҪ����a�W���_�ۡA���Ӥ��O���q�Q�������~�a�H�u�Q�ݤ@��~<br>",
             "ť������S���Hť���I�Φb�s�������a�s�w��紵���L�ӤF�C�o�i�j�Ƥ����F...�U�@�w��紵�q�_�ޤ��X�Ө�B�}�a�A�_�ɤ@�a�����N�|�ܦ��o�V...<br>���t�@�譱�]���H���b�۶��Q��w��紵���H���Cť���n���O�_�ɫ����s�[���̺����k�l�C���O�L�̯u���{���P�s��Է|���Ӻ��...�H�����٬O����I<br>",
             "ť���b�_�ɫ����@�W���F������W�ۤv�H�ͪ��C�~�C�H�̳��{�����ȱo�A���O�L���F�˦۱����a�s�w��紵�A�C�Ѧb�s�y�S�s���}�b�Cť��������L�����s�y�}�b�����ơA�L�N�|�����֪����S�C�����쪺�ܥh�����a�C�O�b�_�ɫ����ĵ�çL���s�k���S�ͪ��~���H�C<br>",
             "���A�o�˨�B�ȹC���B�͡A�ڵ��A�@���ܦ��Ϊ���T�C�o�Ӥ��ꪺ�ӤH�̫��W�w�O�����o�Ǧ��ө����C���O���ǰӤH�����W�w�o�M���k���{���ͷN�C��ù�����������f�ӤH���աA�٦��b�·t���F�˪L���䰵�ͷN���S�´��N�O�o�˪��H�C���O���F�ȿ����M�M�o�ǰ��ͷN...���M���O�ӤH�A���]���S�ƤF�C<br>",
             "���A���Ф@���t�ƫ��ˡH�u�ۥj�|�B��_��V���|�J��s�ּگS���A�ҡA�L���F�����ۤv�A�����񪺤g��J�~�H���b���ζħL...�H�A����O��I�g��J�~�H���Ӻ�靈�l�a�H<br>���O�A�A���S��ť���L���Ӧa��g�`�o�{�j�N�Ұ�򪫪��ǻD�Hť�����ɭԷ�����g��J�~�H�ɰ����|�o�{�Q�����򪫡C<br>",
             "ť���L�ȤB�ӷ~�P���ܡH���O�H���ӤH�̪���´�C�H���ݨ�G�H�ӤH�M�ܮw�޲z���̦���´�ʪ����ʨ��ȤF���֧Q�q�A�ۤv�]�N�Q�ҥ�_�ӤF�C���O�ڻ{���A�G�H���ͷN�����ƬO�ѥͪ��A�H���O���ˤ]�L�k�Ǳo��C<br>�u�O���W�[���A�]����ŧ���ȤB�ӷ~�P�����f���𦸷m���f���A�ҥH�{�b�l���G���C<br>",
             "�A���b�i���s�ܡH�ڬO���i���d�����p�s�Cť�����Ӥ�k�i�H�⨺�Ӥp�s�i����󪺮y�s�O�I���M�ڤ]���M���A��ť���y�H��������̧J���մ����D�ԲӪ����e�C�Y�P���쪺�ܡA�h���ݧa�I<br>",
             "�Ať�L������ù���������ƶܡH�O�Ӵ���D�`�u��������...���O�]���Q�٬��O�Ǹo�̻E�~�������A�ҥH�H�̤��Q�h���̡C���Lť���]��ƥ��L���A�ҥH�٬O�Ӥ������a��C<br>�`���Ať���̪����f�ө��զb��ħL�C������ݭn�����h�����H�H���p�����쪺�ܡA�N�h��ù�������ݬݧa�H",
             "�A�h�L���žǰ|�ܡH��˩O�Hť���R���������g�H�̶��Φ�b���̡B���ť��ӬO�������c�]���A���ܦh�o�˪��ǻD...�H�ӥB���O���n���ǻD...<br>�`���A�ھڳ̪�ť�쪺�����Ať����b���̪��]�k�ӤH�ɰ����b�䦳��O���]�k�v�C���D�O����Ҷ��]�k�v�A��L�̬~����A�i�����F�N�v���ζܡH<br>",
             ]
f_no_news      = html+redfoot+"�藍�_�A�{�b�٨S���s����T�C�U���A���{�a�C<br>"+back+htmlend
f_more_help      = html+redfoot+"�٦��Ʊ��n�������ܡH<br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">�ШD���}�c�l</a>"+htmlend
f_no_more_box    = html+redfoot+"�o���O�s�߬����ڶܡH�S���f�c�A�٭n�ڥ��}�H<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">�߰ݬO�_���i�Ϊ���T</a>"+htmlend
f_more_help2    = html+redfoot+"�٦��Ʊ��n�������ܡH<br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">�ШD���}�c�l</a><br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">�߰ݬO�_���i�Ϊ���T</a>"+htmlend
f_not_adena      = html+redfoot+"�ޡI�ѥS�ݨӧA�����I�S�ҰڡG�ǳƦn650�����A�ӧa�C<br>"+back+htmlend
#Rupio
rupio        = "�K�K�|�ֶ�:<br>"
r_no_items      = html+rupio+"�A���O�·�ħL�ܡH�ӧڭ̪��K�E������O...�H�O�өe�U�s�y�Z�����ܡH"+htmlend
r_items        = html+rupio+"������Ʊ��n���������ܡH<br><a action=\"bypass -h Quest 333_BlackLionHunt r_give_statue\">�n�D�զX�J�����H��</a><br><a action=\"bypass -h Quest 333_BlackLionHunt r_give_tablet\">�n�D�զX�H�g�����H��"+htmlend
r_statue_pieces    = html+rupio+"�A��򪾹D�ڪ�����O�_��򪫰ڡH���O�p�G�Q��۹���_����Ӫ��ˤl�A�N����ʤ֨䤤����@���A�A���O���O�H��p���Q�����k�������N�O�n��<font color=\"LEVEL\">�Y ���� �u�٦��L</font>)�C�ӳ���ܡH"+htmlend
r_statue_brockes  = html+rupio+"�����ڨӨq�@�U�ڪ������a...�H����...��L���T�w�b�x�l�W... �A�⨭��K�W�h...���Y�M���u���������X�I���n�A�@�զX����...�V�|�I�J���}�H�F�C���M�ڦ����D�J�����¡A�ҥH�i��ܯܮz... �ڥu�O�Q�⥦���X�_�өҥH�ΤF�I�O�A�S�Q��...�u���ܩ�p�C"+htmlend
r_statue_complete  = html+rupio+"�����ڨӨq�@�U�ڪ������a...�H����...��L���T�w�b�x�l�W... �A�⨭��K�W�h... ���Y�M���u���������X�I���n�A�@�զX����...�ӡI�����աI���M�s���������i�H�ݱo�X���X�I�A���ݰ_�ӹ������~���O�ܡH�@��...�O�u�Y�k�����Ҽ˶ܡH�J�Ӥ@�ݡA�u�O�ӫܺ�o���J���C"+htmlend
r_tablet_pieces    = html+rupio+"�A��򪾹D�ڪ�����O�_��򪫰ڡH���O���H�g���o�˨観��r���򪫡A�u�n�ʤ֤@�����N�L�k���D���e�A�ҥH�զX�F�]�S����ΡC�H�ڪ��g��A���H�g���o�إ|���Ϊ��򪫡A�q�`�|�H��<font color=\"LEVEL\">4��</font>..."+htmlend
r_tablet_brockes  = html+rupio+"�����ڨӨq�@�U�ڪ������a...�H�����o�}���ݰ_�ӹ��O�̤U�����@����...�o�}���O�b���W��...����I�H�g���}�H�F�C���Ӧ��N�n�w�ƨ�g�L���~�����j�B���A�o�j�N�H�g���|�ܯܮz...�u�O��...�I�ڳ��M�ǤU�o��j�����A�u�O�藍�_�C"+htmlend
r_tablet_complete  = html+rupio+"�����ڨӨq�@�U�ڪ������a...�H�����o�}���ݰ_�ӹ��O�̤U�����@����...�o�}���O�b���W��...�n���b�����ϳ�... ��F�I�����աI�j�N�H�g��... �u�n�_�o�䤤�쩳�O���ۭ��Ǿ��v�����K�I�@��...���O�o���˴N�n�����H����r�O...�n���b���ਣ�L...�I���D�o�H�g���O...�I"+htmlend
#Lockirin
lockirin      = "���Ѫ��ԧJ�Y:<br>"
l_no_tablet      = html+lockirin+"�ڹ泌�H����D�`�P����C�ר�O���ӥH���H��r�O�����H�g���A�Y�ϭn�ڥI�X�����]�b�Ҥ����C���A�o�˱`�h�Ȧ檺�H�A�i��|�ݹL���تF��C�ڻ��A�b�f���a��`�`�|�o�{�j�N�H�g��..."+htmlend
l_just_pieces    = html+lockirin+"�o���H�g���O...�H���D�o�ӬO...�H���M�u�O�@�����A���O�o�O...�l�ܪ�...�I<br> �ޡA�~���H�I�o�ǪF��쩳�O�q���̧�쪺�H�p�G���Ҧ����Ѿl�H���A�զX�������~�A�ڱN�|���A�j��!�S���I�ڥH���|�p�X���Ѫ����W�q�A�M�A���w�I"+htmlend
l_tablet      = html+lockirin+"�o���H�g���O...�H���D�o�ӬO...�H���M�u�O�@�����A���O�o�O...���ܪ�...�I�o��Q�����F��쩳�O�q����...�H�ޡA�~���H�I�ڷ|���A�j���S���A��o�Ӧr���浹�ڧa�I<br><a action=\"bypass -h Quest 333_BlackLionHunt l_give\">�N�H�g���浹�L</a><br><a action=\"bypass -h Quest 333_BlackLionHunt l_info\">�ڵ���X�H�g��</a>"+htmlend
l_give        = html+lockirin+"�u�O�ӷP�§A�F�I�ڭ̤��|�p�X���J�@�Ʒ~�ש�...�I�ӡA��o�Ӧ��U��@�S��!�H��p�G�A�˨�o�˪��H�g���A�N�O�o�����ڡI���ެO�h�֧ڳ��|�I���I"+htmlend
l_info        = html+lockirin+"�u�O��...�ڳ����F�ڷ|���A�R�����S�ҡA�A�٩ڵ�...�~���H�A�A�O���O�H���i�H��o���H�g���H�����浹��L�a��?�ڥi�H�O�ҡA�Y�Ϩ�F�O���a��]���ӨS���H�|��ڥI��h�����A���H���A���ܷQ�k��A�A�ӧ�ڧa�C���ޤ���ɭԡA�p�G�⨺���H�g���浹�ڡA���٬O�̷Ӭ��w���A�j���S�Ҫ��I"+htmlend
#Undiras
undiras        = "�`�W���q�w�w�z�ȴ�:<br>"
u_no_statue      = html+undiras+"��Ӥj�����ѩ^�u�Y�k�����x�|�Ȧ��@�a�C�]�H���n�����v�Чﭲ�A�ڭ̪��k���Q�@�H�{���O�a�Ӧ��`�M�}�a���������s�b�A���ڭ̶·t���F�̵M�{���u�Y�O�ڭ̪��гy�̤δx�ޥͦ����k���C<br>�i�����O�Q�H���M���F���X�x�I��ɡA�򥢤F�ܦh�˹��������t���C�S�O�O�s�@��o���u�Y�k�����j�����������F�C���ެO�֭Y���ڭ̧�^�����J���A�ڭ̲`�W���x�̤@�w�����j�j����§..."+htmlend
u_just_pieces    = html+undiras+"�o���J���O�H���M�u�O�@����...�o�O�򥢪��u�Y�J�����@����...�I�o�F��쩳�O�q���̧�쪺�H�p�G���Ҧ����Ѿl�H���A�զX�������~�A�ڱN�|���A�ܤj����§���I"+htmlend
u_statue      = html+undiras+"�o���J���O�H�o�O...�o�O�򥢪��u�Y�J�����@����...�I�o�F��쩳�O�q���̧�쪺�H�o�򯫸t�����~�쩳�O�q����...�H�o���J���O�ڭ̶·t���F���t���C�ڷQ�H�����ʶR�A�����ڧa�C�ϥ���A�ӻ��O�S����γB�a�H<br><a action=\"bypass -h Quest 333_BlackLionHunt u_give\">��X�u�Y�J��</a><br><a action=\"bypass -h Quest 333_BlackLionHunt u_info\">�ڵ���X�u�Y�J��</a>"+htmlend
u_give        = html+undiras+"�]�H���n���F�v�Чﭲ�A�ڭ̪��k���Q�@�H�{���O�a�Ӧ��`�M�}�a���������s�b�A���ڭ̶·t���F�̵M�{���u�Y�O�ڭ̪��гy�̤δx�ޥͦ����k���C�i�����O�Q�H���M���F�p�X�x�I��ɡA�򥢤F�ܦh�˹��������t���C�A�a�Ӫ��J���O��ɿ򥢪����~���@�C�u���D�`�P�¡C�o�̡A���U����a�C�p�G�A���o�˪��J���A�Ч⥦�a�L�ӧa�C�@�`�W�����@���H�A�C"+htmlend
u_info        = html+undiras+"�o���J���O�ڭ̶·t���F���t���C�ϥ���A�ӻ��O�@�I�γ��S���C�ӥB�b�H�����|�a�ۥ���B���ʡA�|�Q���|�����Ю{�a...�H�S�Q�B����D�N�⩯�B�F�C�ϥ����A�Q�k�ܤF�A�A�ӧ�ڧa�C���ޤ���ɭԥu�n���J�����ڡA�ڷ|�H�p§���¡C�@�`�W�����֦��H�A�C"+htmlend
#Morgan
morgan        = "���|�|������:<br>"
m_no_box      = html+morgan+"�A�O�A�·�Ϊ��ħL�a�Hť���̪񬰤F�����o�@�a���]���A�]�ӫD�`���W�ڡC���]���U�A�̰աC"+htmlend
m_box        = html+morgan+"�A�O�A�·�Ϊ��ħL�a�Hť���̪񬰤F�����o�@�a���]���A�]�ӫD�`���W�ڡC���]���U�A�̰աC���L��ڦ�����ƶ�...�H<br><a action=\"bypass -h Quest 333_BlackLionHunt m_give\">��X�c�l</a>"+htmlend
m_rnd_1        = html+morgan+"�ڭ̰ӷ~�P�����f�c�I�H�o�O���[���e�Q�]��ŧ����A�q�����W�Q�m�����f���ڡI�̪�Q���ܪ��f���Ӧh�A����~�|�l���G���O�A�{�b���^�@�����]��O�y���աC<br>�ڥN��ӷ~�P���V�A�P�¡C�o�̡A���M���h�N��@�O�ڭ̪���§�a�C�٦��o�̡A�e�A�@�ӧڭ�(<font color=\"LEVEL\">���|���f��</font>)�C�o�O�ᤩ��ӷ~�P���^�m�̪��@�طP�µP�C<br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">��^</a>"+htmlend
m_rnd_2        = html+morgan+"�S��^�f�c�աC�u���D�`�P�§A�C�Q�]�����ܪ��f���O�V�ӶV�h�A�p�G�S���A�̶ħL�����A�ڭ̰ӷ~�P�����l���i�N�����]�Q�աC�o�̡A���U����a�C�٦���H���@�ˡA������·N�e�A<font color=\"LEVEL\">���|���f��</font>�C���]���U�A�̰աC<br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">��^</a>"+htmlend
m_rnd_3        = html+morgan+"�u�P�§A�C��������^�f�c�C�p�G�ڭ̰ӷ~�P����������p�y���R�Τ@�I�A�N�|���ΧA�o�ئ���O���ħL��ڭ̪��@�éO... �o�˴N���|�A���Q�]�����ܪ��Ʊ��o�ͤF�a�H<br>��!���U����a�C�ڸ�W�����H���L�o�Ǥ�l�A���ڭ̤��|�X�O���֡A�ҥH������B�Ƥ]�W�[�F�C�o�O�A���ӱo�쪺�A�ҥH���ݭn�Ȯ�C<br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">��^</a>"+htmlend
m_no_more_box       = html+morgan+"�f�c...�H����c�l�ڡH�A�n���S���o�تF���...�H"+htmlend
m_reward      = html+morgan+"������Ʊ��n����������...�H<br><a action=\"bypass -h Quest 333_BlackLionHunt m_give\">��X�f�c</a>"+htmlend

import sys
from com.l2jserver import Config 
from com.l2jserver.gameserver.model.quest import State
from com.l2jserver.gameserver.model.quest import QuestState
from com.l2jserver.gameserver.model.quest.jython import QuestJython as JQuest
#This Put all Mob Ids from dictionari in a list. So its possible to add new mobs, to one of this 4 Areas, without modification on the addKill Part.
MOBS=DROPLIST.keys()

def giveRewards(st,item,count):
  st.giveItems(ADENA_ID,35*count)
  st.takeItems(item,count)
  if count < 20:
    return
  if count<50:
    st.giveItems(LIONS_CLAW,1)
  elif count<100:
    st.giveItems(LIONS_CLAW,2)
  else:
    st.giveItems(LIONS_CLAW,3)
  return


class Quest (JQuest) :

  def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

  def onEvent (self,event,st) :
    part = st.getInt("part")
    if event == "start" :
      st.set("cond","1")
      st.setState(State.STARTED)
      st.playSound("ItemSound.quest_accept")
      #just to go with the official, until we have the option to make the take part invisible, like on officials.
      st.takeItems(BLACK_LION_MARK,1)
      st.giveItems(BLACK_LION_MARK,1)
      return start_explain
    elif event == "p1_t":
      st.set("part","1")
      st.giveItems(SOPHIAS_LETTER1,1)
      return p1_take
    elif event == "p2_t":
      st.set("part","2")
      st.giveItems(SOPHIAS_LETTER2,1)
      return p2_take
    elif event == "p3_t":
      st.set("part","3")
      st.giveItems(SOPHIAS_LETTER3,1)
      return p3_take
    elif event == "p4_t":
      st.set("part","4")
      st.giveItems(SOPHIAS_LETTER4,1)
      return p4_take
    elif event == "exit":
      st.takeItems(BLACK_LION_MARK,1)
      st.exitQuest(1)
      return exit
    elif event == "continue":
      claw=int(st.getQuestItemsCount(LIONS_CLAW)/10)
      check_eye=st.getQuestItemsCount(LIONS_EYE)
      if claw :
        st.giveItems(LIONS_EYE,claw)
        eye=st.getQuestItemsCount(LIONS_EYE)
        st.takeItems(LIONS_CLAW,claw*10)
        ala_count=3
        soul_count=100
        soe_count=20
        heal_count=20
        spir_count=50
        if eye > 9:
          ala_count=4
          soul_count=400
          soe_count=30
          heal_count=50
          spir_count=200
        elif eye > 4:
          spir_count=100
          soul_count=200
          heal_count=25
        while claw > 0:
          n = self.getRandom(5)
          if n < 1 :
            st.rewardItems(ALACRITY_POTION,ala_count)
          elif n < 2 :
            st.rewardItems(SOULSHOT_D,soul_count)
          elif n < 3:
            st.rewardItems(SCROLL_ESCAPE,soe_count)
          elif n < 4:
            st.rewardItems(SPIRITSHOT_D,spir_count)
          elif n == 4:
            st.rewardItems(HEALING_POTION,heal_count)
          claw-=1
        if check_eye:
          return p_eye
        else:
          return p_first_eye
      else:
        return start_continue
    elif event == "leave":
      if part == 1:
        order = SOPHIAS_LETTER1
      elif part == 2:
        order = SOPHIAS_LETTER2
      elif part == 3:
        order = SOPHIAS_LETTER3
      elif part == 4:
        order = SOPHIAS_LETTER4
      else:
        order = 0
      st.set("part","0")
      if order:
        st.takeItems(order,1)
      return p_leave_mission
    elif event == "f_info":
      text = st.getInt("text")
      if text<4:
        rnd=int(self.getRandom(20))
        st.set("text",str(text+1))
        text_rnd = html+redfoot+f_rnd_list[rnd]+back+htmlend
        return text_rnd
      else:
        return f_no_news
    elif event == "f_give":
      if st.getQuestItemsCount(CARGO_BOX1) :
        if st.getQuestItemsCount(ADENA_ID)>=OPEN_BOX_PRICE:
          st.takeItems(CARGO_BOX1,1)
          st.takeItems(ADENA_ID,650)
          random = self.getRandom(162)
          standart = "�n�A���N�ӥ��}�o�c�l�ݤ@��...�}�o����A�p�N��...�n�I�o��e���N���}�F�C����A�ݬݸ̭�������F��H<br>"
          statue = "�o�O...�H�۹����}���H�@��...�O�u�Y�k�����Ҽ�...���|�O���`�k���Aı�o���I���N�Q�H���O�p�G���O�}���ӬO�����~�A�N�����o�줣��������...�ˬO���@��M�a�O�M���׸ɳo�ؿ򪫪�...�L�O�s<font color=\"LEVEL\">�|�ֶ�</font>���K�K�C�p�G��۹����}�������᮳�L�h�A�L�|���A�׸ɦ������~�C<br>" 
          tablet = "�o�O...�H�۪����}���H�@��...�S�ݹL����r�C���D�O���H�ɥN���򪫡H�p�G���O�}���A�ӬO���n�����~�N�i�H�����öQ����ƤF�C�p�G���Ҧ����}��������N�i�H������ˤF...���p������A�N�h��s<font color=\"LEVEL\">�|�ֶ�</font>���K�K�a�C�L�O�_��򪫪��M�a�C<br>"
          if random < 21 :
            st.rewardItems(GLUDIO_APPLE,1)
            return html+redfoot+standart+"<br>���G...�H�j�|�B�S����ī�G�ڡI�ݰ_���Z�n�Y���C�H�a�����e�쥫���h�汼�A�N���ȱo��@�I���C<br>"+back+htmlend
          elif random < 41:
            st.rewardItems(CORN_MEAL,1)
            return html+redfoot+standart+"<br>�@�H�o���O�ɦ̯��ܡH�O���O���ޥΪ��H�ϥ��o���O�A�ݭn���F��A�i�H�쥫���W�汼�C���M�椣�F�h�ֿ��C<br>"+back+htmlend
          elif random < 61:
            st.rewardItems(WOLF_PELTS,1)
            return html+redfoot+standart+"<br>�o�i�֭��O...�H�c�T���֡H�֭��[�u�v�w�g�[�u�L�C�����O�i�ܰ��Ū��֭��C�i��s�y�ִU�ɯ�αo�ۧa�H�ϥ��A���쥫���W���ӽ�o�F�@�I���C<br>"+back+htmlend
          elif random < 74:
            st.rewardItems(MONNSTONE,1)
            return html+redfoot+standart+"<br>�_�ۡH�o�O��ۡI�]�O�s�@����۪��_�ۡC���ӯ��줣���������C<br>"+back+htmlend
          elif random < 86:
            st.rewardItems(GLUDIO_WEETS_FLOWER,1)
            return html+redfoot+standart+"<br>�@�H�o�ӯ����O...�H�|�@�U�A�ݬݦp��H�O�q�j�|�B�X�����ѯ��I���ӬO�Φb�N�ѥ]�a�H�ϥ��A���쥫�����ӥi�H��줣���������C<br>"+back+htmlend
          elif random < 98:
            st.rewardItems(SPIDERSILK_ROPE,1)
            return html+redfoot+standart+"<br>�o�O...�H�O�j�����÷���I�o�O�Τh�B�u�s�ߪ��T��_���������j����s�y���A��껴�K��÷���C����ө����ӷ|��줣���������a�C<br>"+back+htmlend
          elif random < 99:
            st.rewardItems(ALEXANDRIT,1)
            return html+redfoot+standart+"<br>�_��...�H�O���_�۶ܡH�ڡA���O�C�o�O���A�ɡI�A���D�����D�H�o�O�b�����U�e����A����U�e���⪺�öQ���_�ۡC���ӬO�Φb�s�y�Q���H�˹��~�W���F��a�H����ө����ӥi�H��Ӧn�����C<br>"+back+htmlend
          elif random < 109:
            st.rewardItems(SILVER_TEA,1)
            return html+redfoot+standart+"<br>�@�H�ȽL�H�٦����M�H�ݰ_���Z���Ū����H���ӬO���F�u�K�̪������C���M�ڹ�o�ǰ��Ū��~�S�����򿳽�...������ө����ӥi�H��Ӧn�����C<br>"+back+htmlend
          elif random < 119:
            st.rewardItems(GOLEM_PART,1)
            return html+redfoot+standart+"<br>�@�H����˸m...�H�o���ӬO�¦��K�z�u�|���г��r...�H���M�ڤ]���M���A���o�n���O�G�H�ײz���ڮɩҥΪ��s��C����ө����ӥi�H��Ӧn�����C<br>"+back+htmlend
          elif random < 123:
            st.rewardItems(FIRE_EMERALD,1)
            return html+redfoot+standart+"<br>�o�_�۬O...�H�ڡI���K���_�ۡI�A���D�����D�ܡH�o�O�b�����U�ല�o�X�j�P�������@�ثD�`�öQ���_�ۡC�A���B��u�O�n�I����ө����ӯ���ܦn�������C<br>"+back+htmlend
          elif random < 127:
            st.rewardItems(SILK_FROCK,1)
            return html+redfoot+standart+"<br>�o���O��A�ܡH�I�k�H�諸����§�A�C�Z���Ū����H�ݤ@�U�o�ӹϯ��C�o�O�q�F�誺�����Զi�f���F��C�쩳�֦b�o�Ӯɭԥγo�ذ��ت����~...�H�@�w�O�Y�ӳ��w���ꭷ�����Q���H�R�Ӭ諸���~�a�H��o�Ӯ���ө��h�汼�I���ӯ��o��ܦn�������C<br>"+back+htmlend
          elif random < 131:
            st.rewardItems(PORCELAN_URN,1)
            return html+redfoot+standart+"<br>�@�H���|�H�ܦh�a�観�ʤf�S�h�F��...���D�O�j���H�o�ӹϯ�...�H�@�@�I�I�I�O�s�ͤ��ꨩ�̼ڴ������ˡC�A�o��F�D�`���Q���򪫡H�o�جöQ�����~�b�ө��|��o��ܰ��������C<br>"+back+htmlend
          elif random < 132:
            st.rewardItems(IMPERIAL_DIAMOND,1)
            return html+redfoot+standart+"<br>�@�H���|�a�H���|�o�ˡI�I�I�ӫҪ�...�p�ۡH�Φb�˹��㺸���ȤB�ӫҪ��ӫa�W��...�H�u��...�D�`�}�G...�I�A�u�O�ө��B���H�I�~�M�o��F�o��Q�������~�C�p�G���쥫���W���ӯ�����D�`�n�������H<br>"+back+htmlend
          elif random < 147:
            random_stat=self.getRandom(4)
            if random_stat == 3 :
              st.giveItems(STATUE_SHILIEN_HEAD,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 0 :
              st.giveItems(STATUE_SHILIEN_TORSO,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 1 :
              st.giveItems(STATUE_SHILIEN_ARM,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 2 :
              st.giveItems(STATUE_SHILIEN_LEG,1)
              return html+redfoot+standart+statue+back+htmlend
          elif random < 162:
            random_tab=self.getRandom(4)
            if random_tab == 0 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE1,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 1:
              st.giveItems(FRAGMENT_ANCIENT_TABLE2,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 2 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE3,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 3 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE4,1)
              return html+redfoot+standart+tablet+back+htmlend
        else:
          return f_not_adena
      else:
        return f_no_more_box
    elif event in  ["r_give_statue","r_give_tablet"]:
      if event == "r_give_statue":
        items = statue_list
        item = COMPLETE_STATUE
        pieces = r_statue_pieces
        brockes = r_statue_brockes
        complete = r_statue_complete
      elif event == "r_give_tablet":
        items = tablet_list
        item = COMPLETE_TABLET
        pieces = r_tablet_pieces
        brockes = r_tablet_brockes
        complete = r_tablet_complete
      count=0
      for id in items:
        if st.getQuestItemsCount(id):
          count+=1
      if count>3:
        for id in items:
          st.takeItems(id,1)
        if self.getRandom(2)==1 :
          st.giveItems(item,1)
          return complete
        else:
          return brockes 
      elif count<4 and count!=0:
        return pieces
      else:
        return r_no_items
    elif event == "l_give" :
      if st.getQuestItemsCount(COMPLETE_TABLET):
        st.takeItems(COMPLETE_TABLET,1)
        st.giveItems(ADENA_ID,30000)
        return l_give
      else:
        return no_tablet
    elif event == "u_give" :
      if st.getQuestItemsCount(COMPLETE_STATUE) :
        st.takeItems(COMPLETE_STATUE,1)
        st.giveItems(ADENA_ID,30000)
        return u_give
      else:
        return no_statue
    elif event == "m_give":
      if st.getQuestItemsCount(CARGO_BOX1):
        coins = st.getQuestItemsCount(GUILD_COIN)
        count = int(coins/40)
        if count > 2 : count = 2
        st.giveItems(GUILD_COIN,1)
        st.giveItems(ADENA_ID,(1+count)*100)
        st.takeItems(CARGO_BOX1,1)
        random = self.getRandom(3)
        if random == 0:
          return m_rnd_1
        elif random == 1:
          return m_rnd_2
        else:
          return m_rnd_3
      else:
        return m_no_box
    elif event == "start_parts":
      return start_parts
    elif event == "m_reward":
      return m_reward
    elif event == "u_info":
      return u_info
    elif event == "l_info":
      return l_info
    elif event == "p_redfoot":
      return p_redfoot
    elif event == "p_trader_info":
      return p_trader_info
    elif event == "start_chose_parts":
      return start_parts
    elif event == "p1_explanation":
      return p1_explanation
    elif event == "p2_explanation":
      return p2_explanation
    elif event == "p3_explanation":
      return p3_explanation
    elif event == "p4_explanation":
      return p4_explanation
    elif event == "f_more_help":
      return f_more_help
    elif event == "r_exit":
      return r_exit
    
  def onTalk (self,npc,player):
    htmltext = "<html><body>�ثe�S��������ȡA�α��󤣲šC</body></html>"
    st = player.getQuestState(qn)
    if not st : return htmltext

    npcId = npc.getNpcId()
    id = st.getState()
    if npcId != NPC[0] and id != State.STARTED : return htmltext

    if id == State.CREATED :
      if npcId == NPC[0]:
        if st.getQuestItemsCount(BLACK_LION_MARK) :
          if player.getLevel() >24 :
            return  start_start
          else:
            st.exitQuest(1)
            return start_error1
        else:
          st.exitQuest(1)
          return start_error2
    else: 
      part=st.getInt("part")
      if npcId==NPC[0]:
          if part == 1:
            item = UNDEAD_ASH
          elif part == 2:
            item = BLOODY_AXE_INSIGNIAS
          elif part == 3:
            item = DELU_FANG
          elif part == 4:
            item = STAKATO_TALONS
          else:
            return start_ask_again
          count=st.getQuestItemsCount(item)
          box=st.getQuestItemsCount(CARGO_BOX1)
          if box and count:
            giveRewards(st,item,count)
            return p_both_info
          elif box:
            return p_only_box_info
          elif count:
            giveRewards(st,item,count)
            return p_only_item_info
          else:
            return p_no_items
      elif npcId==NPC[1]:
          if st.getQuestItemsCount(CARGO_BOX1):
            return f_give_box
          else:
            return f_no_box
      elif npcId==NPC[2]:
          count=0
          for items in statue_list:
            if st.getQuestItemsCount(items):
              count+=1
          for items in tablet_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return r_items
          else:
            return r_no_items
      elif npcId==NPC[3]:
        if st.getQuestItemsCount(COMPLETE_STATUE):
          return u_statue
        else:
          count=0
          for items in statue_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return u_just_pieces
          else:
            return u_no_statue
      elif npcId==NPC[4]:
        if st.getQuestItemsCount(COMPLETE_TABLET):
          return l_tablet
        else:
          count=0
          for items in tablet_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return l_just_pieces
          else:
            return l_no_tablet
      elif npcId==NPC[5]:
        if st.getQuestItemsCount(CARGO_BOX1):
          return m_box
        else:
          return m_no_box
          
  def onKill(self,npc,player,isPet):
    st = player.getQuestState(qn)
    if not st : return 
    if st.getState() != State.STARTED : return 

    npcId = npc.getNpcId()
    part,allowDrop,chancePartItem,chanceBox,partItem=DROPLIST[npcId]
    random1 = self.getRandom(101)
    random2 = self.getRandom(101)
    mobLevel = npc.getLevel()
    playerLevel = player.getLevel()
    if playerLevel - mobLevel > 8:
      chancePartItem/=3
      chanceBox/=3
    if allowDrop and st.getInt("part")==part :
      if random1<chancePartItem :
        st.giveItems(partItem,1)
        st.playSound("ItemSound.quest_itemget")
      if random2<chanceBox :
        st.giveItems(CARGO_BOX1,1)
        if not random1<chancePartItem:
          st.playSound("ItemSound.quest_itemget") 
    return


QUEST       = Quest(333,qn,"�·઺���y")


QUEST.addStartNpc(NPC[0])

for npcId in NPC:
  QUEST.addTalkId(npcId)

for mobId in MOBS:
  QUEST.addKillId(mobId)