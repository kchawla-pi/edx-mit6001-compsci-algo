iter_count = 0
n_dict = {}
series_n_count = []
series_glob = []


def fib_ineff(n):

    global iter_count
    iter_count += 1
    if n in (1, 2):
        return n
    return fib(n - 1) + fib(n - 2)


def fib_ser_att0(n):
    global series_glob
    global n_dict
    global iter_count
    iter_count += 1
    if n in n_dict:
        series_glob.append(n_dict[n])
        return series_glob[-1]
    if n in (1, 2):
        series_glob.append(n)
        return series_glob[-1]
    series_glob.append(fib(n - 1) + fib(n - 2))
    return series_glob[-1]


def fib(n, d):
    
    global n_dict
    global iter_count
    iter_count += 1
    if n in n_dict:
        return n_dict[n]
    elif n in (1, 2):
        return n
    else:
        n_dict[n] = fib(n - 1, d) + fib(n - 2, d)
        return n_dict[n]


def fib_tut(n):
    
    if n in (1, 2):
        return n
    else:
        return fib_tut(n - 1) + fib_tut(n - 2)
    
    
def fib_series(n):
    
    global series_n_count
    series = []
    if n in series_n_count:
        series.append(n)
    else:
        series.append(fib(n))
    return series

"""
0, 1, 1, 2, 3, 5, 8
"""
import time
n = 39
start = time.time()
print(fib_tut(n))
stop = time.time()
print(stop - start)
# print(fib_ineff(n))
# print(fib(n, n_dict))
start = time.time()
print(fib(n, n_dict))
stop = time.time()
print(stop - start)
# print(n_dict)
# print(fib_series(n))

