Write-Host "正在启动 AI 自动写小说系统..." -ForegroundColor Green
Write-Host ""

# 启动后端
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; python -m venv venv 2>$null; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt *>$null; python main.py"

# 等待 2 秒
Start-Sleep -Seconds 2

# 启动前端
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm install *>$null; npm run dev"

Write-Host ""
Write-Host "前后端已在新窗口中启动" -ForegroundColor Green
Write-Host "后端: http://localhost:8000" -ForegroundColor Cyan
Write-Host "前端: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
