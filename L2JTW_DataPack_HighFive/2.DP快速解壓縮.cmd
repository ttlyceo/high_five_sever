@ECHO OFF
title L2JTW - DP�ֳt�����Y
if not exist "dist\doc\DP-Name.txt" goto _OPSTART
set DP_Name1=Test
FOR /F "tokens=1" %%g IN (dist\doc\DP-Name.txt) DO set DP_Name1=%%g
FOR /F "tokens=2" %%h IN (dist\doc\DP-Name.txt) DO set DP_Name2=%%h
echo �A�{�b�ǳơu�����Y�v�� DP�A�䴩�������O�G%DP_Name1% %DP_Name2%
echo.
echo �@�@�@�@�@�u�����Y�v����m�O�GC:\L2JTW\%DP_Name1%\
echo.
pause
CLS

:_OPSTART
if not exist "build\*.zip" goto _failed
if not exist "winrar.exe" goto _winrar
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do winrar x -o+ %%i C:\L2JTW\%DP_Name1%\
goto _finish

:_winrar
if not exist "%ProgramFiles%\WinRAR\winrar.exe" goto _ERR
echo �����Y���A�еy�� . . .
FOR %%i in (build\*.zip) do "%ProgramFiles%\WinRAR\winrar.exe" x -o+ %%i C:\L2JTW\%DP_Name1%\
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
echo �ЦA���� C:\L2JTW\%DP_Name1%\tools\ �̭����udatabase_installer�v
echo ��ܡu��s�v��Ʈw�A�A�@���� Enter ���쵲���A�~�⧹�� DP ����s
echo.
pause
goto _EXIT
 
:_failed
echo �Ч����sĶ��A��������Y�I
echo.
pause

:_EXIT
