@echo off
setlocal
py "%~dp0main.py" %*
if errorlevel 1 pause
