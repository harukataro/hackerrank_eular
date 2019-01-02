#!/bin/python3

import sys
import math


def generatePythagoreanTriplet(maxnum):
    pythagoren3 = [-1] * (maxnum+1)
    for m in range(2, int(math.sqrt(maxnum/4))):
        for n in range(1, m):
            if n >= m:
                break
            if (m - n) % 2 != 0:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                pythagoren3[a+b+c] = a * b * c
    return pythagoren3


pythagorean = generatePythagoreanTriplet(3000)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pythagorean[n])
