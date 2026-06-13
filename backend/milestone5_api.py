from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import logging
import os
import math
import numpy as np
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(
    title="CreditPathAI API",
    description="AI-powered Loan Risk Prediction System",
    version="1.0.0"
)

# Configure CORS to allow frontend to communicate with backend
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Get the current directory
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "model.pkl"
PIPELINE_PATH = BASE_DIR / "pipeline.pkl"

# Load model and pipeline with graceful fallback
model = None
pipeline = None
model_loaded = False

try:
    if MODEL_PATH.exists() and PIPELINE_PATH.exists():
        model = joblib.load(str(MODEL_PATH))
        pipeline = joblib.load(str(PIPELINE_PATH))
        model_loaded = True
        logger.info("Model and pipeline loaded successfully.")
    else:
        logger.warning(f"Model files not found at {MODEL_PATH} or {PIPELINE_PATH}. Using fallback prediction method.")
        model_loaded = False
except Exception as e:
    logger.error(f"Error loading model or pipeline: {e}")
    logger.warning("Will use fallback prediction method.")
    model_loaded = False

# Define simplified Pydantic schema for frontend input
class SimplifiedLoanApplication(BaseModel):
    income: float
    loan_amount: float
    credit_score: int
    months_employed: int
    age: int
    dti_ratio: float
    education: int = 1
    employment_type: int = 1
    marital_status: int = 1
    has_mortgage: int = 0
    has_cosigner: int = 0

# Full schema for internal processing (with defaults)
class LoanApplication(BaseModel):
    LoanID: int = 0
    Age: int = 40
    LoanAmount: float
    Income: float
    CreditScore: int
    MonthsEmployed: int
    NumCreditLines: int = 3
    InterestRate: float = 5.0
    LoanTerm: int = 60
    DTIRatio: float = 0.35
    Education: int = 1
    EmploymentType: int = 1
    MaritalStatus: int = 1
    HasMortgage: int = 0
    HasDependents: int = 0
    LoanPurpose: int = 1
    HasCoSigner: int = 0
    loan_income_ratio: float = 0.0
    credit_utilization: float
    interest_burden: float
    employment_stability: float
    high_dti_flag: int
    credit_score_Poor: int
    credit_score_Average: int
    credit_score_Good: int
    credit_score_Excellent: int
    log_income: float
    income_loan_interaction: float

# Define thresholds for risk classification
HIGH_RISK_THRESHOLD = 0.95  # Increased threshold for High Risk
MEDIUM_RISK_THRESHOLD = 0.7  # Adjusted threshold for Medium Risk

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "CreditPathAI API is running",
        "status": "healthy",
        "model_status": "loaded" if model_loaded else "using_fallback"
    }

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": model_loaded}



# Prediction endpoint - SIMPLIFIED VERSION
@app.post("/predict")
async def predict(input_data: SimplifiedLoanApplication):
    try:
        # Extract all the input features
        income = input_data.income
        loan_amount = input_data.loan_amount
        credit_score = input_data.credit_score
        months_employed = input_data.months_employed
        age = input_data.age
        dti_ratio = input_data.dti_ratio
        education = input_data.education
        employment_type = input_data.employment_type
        marital_status = input_data.marital_status
        has_mortgage = input_data.has_mortgage
        has_cosigner = input_data.has_cosigner
        
        # Create a simple feature array with all available features
        features = [[
            income,
            loan_amount, 
            credit_score,
            months_employed,
            age,
            dti_ratio,
            education,
            employment_type,
            marital_status,
            has_mortgage,
            has_cosigner,
            loan_amount / income,  # loan_income_ratio
            math.log(income) if income > 0 else 0,  # log_income
        ]]
        
        # Convert to numpy array
        import numpy as np
        X = np.array(features, dtype=float)
        
        # Try to predict with the model
        try:
            if model_loaded and model is not None:
                probabilities = model.predict_proba(X)[0]
                prediction_probability = float(probabilities[1])
                logger.info(f"Model prediction: {prediction_probability}")
            else:
                raise Exception("Model not loaded")
        except Exception as e:
            # If model fails, use an improved heuristic considering multiple factors
            logger.warning(f"Model prediction failed: {e}. Using improved fallback method.")
            
            # EXTREME CASE: Check for unrealistic loan-to-income ratios first
            loan_to_income = (loan_amount / income * 100) if income > 0 else 100
            if loan_to_income > 300:
                # Loan is more than 3x annual income - this is almost certainly HIGH RISK
                prediction_probability = min(0.95, 0.80 + (loan_to_income / 1000))
                logger.warning(f"EXTREME LOAN-TO-INCOME RATIO: {loan_to_income:.1f}% - Setting HIGH RISK")
            else:
                # 1. Credit Score Risk (30% weight)
                if credit_score >= 750:
                    credit_risk = 0.1
                elif credit_score >= 700:
                    credit_risk = 0.25
                elif credit_score >= 650:
                    credit_risk = 0.45
                elif credit_score >= 600:
                    credit_risk = 0.65
                else:
                    credit_risk = 0.85
                
                # 2. Debt-to-Income Ratio Risk (25% weight)
                if dti_ratio <= 20:
                    dti_risk = 0.15
                elif dti_ratio <= 35:
                    dti_risk = 0.35
                elif dti_ratio <= 50:
                    dti_risk = 0.60
                else:
                    dti_risk = 0.85
                
                # 3. Loan-to-Income Ratio Risk (25% weight) - MOST CRITICAL FACTOR
                if loan_to_income <= 25:
                    lti_risk = 0.10
                elif loan_to_income <= 50:
                    lti_risk = 0.30
                elif loan_to_income <= 75:
                    lti_risk = 0.60
                elif loan_to_income <= 100:
                    lti_risk = 0.80
                else:
                    lti_risk = 0.90
                
                # 4. Employment Stability Risk (10% weight)
                if months_employed >= 36:
                    employment_risk = 0.15
                elif months_employed >= 12:
                    employment_risk = 0.40
                elif months_employed >= 6:
                    employment_risk = 0.65
                else:
                    employment_risk = 0.80
                
                # 5. Age & Experience Risk (10% weight)
                if age >= 30:
                    age_risk = 0.20
                elif age >= 25:
                    age_risk = 0.35
                else:
                    age_risk = 0.55
                
                # Weighted average of all factors
                prediction_probability = (
                    credit_risk * 0.30 +
                    dti_risk * 0.25 +
                    lti_risk * 0.25 +
                    employment_risk * 0.10 +
                    age_risk * 0.10
                )
                prediction_probability = min(0.95, max(0.05, prediction_probability))
        
        # Determine risk category (adjusted thresholds for better classification)
        if prediction_probability > 0.55:
            risk = "High"
            action = "High Risk - Immediate Recovery Action Required"
        elif prediction_probability > 0.30:
            risk = "Medium"
            action = "Medium Risk - Monitor Closely and Review Regularly"
        else:
            risk = "Low"
            action = "Low Risk - Approved for Loan"

        # Return response
        return {
            "probability": round(prediction_probability, 4),
            "risk": risk,
            "action": action,
            "details": {
                "credit_score": credit_score,
                "dti_ratio": dti_ratio,
                "age": age,
                "employment_months": months_employed
            }
        }

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        logger.exception("Full exception trace:")
        # Return a valid response even if there's an error
        return {
            "probability": 0.5,
            "risk": "Unknown",
            "action": "Unable to process - please check input data",
            "details": {}
        }