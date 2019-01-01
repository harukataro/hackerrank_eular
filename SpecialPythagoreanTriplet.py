#!/bin/python3

import sys


def numPythagoreanTriplet(x1, x2, x3):
        triple_list = [x1, x2, x3]
        triple_list.sort()
        a = triple_list[0]
        b = triple_list[1]
        c = triple_list[2]
        if c**2 == a**2 + b**2:
            return a * b * c
        else:
            return -1


def tripleNumcombinationGenerator(n):
        max_num = -1
        if n < 12:
            return -1
        else:
            for i in range(n-2, 4, -1):
                c = i
                for j in range(n-c-1, 1, -1):
                    b = j
                    a = n - b - c
                    print(a, b, c)
                    abc = numPythagoreanTriplet(a, b, c)
                    if abc > max_num:
                        max_num = abc
        return max_num


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(tripleNumcombinationGenerator(n))
