#!/bin/python3

import sys
import math


def generate_pythagorean_triplet(max_num):
    pytha_triple = [-1] * (max_num+1)
    for m in range(2, int(max_num/2)):
        for n in range(1, m):
            if n >= m:
                break
            if (m - n) % 2 != 0:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                sum_abc = a + b + c
                multi_abc = a * b * c
                if sum_abc <= max_num+1:
                    pytha_triple[sum_abc] = max(multi_abc, pytha_triple[sum_abc])
                    for i in range(2, int(max_num/sum_abc)+1):
                        if sum_abc * i <= max_num+1:
                            pytha_triple[sum_abc * i] = max(i**3 * pytha_triple[sum_abc], pytha_triple[sum_abc * i])
    return pytha_triple


pythagorean = generate_pythagorean_triplet(3000)


t = int(input().strip())
for a0 in range(t):
    x = int(input().strip())
    print(pythagorean[x])
