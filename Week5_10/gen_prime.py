def genPrimes():
    """
    Returns a generator which yields the next prime number when called using the next() method.
    :return: prime number (starting from 2)
    :rtype: int
    """
    '''
    yield 2 as the first prime number defacto.
    Start an infinite while loop so the generator never stops.
    Take an initial number(num) == 3.
    
    Generate all the numbers from 3 to num as divisors, int divide num by them.
    (use a generator which divides num by next divisor, returns True if remainder is 0)
    (use a comprehension
        if remainder is not 0, continue divisor testing.
        if remainder is 0, an divisor != num, then num is not prime.
            Abandon int division.
        if remainder is 0 and divisor == int, number is prime.
            Yield num.
        
    Increment num by 2 to generate next odd number.
    '''
    def stop_iter():
        raise StopIteration
    yield 2
    num = 1
    divisors = 0
    while True:
        stop = int(((num + 1) / 2))
        num += 2
        divisors = (divisor for divisor in range(3, stop, 2) if num % divisor == 0)  # generating first factor of num
        check = [(divisor_, num, divisors.close()) for divisor_ in divisors if divisor_ != num]  # if first factor of num is not num itself
        if not check:
            yield num
            
    
prime = genPrimes()
for num in prime:
    check = (div for div in range(1, num + 1) if num % div == 0)
    print([factor for factor in check])
    

