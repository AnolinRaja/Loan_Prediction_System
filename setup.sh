#!/bin/bash
# CreditPathAI - Quick Local Setup Script

echo "🚀 CreditPathAI - Local Development Setup"
echo "==========================================="

# Backend Setup
echo ""
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file from .env.example"
fi

echo "✅ Backend setup complete!"
echo "📝 Backend environment variables configured in .env"

# Frontend Setup
echo ""
echo "📦 Setting up Frontend..."
cd ../frontend

# Install dependencies
npm install

# Create .env files if they don't exist
if [ ! -f .env.development ]; then
    echo "REACT_APP_API_URL=http://localhost:8000" > .env.development
    echo "✅ Created .env.development"
fi

if [ ! -f .env.production ]; then
    echo "REACT_APP_API_URL=https://creditpath-backend.onrender.com" > .env.production
    echo "✅ Created .env.production"
fi

echo "✅ Frontend setup complete!"

echo ""
echo "==========================================="
echo "✨ Setup Complete!"
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  venv\\Scripts\\activate  (Windows) or source venv/bin/activate (Mac/Linux)"
echo "  python -m uvicorn milestone5_api:app --reload --port 8000"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Application will be available at: http://localhost:3000"
echo "API will be available at: http://localhost:8000"
echo "API Docs at: http://localhost:8000/docs"
