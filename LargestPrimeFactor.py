#!/bin/python3

import sys
import math

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maxfactor =0
    i =2
    while i < int(math.sqrt(n))+1:
        if n%i  == 0:
            maxfactor = i
            n=n/i
        else:
            i=i+1
print(n)
print(maxfactor)
ans = int (max (n,maxfactor))
print(ans)


            
