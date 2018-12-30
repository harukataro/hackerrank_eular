#!/bin/python3

import sys

def SumSquareDiff(n):
    Square_Sum = (1/6)*n*(n+1)*(2*n+1)
    SumSquare = ((1/2)*n*(n+1))**2
    return int(SumSquare - Square_Sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(SumSquareDiff(n))
