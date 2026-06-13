@echo off
REM CreditPathAI - Quick Local Setup Script for Windows

echo 🚀 CreditPathAI - Local Development Setup
echo ===========================================

REM Backend Setup
echo.
echo 📦 Setting up Backend...
cd backend

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    copy .env.example .env
    echo ✅ Created .env file from .env.example
)

echo ✅ Backend setup complete!
echo 📝 Backend environment variables configured in .env

REM Frontend Setup
echo.
echo 📦 Setting up Frontend...
cd ..\frontend

REM Install dependencies
call npm install

REM Create .env files if they don't exist
if not exist .env.development (
    (echo REACT_APP_API_URL=http://localhost:8000) > .env.development
    echo ✅ Created .env.development
)

if not exist .env.production (
    (echo REACT_APP_API_URL=https://creditpath-backend.onrender.com) > .env.production
    echo ✅ Created .env.production
)

echo ✅ Frontend setup complete!

echo.
echo ===========================================
echo ✨ Setup Complete!
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   cd backend
echo   venv\Scripts\activate.bat
echo   python -m uvicorn milestone5_api:app --reload --port 8000
echo.
echo Terminal 2 (Frontend):
echo   cd frontend
echo   npm start
echo.
echo Application will be available at: http://localhost:3000
echo API will be available at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.
pause
