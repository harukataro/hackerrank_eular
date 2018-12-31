#!/bin/python3

import sys
import math

def is_prime(n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

def primeArray():
    primeArr =[0] * 10001
    primeArr[1]=2
    primeNum = 2
    i = 1
    while primeNum < 10001:
        i += 2
        if is_prime(i):
            primeArr[primeNum] = i
            primeNum = primeNum + 1
    return primeArr

primeArr = primeArray()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeArr[n])

