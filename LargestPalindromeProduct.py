#!/bin/python3

import sys

def is_palindrome6dig(n):
    maxpal = 101101
    for i in range(999,101, -1):
        for j in range(999,101, -1):
            x = i * j
            if x <= maxpal:
                break
            elif x < n:
                xstr = str(x)
                if xstr[5] == xstr[0] and xstr[4] == xstr[1] and xstr[3] == xstr[2]:
                    maxpal = x
    return maxpal

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(is_palindrome6dig(n))
    

