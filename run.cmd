@echo off
setlocal enabledelayedexpansion
:: Получить текущий диск, на котором находится скрипт
for %%i in ("%~dp0") do set currentDrive=%%~di

:: Запустить скрипт на текущем диске
cmd /k "cd /d !currentDrive!\PythonProjects\ytVideoNamesDumper\venv\Scripts & activate & cd /d !currentDrive!\PythonProjects\ytVideoNamesDumper & python main.py"
@REM pause
