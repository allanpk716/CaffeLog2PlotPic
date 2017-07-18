@echo off

:begin

set /p LogFilePath=LogFilePath:

python parse_log.py %LogFilePath% %cd%

python test.py %LogFilePath%

pause

goto begin