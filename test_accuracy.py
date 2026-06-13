import urllib.request
import json

BASE_URL = "http://localhost:8000/predict"

def post_request(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())

# Scenario 1: HIGH RISK (already tested, but showing again)
print("\n" + "="*70)
print("SCENARIO 1: HIGH RISK - Large Loan with Poor Credit")
print("="*70)
high_risk = {
    "income": 50000,
    "loan_amount": 100000,
    "credit_score": 600,
    "months_employed": 6,
    "age": 25,
    "dti_ratio": 60,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $50K, Loan $100K (200%!), Credit 600, DTI 60%")
resp = post_request(BASE_URL, high_risk)
result = resp
print(f"Output: Probability {result['probability']:.2f} = {result['risk']}")
print(f"Action: {result['action']}\n")

# Scenario 2: LOW RISK
print("="*70)
print("SCENARIO 2: LOW RISK - Small Loan with Good Credit")
print("="*70)
low_risk = {
    "income": 150000,
    "loan_amount": 30000,
    "credit_score": 780,
    "months_employed": 60,
    "age": 40,
    "dti_ratio": 15,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $150K, Loan $30K (20%), Credit 780, DTI 15%, Age 40")
resp = post_request(BASE_URL, low_risk)
result = resp
print(f"Output: Probability {result['probability']:.2f} = {result['risk']}")
print(f"Action: {result['action']}\n")

# Scenario 3: MEDIUM RISK
print("="*70)
print("SCENARIO 3: MEDIUM RISK - Balanced Profile")
print("="*70)
medium_risk = {
    "income": 75000,
    "loan_amount": 50000,
    "credit_score": 700,
    "months_employed": 24,
    "age": 35,
    "dti_ratio": 38,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $75K, Loan $50K (67%), Credit 700, DTI 38%, Age 35")
resp = post_request(BASE_URL, medium_risk)
result = resp
print(f"Output: Probability {result['probability']:.2f} = {result['risk']}")
print(f"Action: {result['action']}\n")

print("="*70)
print("✅ ACCURACY TEST COMPLETE!")
print("="*70)
