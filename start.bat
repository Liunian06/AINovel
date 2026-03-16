@echo off
chcp 65001 >nul
echo ========================================
echo    AI Novel Generator - Starting...
echo ========================================
echo.

REM Start Backend
echo [1/2] Starting Backend Server...
start "AI Novel Backend" cmd /k "chcp 65001 >nul && cd backend && python -m venv venv 2>nul && venv\Scripts\activate && pip install -r requirements.txt >nul 2>&1 && python main.py"

REM Wait 2 seconds
timeout /t 2 /nobreak >nul

REM Start Frontend
echo [2/2] Starting Frontend Server...
start "AI Novel Frontend" cmd /k "cd frontend && npm install >nul 2>&1 && npm run dev"

echo.
echo ========================================
echo    Services started successfully!
echo ========================================
echo.
echo    Backend:  http://localhost:8000
echo    Frontend: http://localhost:3000
echo.
echo    Press any key to exit this window...
echo    (Services will continue running in new windows)
echo ========================================
echo.
pause