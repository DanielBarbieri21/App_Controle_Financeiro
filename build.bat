@echo off
setlocal enabledelayedexpansion
set JAVA_HOME=C:\Program Files\Java\jdk-17
set JAVA_TOOL_OPTIONS=
set _JAVA_OPTIONS=
cd /d "%~dp0"
call gradlew.bat assembleDebug
pause
