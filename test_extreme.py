import urllib.request
import json

BASE_URL = "http://localhost:8000/predict"

def post_request(url, data):
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())

print("\n" + "="*80)
print("🚨 EXTREME CASE TEST - UNREALISTIC LOAN AMOUNTS")
print("="*80)

# Test 1: EXTREME - 50M loan on 50K income (1,000% ratio!)
print("\n📊 TEST 1: EXTREME MISMATCH - $50M Loan on $50K Income")
print("-" * 80)
extreme = {
    "income": 50000,
    "loan_amount": 50000000,
    "credit_score": 700,
    "months_employed": 24,
    "age": 35,
    "dti_ratio": 50,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $50K, Loan $50M (100,000%!), Credit 700, DTI 50%")
print("Expected: HIGH RISK (immediate rejection)")
resp = post_request(BASE_URL, extreme)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 2: VERY HIGH - 500K loan on 50K income
print("📊 TEST 2: VERY HIGH - $500K Loan on $50K Income")
print("-" * 80)
very_high = {
    "income": 50000,
    "loan_amount": 500000,
    "credit_score": 700,
    "months_employed": 24,
    "age": 35,
    "dti_ratio": 50,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $50K, Loan $500K (1,000%), Credit 700, DTI 50%")
print("Expected: HIGH RISK")
resp = post_request(BASE_URL, very_high)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 3: HIGH but reasonable - 100K loan on 50K income
print("📊 TEST 3: HIGH BUT REASONABLE - $100K Loan on $50K Income")
print("-" * 80)
high_reasonable = {
    "income": 50000,
    "loan_amount": 100000,
    "credit_score": 750,
    "months_employed": 36,
    "age": 40,
    "dti_ratio": 35,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $50K, Loan $100K (200%), Good Credit 750, DTI 35%, Age 40")
print("Expected: HIGH RISK")
resp = post_request(BASE_URL, high_reasonable)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

# Test 4: Normal - 50K loan on 100K income
print("📊 TEST 4: NORMAL - $50K Loan on $100K Income")
print("-" * 80)
normal = {
    "income": 100000,
    "loan_amount": 50000,
    "credit_score": 750,
    "months_employed": 36,
    "age": 40,
    "dti_ratio": 25,
    "education": 1,
    "employment_type": 1,
    "marital_status": 1,
    "has_mortgage": 0,
    "has_cosigner": 0
}
print("Input: Income $100K, Loan $50K (50%), Credit 750, DTI 25%, Age 40")
print("Expected: LOW RISK")
resp = post_request(BASE_URL, normal)
print(f"✓ Probability: {resp['probability']:.3f}")
print(f"✓ Classification: {resp['risk']}")
print(f"✓ Action: {resp['action']}\n")

print("="*80)
print("✅ ALL EXTREME TESTS COMPLETE!")
print("="*80 + "\n")
