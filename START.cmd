@echo off
:loop
set "current_time=%time:~0,8%"
echo [@]-------------------------------
echo [INFO^|%current_time%] Round STARTED
echo [@]
V:\Python\ScoreSheet\venv\Scripts\python.exe V:\Python\ScoreSheet\ScoreSheet.py
echo [@]
echo [INFO^|%current_time%] Round ENDED
echo [@]-------------------------------
timeout /t 1 >nul
goto loop