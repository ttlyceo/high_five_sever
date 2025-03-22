@ECHO OFF
title L2JTW - DP�ֳt�sĶ

if exist "DP-Support.txt" (
type "DP-Support.txt"
echo.
pause
CLS
)
if not exist "build.xml" goto _WRONG_LOC
:_check_copy
if exist "DP-Support.txt" goto _check_copy_next
if exist "GS-Support.txt" echo �b�o�Ӹ�Ƨ����Ӱ���uGS�ֳt�sĶ�v�~��I
if exist "GS-Support.txt" echo.
if exist "GS-Support.txt" pause
if exist "GS-Support.txt" goto _EXIT
if exist "CB-Support.txt" echo �b�o�Ӹ�Ƨ����Ӱ���uCB�ֳt�sĶ�v�~��I
if exist "CB-Support.txt" echo.
if exist "CB-Support.txt" pause
if exist "CB-Support.txt" goto _EXIT
type build.xml | find /c /i "_Datapack" > %temp%\check.txt
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 goto _check_copy_next
type build.xml | find /c /i "_GameServer" > %temp%\check.txt
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo �b�o�Ӹ�Ƨ����Ӱ���uGS�ֳt�sĶ�v�~��I
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo.
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 pause
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 goto _EXIT
type build.xml | find /c /i "_Community" > %temp%\check.txt
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo �b�o�Ӹ�Ƨ����Ӱ���uCB�ֳt�sĶ�v�~��I
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo.
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 pause
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 goto _EXIT
type build.xml | find /c /i "_Server" > %temp%\check.txt
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo �b�o�Ӹ�Ƨ����Ӱ���uGS�ֳt�sĶ�v�~��I
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 echo.
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 pause
FOR /F %%i IN (%temp%\check.txt) DO IF %%i GTR 0 goto _EXIT
:_check_copy_next
if not exist "WinRAR.exe" goto _UPDATE
if not exist "ant.jar" goto _UPDATE
if not exist "ant-launcher.jar" goto _UPDATE
if not exist "2.DP*.cmd" goto _UPDATE
if exist "1.GS*.cmd" del "1.GS*.cmd"
if exist "1.CB*.cmd" del "1.CB*.cmd"
if exist "2.GS*.cmd" del "2.GS*.cmd"
if exist "2.CB*.cmd" del "2.CB*.cmd"

:_start
set PF=%ProgramFiles%
if exist "%ProgramFiles(x86)%" set PF=%ProgramFiles(x86)%
if exist "%PF%\MySQL\MySQL Server 5.0\bin\mysql.exe" goto _MySQL
if exist "%PF%\MySQL\MySQL Server 5.1\bin\mysql.exe" goto _MySQL
if exist "%PF%\MySQL\MySQL Server 5.5\bin\mysql.exe" goto _MySQL
if not exist "%ProgramFiles%\Java\jre8\bin\java.exe" goto _JAVA_ERR

:_check_ver
if not exist "%ProgramFiles%\Java\jdk1.8.*" goto _JAVA_ERR
dir "%ProgramFiles%\Java\jdk1.8.*" /A:D /B /O > %temp%\check.txt
FOR /F %%j IN (%temp%\check.txt) DO set ver=%%j

:_JAVA_VER
if not exist "%ProgramFiles%\Java\%ver%\lib\tools.jar" goto _JAVA_ERR
if not exist "%ProgramFiles%\Java\%ver%\bin\java.exe" goto _JAVA_ERR
if exist "%ProgramFiles%\Java\%ver%\lib\ant_194dp.txt" goto _JAVA_VER_NEXT
echo.>> "%ProgramFiles%\Java\%ver%\lib\ant_194dp.txt"
if not exist "%ProgramFiles%\Java\%ver%\lib\ant_194dp.txt" goto _NO_ACCESS
copy /Y "ant.jar" "%ProgramFiles%\Java\%ver%\lib" > nul
copy /Y "ant-launcher.jar" "%ProgramFiles%\Java\%ver%\lib" > nul
:_JAVA_VER_NEXT
if not exist "%ProgramFiles%\Java\%ver%\lib\ant.jar" copy /Y "ant.jar" "%ProgramFiles%\Java\%ver%\lib" > nul
if not exist "%ProgramFiles%\Java\%ver%\lib\ant.jar" goto _NO_ACCESS
if not exist "%ProgramFiles%\Java\%ver%\lib\ant-launcher.jar" copy /Y "ant-launcher.jar" "%ProgramFiles%\Java\%ver%\lib" > nul
if not exist "%ProgramFiles%\Java\%ver%\lib\ant-launcher.jar" goto _NO_ACCESS
goto _NEXT

:_NEXT
if not exist "%PF%\Notepad++\notepad++.exe" goto _NOTEPAD
if not exist "%PF%\WinMerge\WinMergeU.exe" goto _WINMERGE
if not exist "%ProgramFiles%\TortoiseSVN\bin\TortoiseSVN*.dll" goto _SVN
if not exist "%SystemDrive%\AppServ\www\index.php" echo �䤣�� %SystemDrive%\AppServ
if not exist "%SystemDrive%\AppServ\www\index.php" echo.
if not exist "%SystemDrive%\AppServ\www\index.php" pause
CLS
if exist "build\*.zip" del "build\*.zip" /Q > nul
if exist "buildX" echo �R�����e�sĶ���Ȧs�ɮסA�еy�� . . .
if exist "buildX" RMDIR "buildX" /S /Q > nul
CLS
if exist "build" RENAME "build" "buildX" > nul
if exist "build" goto _USE
if exist "buildX" echo �R�����e�sĶ���Ȧs�ɮסA�еy�� . . .
if exist "buildX" RMDIR "buildX" /S /Q > nul
CLS

echo �sĶ���A�еy�� . . .
"%ProgramFiles%\Java\%ver%\bin\java.exe" -classpath "%ProgramFiles%\Java\%ver%\lib\ant-launcher.jar" "-Dant.home=%ProgramFiles%\Java\%ver%" org.apache.tools.ant.launch.Launcher > Log.txt
if not exist "build\*.zip" goto _failed
CLS
if exist "build\*.zip" type Log.txt
if exist "build\*.zip" echo.
if exist "build\*.zip" echo ����������������������
if exist "build\*.zip" echo ���@ DP�sĶ���\�I �@��
if exist "build\*.zip" echo ����������������������
echo.
echo �sĶ�L�{���T���w�x�s�b Log.txt
echo.
pause
goto _EXIT

:_MySQL
echo �Х������ª��� MySQL 5�A�~��i��sĶ
echo.
pause
goto _EXIT

:_JAVA_ERR
echo %ProgramFiles%\ �䤣�� Java 8
echo.
echo �Х��w�� JAVA JDK 8 ���̷s�����A�åB���n���w�]�w�˦�m
echo.
echo ������������������������������������������������������������������������
echo �� �`�N�GErtheia �F�����ǡ]�l�H�^�A�����w�� JAVA JDK 8 (���e�O JDK 7) ��
echo ������������������������������������������������������������������������
echo.
pause
goto _EXIT

:_NOTEPAD
echo %PF%\ �䤣�� Notepad++
echo.
echo �Х��w�� Notepad++�A�~��ק�]�w
echo �åB�b�w�ˮɡA���n���w�]�w�˦�m
echo.
pause
goto _EXIT

:_WINMERGE
echo %PF%\ �䤣�� WinMerge
echo.
echo �Х��w�� WinMerge�A�~���� config
echo �åB�b�w�ˮɡA���n���w�]�w�˦�m
echo.
pause
goto _EXIT

:_SVN
echo %ProgramFiles%\ �䤣�� TortoiseSVN
echo.
echo �Х��w�� TortoiseSVN�A�~��i���s
echo �åB�b�w�ˮɡA���n���w�]�w�˦�m
echo.
pause
goto _EXIT

:_WRONG_LOC
echo �L�k�b�o�Ӹ�Ƨ�����u�sĶ�v
echo.
echo �бN DP ��s��̷s������A�A�դ@��
echo.
pause
goto _EXIT

:_UPDATE
echo �Х��N�u�u��-Java 8�v���� 9 ���ɮסA�ƻs�� GS/DP/CB ����Ƨ�
echo.
pause
goto _EXIT

:_NO_ACCESS
color 0c
echo.
echo ����������������������������������������������
echo ���@�@�@�A���q���S���}��s�����v���I�I�@�@�@��
echo ����������������������������������������������
echo.
pause
CLS
echo ���I���G
echo �����H�u�t�κ޲z���v���b��n�J Windows�A�~�֦��������v��
echo �ˬd��k�G
echo Vista�G����x���s�W�β����ϥΪ̱b����ˬd�ݬݬO���O�uAdministrator�v
echo Win 7�G����x���s�W�β����ϥΪ̱b����ˬd�ݬݬO���O�u�t�κ޲z���v
echo ============================================================================
echo ���I���G
echo �������� UAC�A�u�ֳt�sĶ�v�~��s��
echo ������k�G�Ы��ӥH�U��k�A�� UAC ����
echo.
echo Vista�G����x���ϥΪ̱b��M�a�x�w�����ϥΪ̱b����}�ҩ������ϥΪ̱b�ᱱ���
echo        �������ġG�ϥ�[�ϥΪ̱b�ᱱ��(UAC)]�Ө�U�O�@�z���q�����T�w�����s�}��
echo.
echo Win 7�G����x���t�ΤΦw���ʡ��ܧ�ϥΪ̱b�ᱱ��]�w��
echo        �N�վ�s���U�Ԧܡu���n�q���v���T�w�����s�}��
echo ============================================================================
echo.
pause
goto _EXIT

:_USE
echo.
echo �Х������Ҧ��{���A�M��A�դ@���C
echo.
pause
goto _EXIT

:_failed
echo.
type Log.txt
echo.
echo ����������������������
echo ���@ DP�sĶ���ѡI �@��
echo ����������������������
echo.
echo �sĶ���Ѫ��T���w�x�s�b Log.txt
echo �z�i�H�N Log.txt �̭������e�K��Q�װϡA�M�D���U...
echo.
pause

:_EXIT
