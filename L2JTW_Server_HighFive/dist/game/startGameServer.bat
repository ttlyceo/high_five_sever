@echo off
title Game Server Console
REM ------------------------------------------------------
REM �ˬd�O�_�s�b DP �䴩��������T
if not exist ..\doc\L2J_DataPack_Ver.txt echo �S���o�{ DP �䴩��������T�I
if not exist ..\doc\L2J_DataPack_Ver.txt echo �ЦA�@���G��s DP �� �sĶ DP �� �����Y DP �� �w�˸�Ʈw
if not exist ..\doc\L2J_DataPack_Ver.txt echo.
if not exist ..\doc\L2J_DataPack_Ver.txt pause
if not exist ..\doc\L2J_DataPack_Ver.txt exit
REM ���o DP �䴩��������T
FOR /F %%g IN (..\doc\L2J_DataPack_Ver.txt) DO set vdp=%%g
REM �ˬd DP �䴩��������T
if not %vdp% == High_Five echo �L�k�~�������A���A�]���G
if not %vdp% == High_Five echo GS �䴩�������O�GHigh_Five
if not %vdp% == High_Five echo DP �䴩�������O�G%vdp%
if not %vdp% == High_Five echo �нT�w GS �M DP ���ϥάۦP��������A�A�դ@��
if not %vdp% == High_Five echo.
if not %vdp% == High_Five pause
if not %vdp% == High_Five exit
REM ------------------------------------------------------

call :init
:: ----- �]�w java �O����ζq�Ψ�L�Ѽ� -----
set javaheap=1024m

set java_param=com.l2jserver.gameserver.GameServer
set java_param=-cp "%iii%libs\*";"%LLL%l2jserver.jar" %java_param%
set java_param=-Xms%javaheap% -Xmx%javaheap% %java_param%
:: set java_param=-XX:PermSize=50m %java_param%
:: set java_param=-XX:MaxPermSize=100m %java_param%
set java_param=-XX:+CMSIncrementalMode %java_param%
set java_param=-XX:+UseCMSCompactAtFullCollection %java_param%
set java_param=-XX:+UseParNewGC %java_param%
set java_param=-XX:+CMSParallelRemarkEnabled %java_param%
set java_param=-XX:+UseParNewGC %java_param%
set java_param=-XX:+CMSParallelRemarkEnabled %java_param%
set java_param=-XX:+UseConcMarkSweepGC %java_param%
set java_param=-Djava.util.logging.manager=com.l2jserver.util.L2LogManager %java_param%
:: set java_param=-Djava.util.logging.manager=com.l2jserver.util.L2LogManager -XX:+UseConcMarkSweepGC -XX:+CMSParallelRemarkEnabled -XX:+UseParNewGC -XX:+UseCMSCompactAtFullCollection -XX:+CMSIncrementalMode -Xms%javaheap% -Xmx%javaheap% -cp "%iii%libs\*";"%LLL%l2jserver.jar" com.l2jserver.gameserver.GameServer
goto start

:init
set LLL=%~dp0
::FOR /F "delims=game" %%i IN ("%LLL%") do set iii=%%i
set iii=%LLL:~0,-5%
call :check_libs
call :try_java
goto :eof

:check_libs
REM ------------------------------------------------------
if not exist ..\libs\*.jar (
	echo �z�������s�����Y�u�sĶ�����v�� GS�A�~�i�H�~�����
	echo.
	pause
	exit
)
goto :eof
REM ------------------------------------------------------

:check_java
if "%found%"=="1" goto :eof
if not exist %1 goto :eof
set found=1
set PATH=%~dp1
REM echo �ϥ� java ��m %path%
goto :eof

:set_java
REM echo �j�M java ��m
call :check_java "%ProgramW6432%\Java\jre7\bin\java.exe"
call :check_java "%ProgramFiles%\Java\jre7\bin\java.exe"
call :check_java "%ProgramFiles(x86)%\Java\jre7\bin\java.exe"
call :check_java "%windir%\system32\java.exe"
if "%found%"=="" (
	echo �䤣�� java.exe
	echo �Х��w�� java 1.7
	echo �U���Φw�˥i�Ѧҽ׾�
	echo http://www.l2jtw.com/l2jtwbbs/viewtopic.php?f=42^&t=6264
	echo.
	pause
	exit
)
goto :eof

:try_java
call :set_java
goto :eof

:start
java %java_param%
if ERRORLEVEL 2 goto restart
if ERRORLEVEL 1 goto error
goto end

:restart
echo.
echo Admin Restart ...
echo.
goto start

:error
echo.
echo Server terminated abnormally
echo.
:end
echo.
echo server terminated
echo.
pause
