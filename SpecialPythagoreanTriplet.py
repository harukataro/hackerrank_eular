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
            for i in range(int(n/3)+1, int(n/2)):
                c = i
                for j in range(int((n-c)/2)+1, n-c):
                    b = j
                    a = n - b - c
                    if a > b:
                        break
                    else:
                        if ((a % 4) * (b % 4) * (a % 3) * (b % 3) == 0) and ((a % 5) * (b % 5) * (c % 5) == 0):
                            abc = numPythagoreanTriplet(a, b, c)
                            print(c, b, a, abc)
                            if abc > max_num:
                                return abc
        return -1


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#    print(tripleNumcombinationGenerator(n))
print(tripleNumcombinationGenerator(736))
