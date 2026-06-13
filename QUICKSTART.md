# 🚀 QUICKSTART - CreditPathAI Deployment

**⏱️ Time to deployment: 15 minutes**

---

## 🔥 Fastest Path to Production

### Option A: Local Testing (2 minutes)

**Windows:**
```bash
cd "e:\projects_own\loan prediction system"
setup.bat
```

**Mac/Linux:**
```bash
cd "e:\projects_own\loan prediction system"
bash setup.sh
```

Then open:
- 🌐 Frontend: http://localhost:3000
- 🔌 Backend: http://localhost:8000/docs

---

### Option B: Free Cloud Deployment (15 minutes)

#### Step 1️⃣: GitHub
```bash
git push origin main
```

#### Step 2️⃣: Netlify (Frontend)
1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub
3. New site → Import → Select your repo
4. Build settings:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish: `frontend/build`
5. Deploy → ✅ Done in 2 min

#### Step 3️⃣: Render (Backend)
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. PostgreSQL → New Database → Free tier ✅
4. Web Service → GitHub → Select repo
5. Settings:
   - Name: `creditpath-backend`
   - Root: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `python -m uvicorn milestone5_api:app --host 0.0.0.0 --port 8000`
   - Env vars:
     ```
     CORS_ORIGINS: https://your-frontend.netlify.app
     ```
6. Deploy → ✅ Done in 5 min

#### Step 4️⃣: Link Frontend to Backend
1. Update frontend `.env.production`
2. Set: `REACT_APP_API_URL=https://your-backend.onrender.com`
3. Push to GitHub → Netlify auto-redeploys ✅

---

## 🎯 What's Already Fixed

✅ API URL dynamically configured  
✅ Model loading works or uses fallback  
✅ Environment variables all set up  
✅ Docker containers secure  
✅ Error handling comprehensive  
✅ Documentation complete  

---

## 📊 Your Live URLs (After Deployment)

```
🌐 Frontend: https://your-site.netlify.app
🔌 API: https://your-site.onrender.com
📚 Docs: https://your-site.onrender.com/docs
```

---

## ✅ Verification (After Deployment)

**Test 1: API Health**
```bash
curl https://your-api.onrender.com/health
# Should return: {"status": "ok", "model_loaded": true}
```

**Test 2: Frontend Access**
Visit `https://your-site.netlify.app` → Form should load ✅

**Test 3: Prediction**
Fill form → Click predict → See results ✅

---

## 🆘 Common Issues

### Frontend can't connect
→ Check env variable `REACT_APP_API_URL` in Netlify settings

### Backend won't start
→ Check `CORS_ORIGINS` in Render env variables

### Still having issues?
→ Read `DEPLOYMENT_FIXED.md` for detailed help

---

## 📋 Checklist Before Deployment

- [ ] All code pushed to GitHub
- [ ] GitHub repo is public
- [ ] Created Netlify account
- [ ] Created Render account
- [ ] Ready to deploy!

---

**Ready? Go to step 2️⃣ and deploy now!** 🚀

---

**Questions?** See detailed guides:
- Full guide: `DEPLOYMENT_FIXED.md`
- Free options: `FREE_DEPLOYMENT.md`
- What was fixed: `REPAIR_SUMMARY.md`
- Complete project info: `README.md`
