@echo off
cd /d "%~dp0"
if exist ".venv" rmdir /s /q ".venv"
echo 开发环境已删除，下次运行 start.bat 将自动重建。
pause
