#!/usr/bin/evn python
from time import clock
from functools import reduce

def timeit(func, *nkwargs, **kwargs):
    try:
        start = clock()
        retval = func(*nkwargs, **kwargs)
        result = (True, retval, clock() - start)
    except Exception as diag:
        result = (False, str(diag))
    return result

def mult(x, y):
    return x * y

def reducefact(n):
    if n == 0 or n == 1:
        return 1
    return reduce(mult, range(1, n+1))

def iterfact(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    for i in range(1, n+1):
        fact *= i
    return fact

def recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive(n - 1)

def test():
    funcs = [iterfact, reducefact, recursive]
    eachVal = 100

    for eachFunc in funcs:
        ret = timeit(eachFunc, eachVal)
        if ret[0]:
            print('%s result: %s, and spend time: %s' % (eachFunc.__name__, ret[1], ret[2]))
        else:
            print('%s execute failed: %s' % ret[1])

test()