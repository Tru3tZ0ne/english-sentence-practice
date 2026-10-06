@echo off
cd /d "%~dp0"
.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --windowed --name EnglishLearning --add-data "web;web" --add-data "content;content" run_app.py
echo 已生成 dist\EnglishLearning。
pause
