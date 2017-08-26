# --encoding: utf-8--


def credit_balance(balance, annualInterestRate=0.2, monthlyPaymentAmount=0, monthlyPaymentRate=0.04,
            months=12):
    for idx in range(0, months):
        month_end_payment = monthlyPaymentAmount if monthlyPaymentRate == 0 else round(
            balance * monthlyPaymentRate, 2)
        
        month_end_unpaid_balance = round(balance - month_end_payment, 2)
        next_month_balance = round(
            month_end_unpaid_balance + month_end_unpaid_balance * annualInterestRate / months, 2)
        balance = next_month_balance
    return balance


def monthly_payment_calc(balance, annualInterestRate=0.2, months=12):
    monthlyPaymentAmount = 0
    monthlyPaymentRate = 0
    while credit_balance(balance, annualInterestRate, monthlyPaymentAmount, monthlyPaymentRate,
                         months) > 0:
        monthlyPaymentAmount += 10
    return monthlyPaymentAmount


def monthly_payment_search(balance, annualInterestRate=0.2, months=12):
    eps = 0.05
    monthlyPaymentRate = 0  # not relevant here, edge condition
    monthlyPaymentAmount = 0  # not relevant here, edge condition
    
    monthly_payment_min_possible = balance / months  # when interest rate is zero.
    monthly_payment_max_possible = credit_balance(balance, annualInterestRate, monthlyPaymentAmount,
                                           monthlyPaymentRate, months) / months  # when pay/month is 0
    
    lower = monthly_payment_min_possible  # initial lower bound for monthly payments
    upper = monthly_payment_max_possible  # initial upper bound for monthly payments
    new_balance = 1 # initializing to 1 for while loop
    while new_balance:
        monthlyPaymentAmount = (lower + upper) / 2
        new_balance = credit_balance(balance, annualInterestRate, monthlyPaymentAmount, monthlyPaymentRate,
                                             months)
        if new_balance < -eps:
            upper = monthlyPaymentAmount
            lower = lower
        elif new_balance > 0:
            upper = upper
            lower = monthlyPaymentAmount
        else:
            return round(monthlyPaymentAmount, 2)
    
    
def tests():
    credit_balance_tests = ({'args': (42, 0.2, 0, 0.04, 12), 'expected': 31.38},
                            {'args': (484, 0.2, 0, 0.04, 12), 'expected': 361.61}
                            )
    
    monthly_payment_calc_tests = ({'args': (3329, 0.2, 12), 'expected': 310},
                                 {'args': (4773, 0.2, 12), 'expected': 440},
                                 {'args': (3926, 0.2, 12), 'expected': 360}
                                 )
    
    monthly_payment_search_tests = ({'args': (320000, 0.2, 12), 'expected': 29157.09},
                                    {'args': (999999, 0.18, 12), 'expected': 90325.03},
                                    {'args': (386577, 0.21, 12), 'expected': 35376.55},
                                    {'args': (207184, 0.2, 12), 'expected': 18877.76},
                                    {'args': (71228, 0.21, 12), 'expected': 6518.24},
                                    {'args': (57672, 0.15, 12), 'expected': 5141.11},
                                    {'args': (310107, 0.22, 12), 'expected': 28501.74},
                                    {'args': (438941, 0.22, 12), 'expected': 40342.79},
                                    {'args': (404579, 0.2, 12), 'expected': 36863.58},
                                    {'args': (409965, 0.21, 12), 'expected': 37516.84},
                                    {'args': (77214, 0.21, 12), 'expected': 7066.03},
                                    {'args': (460027, 0.22, 12), 'expected': 42280.79}
                                    )
    result_table = {True: 'Passed', False: 'Change'}
    
    print("\nTesting credit_balance():")
    for test_ in credit_balance_tests:
        ans = credit_balance(*test_['args'])
        print(result_table[abs(ans - test_['expected']) < 0.05], ans, test_['expected'])
        
    print("\nTesting monthly_payment_calc():")
    for test_ in monthly_payment_calc_tests:
        ans = monthly_payment_calc(*test_['args'])
        print(result_table[abs(ans - test_['expected']) < 0.05], ans, test_['expected'])

    print("\nTesting monthly_payment_search():")
    for test_ in monthly_payment_search_tests:
        ans = monthly_payment_search(*test_['args'])
        print(result_table[abs(ans - test_['expected']) < 0.05], ans, test_['expected'])


def time_it():
    import time
    start = time.time()
    print()
    print(monthly_payment_calc(1534567847.93))
    stop = time.time()
    print('Time taken:', stop - start)
    quit()
    start = time.time()
    print(monthly_payment_search(15345678475.93))
    stop = time.time()
    print('Time taken:', stop - start)


tests()
time_it()
# balance = 320000
# annualInterestRate = 0.2
# print("Lowest Payment:", monthly_payment_search(balance=balance, annualInterestRate=annualInterestRate))
# balance = 999999
# annualInterestRate = 0.18
# print("Lowest Payment:", monthly_payment_search(balance=balance, annualInterestRate=annualInterestRate))





