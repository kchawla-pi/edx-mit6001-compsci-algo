"""
The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal
---
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

"""
idx = beginning of month idx, starts at 0.
b = balance, which is
    b[idx] = balance
p = minMonthlyPayment, which is
    p[idx] = b[idx]*minMonthlyPaymentRate(mmpr)
ub = unpaid balance, which is
    ub[idx] = b[idx] - p[idx]

b[idx] = balance
p[idx] = b[idx]*minMonthlyPaymentRate(mmpr)
ub[idx] = b[idx] - p[idx]

b[idx+1] = ub[idx] + ub[idx]*annualInterestRate/12 (iR/12)
p[idx+1] = ub[idx+1]
ub[idx+1] = b[idx+1] - p[idx+1]

b[idx+2] = ub[idx+1] + ub[idx+1]*iR/12
"""
# balance = 5000
# monthlyPaymentRate = 0.02
# annualInterestRate = 0.18
# balance = 484
b = [balance]
iR = annualInterestRate
mPR = monthlyPaymentRate
p = []
ub = []
for idx in range(0, 12):
    month_end_payment = round(b[idx] * mPR, 2)
    p.append(month_end_payment)  # minimum payment for month of idx
    
    month_end_unpaid_balance = round(b[idx] - p[idx], 2)
    ub.append(month_end_unpaid_balance)  # unpaid balance for month of idx
    
    next_month_balance = round(ub[idx] + ub[idx] * iR/12, 2)
    b.append(next_month_balance)
print(b[-1], sum(p))
p.insert(0, 0)
ub.insert(0, 0)
from pprint import pprint
pprint(b)

pprint(p)
