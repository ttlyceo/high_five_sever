@ECHO OFF
title L2JTW - GS�ֳt�����Y
if not exist "dist\doc\GS-Name.txt" goto _OPSTART
set GS_Name1=Test
FOR /F "tokens=1" %%g IN (dist\doc\GS-Name.txt) DO set GS_Name1=%%g
FOR /F "tokens=2" %%h IN (dist\doc\GS-Name.txt) DO set GS_Name2=%%h
echo �A�{�b�ǳơu�����Y�v�� GS�A�䴩�������O�G%GS_Name1% %GS_Name2%
echo.
echo �@�@�@�@�@�u�����Y�v����m�O�GC:\L2JTW\%GS_Name1%\
echo.
pause
CLS

:_OPSTART
set GSM=game
REM set GSM=gameserver
REM �̷s�� L2J �� gameserver ����Ƨ���W�� game
if not exist "build\*.zip" goto _failed
if not exist C:\L2JTW\%GS_Name1%\login\config_bak1\ md C:\L2JTW\%GS_Name1%\login\config_bak1\
if not exist C:\L2JTW\%GS_Name1%\login\config_bak2\ md C:\L2JTW\%GS_Name1%\login\config_bak2\
if not exist C:\L2JTW\%GS_Name1%\login\config_bak3\ md C:\L2JTW\%GS_Name1%\login\config_bak3\
if not exist C:\L2JTW\%GS_Name1%\%GSM%\config_bak1\ md C:\L2JTW\%GS_Name1%\%GSM%\config_bak1\
if not exist C:\L2JTW\%GS_Name1%\%GSM%\config_bak2\ md C:\L2JTW\%GS_Name1%\%GSM%\config_bak2\
if not exist C:\L2JTW\%GS_Name1%\%GSM%\config_bak3\ md C:\L2JTW\%GS_Name1%\%GSM%\config_bak3\
if exist C:\L2JTW\%GS_Name1%\login\config_bak2\*.properties copy C:\L2JTW\%GS_Name1%\login\config_bak2\*.properties C:\L2JTW\%GS_Name1%\login\config_bak3\ /Y >nul
if exist C:\L2JTW\%GS_Name1%\login\config_bak1\*.properties copy C:\L2JTW\%GS_Name1%\login\config_bak1\*.properties C:\L2JTW\%GS_Name1%\login\config_bak2\ /Y >nul
if exist C:\L2JTW\%GS_Name1%\login\config\*.properties copy C:\L2JTW\%GS_Name1%\login\config\*.properties C:\L2JTW\%GS_Name1%\login\config_bak1\ /Y >nul
if exist C:\L2JTW\%GS_Name1%\%GSM%\config_bak2\*.properties copy C:\L2JTW\%GS_Name1%\%GSM%\config_bak2\*.properties C:\L2JTW\%GS_Name1%\%GSM%\config_bak3\ /Y >nul
if exist C:\L2JTW\%GS_Name1%\%GSM%\config_bak1\*.properties copy C:\L2JTW\%GS_Name1%\%GSM%\config_bak1\*.properties C:\L2JTW\%GS_Name1%\%GSM%\config_bak2\ /Y >nul
if exist C:\L2JTW\%GS_Name1%\%GSM%\config\*.properties copy C:\L2JTW\%GS_Name1%\%GSM%\config\*.properties C:\L2JTW\%GS_Name1%\%GSM%\config_bak1\ /Y >nul
if not exist "winrar.exe" goto _winrar
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do winrar x -o+ %%i C:\L2JTW\%GS_Name1%\
goto _finish

:_winrar
if not exist "%ProgramFiles%\WinRAR\winrar.exe" goto _ERR
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do "%ProgramFiles%\WinRAR\winrar.exe" x -o+ %%i C:\L2JTW\%GS_Name1%\
goto _finish

:_ERR
echo �Х��w�� WinRAR �����Y�{���I
echo.
pause
goto _EXIT

:_finish
CLS
echo �����Y�����I
echo.
echo GS��s�����I
echo.
echo �u�ª� config�v�w�g�ƥ���uconfig_bak1�v
echo.
echo �аO�o�}�� C:\L2JTW\%GS_Name1%\login\config\LoginServer.properties
echo �ק�u�n�J���A���v���s�u�K�X�M�����]�w�I
echo.
echo �аO�o�}�� C:\L2JTW\%GS_Name1%\%GSM%\config\Server.properties
echo �ק�u�C�����A���v���s�u�K�X�M�����]�w�I
echo.
echo �Ϊ̨ϥ� WinMerge�A��� config �M config_bak1 �o�G�Ӹ�Ƨ�
echo.
pause
goto _EXIT
 
:_failed
echo �Ч����sĶ��A��������Y�I
echo.
pause

:_EXIT
