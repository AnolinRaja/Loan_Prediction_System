import urllib.request
import json

BASE_URL = "http://localhost:8000/predict"

def post_request(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())

print("\n" + "="*75)
print("🎯 IMPROVED THRESHOLD TEST - WITH BETTER CLASSIFICATION")
print("="*75)

# Test 1: Very High Risk - Massive Loan
print("\n📊 TEST 1: MASSIVE LOAN (300% of income)")
print("-" * 75)
massive_loan = {
    "income": 40000,
    "loan_amount": 120000,
    "credit_score": 580,
    "months_employed": 3,
    "age": 23,
    "dti_ratio": 80,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $40K, Loan $120K (300%!), Credit 580, DTI 80%, Age 23")
resp = post_request(BASE_URL, massive_loan)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 2: High Risk - Large Loan
print("📊 TEST 2: LARGE LOAN (100% of income)")
print("-" * 75)
large_loan = {
    "income": 50000,
    "loan_amount": 50000,
    "credit_score": 620,
    "months_employed": 6,
    "age": 28,
    "dti_ratio": 55,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $50K, Loan $50K (100%), Credit 620, DTI 55%, Age 28")
resp = post_request(BASE_URL, large_loan)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 3: Medium Risk - Moderate Loan
print("📊 TEST 3: MODERATE LOAN (50% of income)")
print("-" * 75)
moderate_loan = {
    "income": 75000,
    "loan_amount": 37500,
    "credit_score": 680,
    "months_employed": 18,
    "age": 32,
    "dti_ratio": 42,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $75K, Loan $37.5K (50%), Credit 680, DTI 42%, Age 32")
resp = post_request(BASE_URL, moderate_loan)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 4: Low Risk - Small Loan
print("📊 TEST 4: SMALL LOAN (20% of income)")
print("-" * 75)
small_loan = {
    "income": 150000,
    "loan_amount": 30000,
    "credit_score": 780,
    "months_employed": 60,
    "age": 42,
    "dti_ratio": 12,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $150K, Loan $30K (20%), Credit 780, DTI 12%, Age 42")
resp = post_request(BASE_URL, small_loan)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

print("="*75)
print("✅ ALL TESTS COMPLETE - Check results above!")
print("="*75 + "\n")
