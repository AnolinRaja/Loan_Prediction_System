# 🚀 Deployment Guide - CreditPathAI

## Prerequisites

You need to have installed:
- **Docker** ([Download](https://www.docker.com/products/docker-desktop))
- **Docker Compose** (included with Docker Desktop)
- **Git** (for version control)

---

## 📦 Option 1: Local Docker Deployment (Recommended for Testing)

### Step 1: Prepare Environment File
```bash
# Create .env file from example
cp .env.example .env

# Edit .env with your preferred values
# (or keep defaults for local development)
```

### Step 2: Build and Run with Docker Compose
```bash
# Build all containers
docker-compose build

# Start all services
docker-compose up

# Or run in background
docker-compose up -d
```

### Step 3: Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database**: localhost:5432

### Step 4: Stop Services
```bash
docker-compose down

# Remove volumes (clears database)
docker-compose down -v
```

---

## ☁️ Option 2: Cloud Deployment

### **A. AWS Deployment**

#### Using AWS ECS (Elastic Container Service)
1. Push Docker images to Amazon ECR (Elastic Container Registry)
2. Create RDS PostgreSQL database
3. Deploy using ECS Fargate
4. Use ALB for load balancing

**Commands:**
```bash
# Create ECR repositories
aws ecr create-repository --repository-name creditpath-backend
aws ecr create-repository --repository-name creditpath-frontend

# Build and push images
docker build -t creditpath-backend ./backend
docker tag creditpath-backend:latest [AWS_ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/creditpath-backend:latest
docker push [AWS_ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/creditpath-backend:latest
```

#### Using AWS Elastic Beanstalk
```bash
# Install EB CLI
pip install awsebcli

# Initialize and deploy
eb init -p docker creditpath-app
eb create creditpath-env
eb deploy
```

---

### **B. Heroku Deployment** (Free/Paid)

**Step 1: Install Heroku CLI**
```bash
# Windows: Download from https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Create Heroku Apps**
```bash
heroku login
heroku create creditpath-backend
heroku create creditpath-frontend
```

**Step 3: Add PostgreSQL Add-on**
```bash
heroku addons:create heroku-postgresql:hobby-dev --app creditpath-backend
```

**Step 4: Deploy Backend**
```bash
cd backend
heroku git:remote -a creditpath-backend
git push heroku main
```

**Step 5: Deploy Frontend**
```bash
cd ../frontend
heroku git:remote -a creditpath-frontend
git push heroku main
```

---

### **C. Azure App Service Deployment**

**Step 1: Install Azure CLI**
```bash
# Windows: Download from https://docs.microsoft.com/cli/azure/install-azure-cli-windows
```

**Step 2: Create Resource Group**
```bash
az group create --name creditpath-rg --location eastus
```

**Step 3: Create Container Registry**
```bash
az acr create --resource-group creditpath-rg --name creditpathreg --sku Basic
```

**Step 4: Push Docker Images**
```bash
az acr build --registry creditpathreg --image creditpath-backend:latest ./backend
az acr build --registry creditpathreg --image creditpath-frontend:latest ./frontend
```

**Step 5: Deploy to App Service**
```bash
az appservice plan create --name creditpath-plan --resource-group creditpath-rg --is-linux --sku B1
az webapp create --resource-group creditpath-rg --plan creditpath-plan --name creditpath-backend --deployment-container-image-name creditpathreg.azurecr.io/creditpath-backend:latest
```

---

### **D. DigitalOcean App Platform** (Simple & Affordable)

**Step 1: Connect GitHub**
- Go to DigitalOcean App Platform
- Connect your GitHub repository

**Step 2: Configure App Spec**
Create `app.yaml`:
```yaml
name: creditpath
services:
- name: backend
  github:
    repo: your-username/repo-name
    branch: main
  build_command: pip install -r requirements.txt
  run_command: uvicorn milestone5_api:app --host 0.0.0.0 --port 8080
  envs:
  - key: DATABASE_URL
    scope: RUN_AND_BUILD_TIME
    value: ${db.connection_string}

- name: frontend
  github:
    repo: your-username/repo-name
    branch: main
  build_command: cd frontend && npm install && npm run build
  run_command: npm serve -s build

databases:
- name: db
  engine: PG
  version: "12"
```

**Step 3: Deploy**
- Click "Launch App"

---

## 🐳 Docker Commands Reference

```bash
# Build images
docker-compose build

# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Access PostgreSQL shell
docker-compose exec postgres psql -U creditpath_user -d creditpath_db

# Remove everything (containers, volumes, networks)
docker-compose down -v
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
# Database
DB_USER=creditpath_user
DB_PASSWORD=your_secure_password
DB_NAME=creditpath_db

# FastAPI
FASTAPI_ENV=production
DATABASE_URL=postgresql://creditpath_user:your_password@postgres:5432/creditpath_db

# CORS
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# React API
REACT_APP_API_URL=http://localhost:8000
```

---

## 📊 Architecture After Deployment

```
┌─────────────────────────────────────────────────┐
│          User Browser                           │
│  (https://yourdomain.com:3000)                 │
└──────────────────┬──────────────────────────────┘
                   │
        ┌──────────▼──────────┐
        │   Frontend (React)  │ Port: 3000
        │   (Static Files)    │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │  Backend (FastAPI)  │ Port: 8000
        │ (API Endpoints)     │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │  PostgreSQL DB      │ Port: 5432
        │  (Data Storage)     │
        └─────────────────────┘
```

---

## 🚨 Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild
docker-compose build --no-cache
```

### Database connection error
```bash
# Verify database is running
docker-compose exec postgres pg_isready

# Check connection string in logs
docker-compose logs backend | grep DATABASE_URL
```

### Port already in use
```bash
# Change port in docker-compose.yml
# For example: "5433:5432" for PostgreSQL
```

### Frontend can't connect to backend
```bash
# Update REACT_APP_API_URL in frontend/.env
REACT_APP_API_URL=http://your-backend-url:8000
```

---

## 📋 Deployment Comparison Table

| Platform | Cost | Ease | Scalability | Best For |
|---|---|---|---|---|
| **Docker Local** | Free | ⭐⭐⭐ | Low | Development |
| **Heroku** | $7-50/mo | ⭐⭐⭐⭐⭐ | Medium | Startups |
| **AWS ECS** | $20-100+/mo | ⭐⭐ | High | Enterprise |
| **Azure** | $20-100+/mo | ⭐⭐ | High | Enterprise |
| **DigitalOcean** | $5-50/mo | ⭐⭐⭐⭐ | Medium | Small Teams |
| **Render** | $7-50/mo | ⭐⭐⭐⭐⭐ | Medium | Startups |

---

## 🎯 Recommended Path

**For Quick Testing:**
→ Use **Docker Compose locally**

**For Production (Small Budget):**
→ Use **Heroku** or **DigitalOcean**

**For Enterprise (Scalability):**
→ Use **AWS ECS** or **Azure**

---

## 📝 Next Steps

1. Install Docker Desktop
2. Copy `.env.example` to `.env`
3. Run `docker-compose up`
4. Access http://localhost:3000
5. Choose your cloud platform
6. Follow the platform-specific deployment steps

