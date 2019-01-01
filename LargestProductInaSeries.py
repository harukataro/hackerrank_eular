#!/bin/python3

import sys


def numgen(num,n,k):
    mMax =0
    numStr =str(num)
    if n==k:
        for i in range(0,n):
            multiple *= int(numStr[i])
        return multiple
    for i in range(0,n-k):
        multiple =1
        for j in range(i,i+k):
            if numStr[j] == 0:
                multiple =0
                break
            else:
                multiple *= int(numStr[j])
        if multiple > mMax:
            mMax =multiple
            print(i, mMax)
    return mMax

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(numgen(num,n,k))
# print(numgen(2709360626,10,5))