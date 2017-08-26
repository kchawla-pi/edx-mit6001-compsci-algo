# --encoding: utf-8--

current_recursion_depth = -1
max_recursion_depth = current_recursion_depth

def credit_balance(balance, annualInterestRate=0.2, monthlyPayment=10, months=12):
    b = [balance]
    iR = annualInterestRate
    p = []
    ub = []
    for idx in range(0, months):
        p.append(monthlyPayment)  # minimum payment for month of idx
        
        month_end_unpaid_balance = round(b[idx] - p[idx], 2)
        ub.append(month_end_unpaid_balance)  # unpaid balance for month of idx
        
        next_month_balance = round(ub[idx] + ub[idx] * iR / months, 2)
        b.append(next_month_balance)
    # p.insert(0, 0)  # inserting zero payment for the initial (zeroth) month.
    # ub.insert(0, 0)  # inserting zero unpaid balance for the initial (zeroth) month.
    return b[-1]


def zero_debt_payment_calc(balance, annualInterestRate=0.2, monthlyPayment=10):
    global current_recursion_depth
    global max_recursion_depth
    current_recursion_depth += 1
    balance_paid = credit_balance(balance=balance, annualInterestRate=annualInterestRate,
                                   monthlyPayment=monthlyPayment) <= 0
    if balance_paid:
        return monthlyPayment
        # balance_paid = True
    else:
        monthlyPayment += 10
        monthlyPayment = zero_debt_payment_calc(balance=balance, annualInterestRate=annualInterestRate,
                                                monthlyPayment=monthlyPayment)
        balance_paid = True
        max_recursion_depth = current_recursion_depth
        current_recursion_depth -= 1
        
# def zero_debt_pay_amount(balance, monthlyPaymentRate):
#     balance
def zero_debt_payment2(balance, annualInterestRate=0.2, monthlyPayment=10):
    global current_recursion_depth
    global max_recursion_depth
    current_recursion_depth += 1
    if credit_balance(balance=balance, annualInterestRate=annualInterestRate,
                                   monthlyPayment=monthlyPayment) <= 0:
        return monthlyPayment
    else:
        zero_debt_payment2(balance=balance, annualInterestRate=annualInterestRate,
                       monthlyPayment=monthlyPayment+10)
    
    
    
months=12
balance = 3329
print(zero_debt_payment_calc2(balance))
    







"""
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
"""
