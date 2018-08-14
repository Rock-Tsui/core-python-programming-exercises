#!/usr/bin/env python

def fib(n):
    if n ==0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def get_nfibo(n):
    print(fib(n-1))

get_nfibo(6)