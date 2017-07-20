@echo off

:begin

echo LogFilePath:Input Log File Path
echo refresh:Input 0 Draw Once,Input 1 Watch Loop (60s)

set /p LogFilePath=LogFilePath:
set /p refresh=refresh:

call :show %LogFilePath%

python parse_log.py %LogFilePath% %str2%

python test.py %LogFilePath% %refresh%

pause

goto begin

:show
set str2=%~dp1