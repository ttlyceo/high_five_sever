@ECHO OFF
title L2JTW - CB�ֳt�����Y
set CB_Name1=Community
echo �A�{�b�ǳơu�����Y�v�� CB�A�䴩�������O�G��������
echo.
echo �@�@�@�@�@�u�����Y�v����m�O�GC:\L2JTW\%CB_Name1%\
echo.
pause
CLS
if not exist "build\*.zip" goto _failed
if not exist C:\L2JTW\%CB_Name1%\community\config_bak1\ md C:\L2JTW\%CB_Name1%\community\config_bak1\
if not exist C:\L2JTW\%CB_Name1%\community\config_bak2\ md C:\L2JTW\%CB_Name1%\community\config_bak2\
if not exist C:\L2JTW\%CB_Name1%\community\config_bak3\ md C:\L2JTW\%CB_Name1%\community\config_bak3\
if exist C:\L2JTW\%CB_Name1%\community\config_bak2\*.properties copy C:\L2JTW\%CB_Name1%\community\config_bak2\*.properties C:\L2JTW\%CB_Name1%\community\config_bak3\ /Y >nul
if exist C:\L2JTW\%CB_Name1%\community\config_bak1\*.properties copy C:\L2JTW\%CB_Name1%\community\config_bak1\*.properties C:\L2JTW\%CB_Name1%\community\config_bak2\ /Y >nul
if exist C:\L2JTW\%CB_Name1%\community\config\*.properties copy C:\L2JTW\%CB_Name1%\community\config\*.properties C:\L2JTW\%CB_Name1%\community\config_bak1\ /Y >nul
if not exist "winrar.exe" goto _winrar
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do winrar x -o+ %%i C:\L2JTW\%CB_Name1%\
goto _finish

:_winrar
if not exist "%ProgramFiles%\WinRAR\winrar.exe" goto _ERR
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do "%ProgramFiles%\WinRAR\winrar.exe" x -o+ %%i C:\L2JTW\%CB_Name1%\
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
echo CB��s�����I
echo.
echo �u�ª� config�v�w�g�ƥ���uconfig_bak1�v
echo.
echo �аO�o�}�� C:\L2JTW\%CB_Name1%\community\config\communityserver.properties
echo �ק�u�G�i����A���v���s�u�K�X�M�����]�w�I
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
