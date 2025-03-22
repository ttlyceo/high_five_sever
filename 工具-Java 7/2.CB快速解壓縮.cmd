@ECHO OFF
title L2JTW - CB快速解壓縮
set CB_Name1=Community
echo 你現在準備「解壓縮」的 CB，支援的版本是：不限版本
echo.
echo 　　　　　「解壓縮」的位置是：C:\L2JTW\%CB_Name1%\
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
echo 解壓縮中，請稍候 . . .
FOR %%i in (build\*.zip) do winrar x -o+ %%i C:\L2JTW\%CB_Name1%\
goto _finish

:_winrar
if not exist "%ProgramFiles%\WinRAR\winrar.exe" goto _ERR
echo 解壓縮中，請稍候 . . .
FOR %%i in (build\*.zip) do "%ProgramFiles%\WinRAR\winrar.exe" x -o+ %%i C:\L2JTW\%CB_Name1%\
goto _finish

:_ERR
echo 請先安裝 WinRAR 解壓縮程式！
echo.
pause
goto _EXIT

:_finish
CLS
echo 解壓縮完成！
echo.
echo CB更新完成！
echo.
echo 「舊的 config」已經備份到「config_bak1」
echo.
echo 請記得開啟 C:\L2JTW\%CB_Name1%\community\config\communityserver.properties
echo 修改「佈告欄伺服器」的連線密碼和相關設定！
echo.
echo 或者使用 WinMerge，比對 config 和 config_bak1 這二個資料夾
echo.
pause
goto _EXIT
 
:_failed
echo 請完成編譯後再執行解壓縮！
echo.
pause

:_EXIT
