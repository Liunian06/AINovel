@echo off
echo 正在启动 AI 自动写小说系统...
echo.

REM 启动后端
start "AI Novel Backend" cmd /k "cd backend && python -m venv venv 2>nul && venv\Scripts\activate && pip install -r requirements.txt >nul 2>&1 && python main.py"

REM 等待 2 秒
timeout /t 2 /nobreak >nul

REM 启动前端
start "AI Novel Frontend" cmd /k "cd frontend && npm install >nul 2>&1 && npm run dev"

echo.
echo 前后端已在新窗口中启动
echo 后端: http://localhost:8000
echo 前端: http://localhost:3000
echo.
pause
