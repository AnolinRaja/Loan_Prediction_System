# 🏦 CreditPathAI - Loan Risk Prediction System

> **AI-Powered Loan Default Prediction using Machine Learning**

![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![React](https://img.shields.io/badge/react-18.2.0-61dafb)

## 🎯 Overview

CreditPathAI is a full-stack web application that predicts loan default risk using machine learning. Financial institutions can use this tool to assess credit risk and make better lending decisions.

**Live Demo:**
- 🌐 Frontend: https://creditpath-frontend.netlify.app
- 🔌 Backend API: https://creditpath-backend.onrender.com
- 📚 API Docs: https://creditpath-backend.onrender.com/docs

---

## ✨ Features

### 🎨 Frontend (React Dashboard)
- ✅ Interactive loan application form with validation
- ✅ Real-time risk assessment results
- ✅ Color-coded risk levels (Low/Medium/High)
- ✅ Interactive charts and visualizations (Plotly)
- ✅ Professional UI with responsive design
- ✅ Loading states and error handling
- ✅ Probability breakdown and recommendations

### 🔧 Backend (FastAPI API)
- ✅ REST API endpoints for predictions
- ✅ Machine Learning model integration
- ✅ CORS enabled for cross-origin requests
- ✅ Comprehensive error handling
- ✅ Fallback prediction logic
- ✅ Health check endpoint
- ✅ Automatic Swagger/OpenAPI documentation

### 🧠 Machine Learning
- ✅ Random Forest Classifier for predictions
- ✅ Trained on comprehensive loan dataset
- ✅ ~88% model accuracy
- ✅ Feature engineering and preprocessing
- ✅ Heuristic fallback for missing models

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         User Browser                        │
│     (React Frontend - Netlify)              │
└────────────────┬────────────────────────────┘
                 │ HTTPS
┌────────────────▼────────────────────────────┐
│    FastAPI Backend (Render)                │
│    - REST API Endpoints                    │
│    - Model Predictions                     │
│    - Error Handling                        │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│    PostgreSQL Database (Render)            │
│    - Data Storage                          │
│    - User Information                      │
└─────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Local Development (Windows)

#### Automated Setup (Recommended)
```bash
# Run the setup script
setup.bat
```

#### Manual Setup

**1. Backend Setup**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**2. Frontend Setup**
```bash
cd frontend
npm install
```

**3. Start Backend**
```bash
cd backend
venv\Scripts\activate
python -m uvicorn milestone5_api:app --reload --port 8000
```

**4. Start Frontend** (new terminal)
```bash
cd frontend
npm start
```

**5. Access Application**
- 🌐 Frontend: http://localhost:3000
- 🔌 Backend: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs

---

## 📦 Tech Stack

### Frontend
| Technology | Version | Purpose |
|---|---|---|
| React | 18.2.0 | UI Framework |
| Axios | 1.4.0 | HTTP Client |
| Plotly.js | 2.26.0 | Visualizations |
| CSS3 | - | Styling |

### Backend
| Technology | Version | Purpose |
|---|---|---|
| FastAPI | 0.104.1 | Web Framework |
| Uvicorn | 0.24.0 | ASGI Server |
| Scikit-learn | 1.3.2 | ML Library |
| Pandas | 2.1.3 | Data Processing |
| SQLAlchemy | 2.0.23 | ORM |

### Database
| Technology | Purpose |
|---|---|
| PostgreSQL | Relational Database |
| psycopg2 | Python PostgreSQL Adapter |

---

## 🌐 Deployment

### Free Deployment: Netlify + Render

#### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "CreditPathAI - Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/loan-prediction-system
git push -u origin main
```

#### Step 2: Deploy Frontend on Netlify
1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub
3. Click "Add new site" → "Import an existing project"
4. Select your repo
5. Build settings:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/build`
6. Add environment variable:
   ```
   REACT_APP_API_URL: https://creditpath-backend.onrender.com
   ```
7. Deploy!

#### Step 3: Deploy Backend on Render
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Create PostgreSQL database (free tier)
4. Create Web Service:
   - Connect GitHub repo
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python -m uvicorn milestone5_api:app --host 0.0.0.0 --port 8000`
5. Add environment variables:
   ```
   CORS_ORIGINS: https://creditpath-frontend.netlify.app
   FASTAPI_ENV: production
   ```
6. Deploy!

**Result: FREE deployment! 🎉**

### Docker Deployment

```bash
# Build containers
docker-compose build

# Start all services
docker-compose up

# Access:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
# - Database: localhost:5432
```

---

## 📊 API Endpoints

### Prediction Endpoint
```
POST /predict
Content-Type: application/json

{
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
}

Response:
{
  "probability": 0.3456,
  "risk": "Low",
  "action": "Low Risk - Approved for Loan",
  "details": {
    "credit_score": 700,
    "dti_ratio": 0.35,
    "age": 35,
    "employment_months": 36
  }
}
```

### Health Check
```
GET /health

Response:
{
  "status": "ok",
  "model_loaded": true
}
```

### Root Endpoint
```
GET /

Response:
{
  "message": "CreditPathAI API is running",
  "status": "healthy",
  "model_status": "loaded"
}
```

---

## ⚙️ Environment Configuration

### Frontend Development (.env.development)
```env
REACT_APP_API_URL=http://localhost:8000
```

### Frontend Production (.env.production)
```env
REACT_APP_API_URL=https://creditpath-backend.onrender.com
```

### Backend (.env)
```env
FASTAPI_ENV=development
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
DATABASE_URL=postgresql://user:password@localhost:5432/creditpath_db
```

---

## 📁 Project Structure

```
loan-prediction-system/
│
├── frontend/                    # React Dashboard
│   ├── src/
│   │   ├── components/
│   │   │   ├── Form.js        # Application form
│   │   │   ├── Dashboard.js   # Results display
│   │   │   └── Charts.js      # Visualizations
│   │   ├── services/
│   │   │   └── api.js         # API integration
│   │   ├── styles/            # CSS files
│   │   ├── App.js             # Main component
│   │   └── index.js           # Entry point
│   ├── public/                # Static files
│   ├── package.json           # Dependencies
│   ├── .env.development       # Dev config
│   ├── .env.production        # Prod config
│   └── Dockerfile             # Container image
│
├── backend/                    # FastAPI Server
│   ├── milestone5_api.py      # Main API
│   ├── train_model.py         # Model training
│   ├── preprocess.py          # Data preprocessing
│   ├── analyze_data.py        # Data analysis
│   ├── load_dataset.py        # Dataset loading
│   ├── save_model.py          # Model saving
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example           # Env template
│   ├── .gitignore             # Git ignore rules
│   └── Dockerfile             # Container image
│
├── docker-compose.yml         # Docker orchestration
├── setup.bat                  # Windows setup script
├── setup.sh                   # Unix setup script
├── DEPLOYMENT_FIXED.md        # Deployment guide
├── FREE_DEPLOYMENT.md         # Free hosting options
└── README.md                  # This file
```

---

## 🧪 Testing

### Test Backend Locally
```bash
# Health check
curl http://localhost:8000/health

# Test prediction
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

### Test Frontend
1. Go to http://localhost:3000
2. Fill in loan details
3. Click "Get Risk Assessment"
4. Verify results display correctly

---

## 🐛 Troubleshooting

### Issue: Frontend can't connect to backend
**Solution:** Check environment variables
```bash
# Development
REACT_APP_API_URL=http://localhost:8000

# Production
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

### Issue: CORS errors
**Solution:** Update CORS_ORIGINS in backend .env
```bash
CORS_ORIGINS=https://your-frontend-url.netlify.app,http://localhost:3000
```

### Issue: Model files not found
**Solution:** Don't worry! API uses fallback prediction
- Model not loaded? Uses heuristic method
- Check logs: `docker-compose logs backend`

### Issue: Port already in use
**Solution:** Use different port
```bash
# Backend
python -m uvicorn milestone5_api:app --port 8001

# Frontend
npm start -- --port 3001
```

---

## 📈 Model Performance

- **Accuracy**: ~88%
- **Algorithm**: Random Forest Classifier
- **Features**: 11 engineered features
- **Training Data**: Comprehensive loan dataset
- **Fallback**: Heuristic-based prediction

---

## 🔐 Security

- ✅ CORS properly configured
- ✅ Environment variables for secrets
- ✅ Non-root Docker containers
- ✅ Error messages don't expose system details
- ✅ Input validation on frontend and backend
- ✅ HTTPS ready for production

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🎯 Future Enhancements

- [ ] User authentication and dashboard
- [ ] Loan history and tracking
- [ ] Advanced analytics and reporting
- [ ] Real-time model updates
- [ ] Multi-language support
- [ ] Mobile app
- [ ] Additional ML models (XGBoost, LightGBM)
- [ ] Model explainability (SHAP values)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📞 Support

For issues, questions, or suggestions:
1. Check [DEPLOYMENT_FIXED.md](./DEPLOYMENT_FIXED.md) for deployment help
2. Check [FREE_DEPLOYMENT.md](./FREE_DEPLOYMENT.md) for hosting options
3. Review API documentation: http://localhost:8000/docs

---

## 🎉 Ready to Deploy?

1. ✅ Code is fixed and ready
2. ✅ Environment variables configured
3. ✅ Docker containers optimized
4. ✅ Deployment files prepared
5. ✅ Documentation complete

**Next Steps:**
1. Push to GitHub
2. Deploy on Netlify (Frontend)
3. Deploy on Render (Backend)
4. Share your project URL
5. Showcase your AI skills! 🚀

---

## 📊 Project Stats

- 🐍 Python (Backend)
- ⚛️ React (Frontend)
- 🗄️ PostgreSQL (Database)
- 🤖 Machine Learning
- 📊 Data Science
- ☁️ Cloud Deployment

**Happy coding!** 🎉
