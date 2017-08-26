# --encoding: utf-8--


def credit_balance(balance, annualInterestRate=0.2, monthlyPaymentAmount=10, monthlyPaymentRate=0, months=12):
    initial_balance = balance
    for idx in range(0, months):
        month_end_payment = monthlyPaymentAmount if monthlyPaymentRate == 0 else round(balance * monthlyPaymentRate, 2)

        month_end_unpaid_balance = round(balance - month_end_payment, 2)
        next_month_balance = round(month_end_unpaid_balance + month_end_unpaid_balance * annualInterestRate/ months, 2)
        balance = next_month_balance
    return balance
    

def monthly_payment_calc(balance, annualInterestRate=0.2, monthlyPaymentAmount=10, monthlyPaymentRate=0, months=12):
    while credit_balance(balance=balance, annualInterestRate=annualInterestRate, monthlyPaymentAmount=monthlyPaymentAmount, monthlyPaymentRate=monthlyPaymentRate, months=months) > 0:
        monthlyPaymentAmount += 10
    return monthlyPaymentAmount
        

def tests():
    credit_balance_tests = ({'params': (42, 0.2, 0, 0.04, 12), 'expected': 31.38},
                            {'params': (484, 0.2, 0, 0.04, 12), 'expected': 361.61}
                            )
    
    monthly_payment_calc_test = ({'params': (3329, 0.2, 10, 0, 12), 'expected': 310},
                                 {'params': (4773, 0.2, 10, 0, 12), 'expected': 440},
                                 {'params': (3926, 0.2, 10, 0, 12), 'expected': 360}
                                 )
    
    result_table = {True: 'Passed', False: 'Change'}
    for test_ in credit_balance_tests:
        print(result_table[credit_balance(*test_['params']) == test_['expected']])
    
    for test_ in monthly_payment_calc_test:
        # print(monthly_payment_calc(*test_['params']), test_['expected'])
        print(result_table[monthly_payment_calc(*test_['params']) == test_['expected']])

tests()

balance = 3926
annualInterestRate = 0.2
print("Lowest Payment:", monthly_payment_calc(balance=balance, annualInterestRate=annualInterestRate))
