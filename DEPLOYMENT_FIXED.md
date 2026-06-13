# 🚀 CreditPathAI - Complete Deployment & Setup Guide

## ✅ Issues Fixed

This guide covers all deployment issues that have been fixed:

### Backend Fixes
- ✅ **Model Loading**: Now gracefully handles missing model files with fallback prediction
- ✅ **Environment Variables**: Properly reads CORS_ORIGINS from environment
- ✅ **Error Handling**: Improved error messages and logging
- ✅ **Health Checks**: Added `/health` endpoint for deployment verification
- ✅ **Path Issues**: Fixed relative/absolute path issues for model files

### Frontend Fixes
- ✅ **Dynamic API URL**: Now reads from environment variables
- ✅ **Development/Production**: Separate .env files for different environments
- ✅ **CORS**: Properly configured for deployment

---

## 📋 Local Setup (Windows)

### Option 1: Automated Setup (Recommended)
```bash
# Run setup script
setup.bat
```

### Option 2: Manual Setup

#### Step 1: Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Step 2: Frontend Setup
```bash
cd frontend
npm install
```

#### Step 3: Create Environment Files (already done, but verify):
**backend/.env**
```env
FASTAPI_ENV=development
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

**frontend/.env.development**
```env
REACT_APP_API_URL=http://localhost:8000
```

#### Step 4: Run Application

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate
python -m uvicorn milestone5_api:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

**Access:**
- 🌐 Frontend: http://localhost:3000
- 🔌 Backend API: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs

---

## ☁️ Deployment: Netlify + Render

### Step 1: Push to GitHub
```bash
# Create .gitignore files (already done)
git init
git add .
git commit -m "CreditPathAI - Loan Prediction System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/loan-prediction-system
git push -u origin main
```

### Step 2: Deploy Frontend on Netlify

1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub
3. Click "Add new site" → "Import an existing project"
4. Select your GitHub repo
5. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/build`
6. Add environment variable:
   ```
   REACT_APP_API_URL: https://creditpath-backend.onrender.com
   ```
7. Click "Deploy"

**Result:** `https://creditpath-frontend.netlify.app`

### Step 3: Deploy Backend on Render

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +"
4. Select "PostgreSQL" and create free database
5. Note the connection string
6. Click "New +"
7. Select "Web Service"
8. Connect your GitHub repo
9. Configure:
   - **Name**: `creditpath-backend`
   - **Environment**: `Python 3`
   - **Root directory**: `backend`
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `python -m uvicorn milestone5_api:app --host 0.0.0.0 --port 8000`
10. Add environment variables:
    ```
    CORS_ORIGINS: https://creditpath-frontend.netlify.app
    FASTAPI_ENV: production
    DATABASE_URL: [PostgreSQL connection string]
    ```
11. Click "Create Web Service"

**Result:** `https://creditpath-backend.onrender.com`

### Step 4: Verify Deployment

- 🌐 Visit frontend URL: https://creditpath-frontend.netlify.app
- 🔌 Test backend: https://creditpath-backend.onrender.com/health
- 📚 API Docs: https://creditpath-backend.onrender.com/docs

---

## 🔧 Docker (Alternative)

### Local Docker Deployment
```bash
# Build containers
docker-compose build

# Start services
docker-compose up

# Access:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
# - Database: localhost:5432
```

---

## 🧪 Testing

### Test Backend Endpoints

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Make Prediction:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "income": 50000,
    "loan_amount": 25000,
    "credit_score": 700,
    "months_employed": 36,
    "age": 35,
    "dti_ratio": 0.35,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
  }'
```

---

## 📊 Environment Variables Reference

### Backend (backend/.env)
```env
# Server
FASTAPI_ENV=production
HOST=0.0.0.0
PORT=8000

# CORS (comma-separated)
CORS_ORIGINS=https://creditpath-frontend.netlify.app,http://localhost:3000

# Database (optional)
DATABASE_URL=postgresql://user:password@host:5432/creditpath_db
```

### Frontend (.env.production)
```env
REACT_APP_API_URL=https://creditpath-backend.onrender.com
```

### Frontend (.env.development)
```env
REACT_APP_API_URL=http://localhost:8000
```

---

## ⚠️ Common Issues & Solutions

### Issue: Frontend can't connect to backend
**Solution:** Check `REACT_APP_API_URL` environment variable
```bash
# Development
REACT_APP_API_URL=http://localhost:8000

# Production
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

### Issue: Model files not found
**Solution:** Don't worry! The API has fallback prediction logic
- If models exist: Uses trained ML model
- If models missing: Uses heuristic-based prediction

### Issue: CORS errors in browser
**Solution:** Verify `CORS_ORIGINS` in backend .env
```bash
CORS_ORIGINS=https://your-frontend-url.netlify.app
```

### Issue: Port already in use
**Solution:** Change port in startup command
```bash
# Use different port
python -m uvicorn milestone5_api:app --port 8001
```

---

## 🚀 Quick Deployment Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub (all branches committed)
- [ ] Deployed frontend on Netlify
- [ ] Deployed backend on Render
- [ ] Added environment variables on both platforms
- [ ] Verified health check endpoint: `/health`
- [ ] Tested prediction endpoint
- [ ] Verified CORS configuration
- [ ] Tested end-to-end flow

---

## 📞 Support

**API Documentation:** https://creditpath-backend.onrender.com/docs

**Local Testing:** http://localhost:8000/docs

**Render Status:** https://render.com/dashboard

**Netlify Status:** https://app.netlify.com/

---

## 🎉 You're Ready!

Your CreditPathAI project is now:
- ✅ Fixed and ready for deployment
- ✅ Properly configured for production
- ✅ Optimized for Netlify + Render
- ✅ All errors handled gracefully
- ✅ Ready for your portfolio!

**Next Steps:**
1. Deploy on Netlify + Render (10 minutes)
2. Share your project URL
3. Showcase your AI skills! 🚀
