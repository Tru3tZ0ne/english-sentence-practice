@echo off
setlocal
cd /d "%~dp0"
set "PY_CMD="
where py >nul 2>nul && (py -3 -c "import sys" >nul 2>nul && set "PY_CMD=py -3")
if not defined PY_CMD where python >nul 2>nul && set "PY_CMD=python"
if not defined PY_CMD (echo [错误] 未找到 Python 3，请安装 Python 3.11+。& pause & exit /b 1)
if not exist ".venv\Scripts\python.exe" (%PY_CMD% -m venv .venv || (echo [错误] 创建虚拟环境失败。& pause&exit /b 1))
if not exist ".venv\.requirements-installed" (.venv\Scripts\python.exe -m pip install -r requirements.txt || (echo [错误] 依赖安装失败。& pause&exit /b 1)) & type nul > .venv\.requirements-installed
.venv\Scripts\python.exe run_app.py
if errorlevel 1 (echo [错误] 应用启动失败，请查看 logs\app.log。&pause)
