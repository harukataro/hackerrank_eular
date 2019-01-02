#!/bin/python3

import sys
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_array():
    primeArr = []
    primeArr.append(2)
    i = 1
    while i <= 100000:
        i += 2
        if is_prime(i):
            primeArr.append(i)
    return primeArr

def prime_sum(n, primeArr):
    prime_sum_num = 0
    for i in range(0, len(primeArr)):
        if primeArr[i] > n:
            break
        else:
            prime_sum_num += primeArr[i]
    return prime_sum_num


primeArr = prime_array()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_sum(n, primeArr))
