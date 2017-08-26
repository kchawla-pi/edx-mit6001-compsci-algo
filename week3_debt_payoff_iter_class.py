# --encoding: utf-8--


class CreditCardPayment:
    """
    Class to calculate balance, interest, monthly payments.
    """
    def __init__(self, balance, annualInterestRate=0.2, monthlyPaymentAmount=10, monthlyPaymentRate=0.04, months=12):
        self.init_balance = balance
        self.balance = balance
        self.annualInterestRate = annualInterestRate
        self.monthlyPaymentAmount = monthlyPaymentAmount
        self.monthlyPaymentRate = monthlyPaymentRate
        self.months = months
        
    def credit_balance(self, purpose: ('calc', 'pay')='calc'):
        for idx in range(0, self.months):
            month_end_payment = (self.monthlyPaymentAmount if (self.monthlyPaymentRate == 0 or purpose == 'pay')
                                 else round(self.balance * self.monthlyPaymentRate, 2)
                                 )
            month_end_unpaid_balance = round(self.balance - month_end_payment, 2)
            next_month_balance = round(month_end_unpaid_balance +
                                       month_end_unpaid_balance * self.annualInterestRate / self.months, 2)
            self.balance = next_month_balance

    def monthly_payment_calc(self):
        while self.credit_balance() > 0:
            self.monthlyPaymentAmount += 10

    def monthly_payment_search(self):
        lower_bound = self.balance / self.months
        upper_bound = self.credit_balance(balance)


balance = 320000
annualInterestRate = 0.2
months = 12
# def monthly_payment_search(balance, annualInterestRate=0.2, months=12):



def tests():
    cc_pay = CreditCardPayment
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


# tests()

