# 🔐 Security & Sensitive Data Management

## Overview

This document outlines what sensitive data is protected from git tracking and how to manage environment variables locally.

---

## 🚨 Protected Sensitive Data

### Environment Variables (Never Tracked)
All `.env` files are **excluded from git** and never committed:

```
❌ NEVER COMMITTED:
.env                          # Root environment file
.env.local                     # Local overrides
.env.*.local                   # Environment-specific local files
backend/.env                   # Backend secrets
backend/.env.local             # Backend local overrides
frontend/.env                  # Frontend secrets
frontend/.env.development.local
frontend/.env.test.local
frontend/.env.production.local
```

### Credentials & Keys
```
❌ NEVER COMMITTED:
*.key                          # Private keys
*.pem                          # Certificate files
*.p12, *.pfx                   # Password-protected certificates
secrets/                       # Secret folders
API_KEYS                       # All API credentials
DATABASE_PASSWORDS             # Database credentials
JWT_SECRETS                    # JWT signing keys
```

### Database Files
```
❌ NEVER COMMITTED:
*.db                           # SQLite databases
*.sqlite, *.sqlite3            # Local databases
database.db                    # Development database
```

### Data Files
```
❌ NEVER COMMITTED (by design):
*.csv                          # Data files
Loan_default.csv               # Original dataset
final_features.csv             # Processed features
*.xlsx, *.xls                  # Excel files
*.parquet                      # Parquet data files
data/, datasets/               # Data directories
```

### Code Artifacts
```
❌ NEVER COMMITTED:
__pycache__/                   # Python bytecode
*.pyc, *.pyo, *.pyd            # Python compiled files
node_modules/                  # NPM packages
venv/, env/, ENV/              # Virtual environments
.pytest_cache/                 # Test cache
.coverage/                     # Coverage reports
build/, dist/                  # Build artifacts
```

---

## ✅ What IS Tracked

### Safe Configuration Files
```
✅ COMMITTED:
.env.example                   # Template with placeholders
.env.development               # Non-secret dev config
.env.production                # Non-secret prod config
.gitignore                     # Git ignore rules
docker-compose.yml             # Container orchestration
Dockerfile                     # Container images
requirements.txt               # Python dependencies
package.json                   # Node dependencies
```

---

## 🔧 Local Setup Instructions

### Step 1: Create Backend Environment File

**Location:** `backend/.env`

```bash
# Copy the template
cp backend/.env.example backend/.env

# Edit with your values
# backend/.env content:
```

```ini
FASTAPI_ENV=development
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
DATABASE_URL=postgresql://username:password@localhost:5432/creditpath_db
HOST=0.0.0.0
PORT=8000
```

### Step 2: Create Frontend Environment File

**Location:** `frontend/.env.development`

```bash
# Copy the template
cp frontend/.env.example frontend/.env.development

# Edit with your values
# frontend/.env.development content:
```

```ini
REACT_APP_API_URL=http://localhost:8000
```

### Step 3: Create Production Frontend Environment (for Netlify)

**Location:** `frontend/.env.production` (local reference only)

```ini
REACT_APP_API_URL=https://your-backend.onrender.com
```

---

## 🚀 Deployment: Environment Variables

### Netlify (Frontend)

Set these in Netlify Dashboard → Site Settings → Environment:

```
REACT_APP_API_URL = https://your-backend.onrender.com
```

Build command: `npm run build`
Base directory: `frontend/`
Publish directory: `frontend/build/`

### Render (Backend)

Set these in Render Dashboard → Service → Environment:

```
FASTAPI_ENV=production
CORS_ORIGINS=https://your-frontend.netlify.app
DATABASE_URL=<auto-provided by PostgreSQL service>
PORT=8000
```

Build command: `pip install -r requirements.txt`
Start command: `python -m uvicorn milestone5_api:app --host 0.0.0.0 --port 8000`

---

## 🔍 Verification Checklist

Before pushing to GitHub:

- [ ] No `.env` files in git status
- [ ] No database files (`.db`, `.sqlite3`) in git status
- [ ] No CSV data files in git status
- [ ] No private keys or certificates in git status
- [ ] `.gitignore` contains all sensitive patterns
- [ ] `.env.example` files exist with safe placeholders

**Verify with:**
```bash
git status                 # Check for uncommitted sensitive files
git ls-files               # List all tracked files (should not include .env)
grep -r "password" .       # Search for hardcoded passwords
```

---

## 🛡️ Security Best Practices

### Development
1. ✅ Use `.env.local` files for local secrets
2. ✅ Never commit `.env` files
3. ✅ Keep database credentials in `.env` only
4. ✅ Use strong passwords for local databases
5. ✅ Rotate API keys regularly

### Production
1. ✅ Use platform-provided secret management (Netlify/Render secrets)
2. ✅ Never commit production credentials
3. ✅ Use environment-specific secrets
4. ✅ Enable CORS only for trusted origins
5. ✅ Rotate database passwords regularly
6. ✅ Use SSL/TLS for all communications

### Git Security
1. ✅ Review files before committing: `git diff --staged`
2. ✅ Use `.gitignore` patterns comprehensively
3. ✅ Check for secrets before pushing: `git log -p | grep -i password`
4. ✅ Clean git cache of accidentally committed files: `git rm --cached <file>`

---

## 📋 `.gitignore` Coverage

### Root `.gitignore`
- Environment files (.env, .env.*)
- Sensitive certificates (*.key, *.pem)
- Data files (*.csv, datasets/)
- System files (.DS_Store, etc.)

### Frontend `.gitignore`
- Node modules and dependencies
- Build outputs
- Environment-specific secrets
- IDE and cache files

### Backend `.gitignore`
- Python virtual environments (venv/)
- Python cache (__pycache__, *.pyc)
- Build artifacts
- Test coverage reports
- Environment-specific secrets

---

## ⚠️ If You Accidentally Commit Secrets

### Immediate Action
```bash
# Remove from git history (before pushing)
git reset --soft HEAD~1        # Undo last commit
git reset HEAD .env            # Unstage the file
git add --update .gitignore    # Add to gitignore if not there
git commit -m "Security: Removed sensitive .env file"

# For already-pushed commits to GitHub:
# 1. Invalidate compromised credentials immediately
# 2. Use: git-filter-branch or BFG Repo-Cleaner (advanced)
# 3. Contact platform if credentials exposed
```

---

## 📞 Support

For security concerns or questions:
1. Review this file
2. Check `.env.example` for template structure
3. Verify `.gitignore` patterns cover all sensitive data
4. Test with: `git status` and `git ls-files`

---

**Last Updated:** 2024
**Status:** ✅ All sensitive data protected
