#!/bin/python3

import sys

def gcd(x,y):
    m = max(x,y)
    n = min(x,y)
    if m%n == 0:
        return n
    else:
        return(gcd(n,m%n))

def lcm(x,y):
    return (x * y)//gcd(x,y)

def multilcm():
    mlcm = [1] * 41
    for i in range(2,41):
        mlcm[i]=lcm(mlcm[i-1],i)
    return mlcm

t = int(input().strip())
mlcm = multilcm()
for a0 in range(t):
    n = int(input().strip())
    print(mlcm[n])