# --encoding: utf-8--


def credit_balance(balance, annualInterestRate=0.2, monthlyPaymentRate=0.04, months=12):
    b = [balance]
    iR = annualInterestRate
    mPR = monthlyPaymentRate
    p = []
    ub = []
    for idx in range(0, months):
        month_end_payment = round(b[idx] * mPR, 2)
        p.append(month_end_payment)  # minimum payment for month of idx
        
        month_end_unpaid_balance = round(b[idx] - p[idx], 2)
        ub.append(month_end_unpaid_balance)  # unpaid balance for month of idx
        
        next_month_balance = round(ub[idx] + ub[idx] * iR/months, 2)
        b.append(next_month_balance)
    p.insert(0, 0)  # inserting zero payment for the initial (zeroth) month.
    ub.insert(0, 0)  # inserting zero unpaid balance for the initial (zeroth) month.
    return b[-1]

print("Remaining balance:", credit_balance(balance=484))
print("Remaining balance:", credit_balance(balance=42))
