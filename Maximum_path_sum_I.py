#!/bin/python3

import sys


def max_sum(x, y, data, max_n):
    if x == 0:
        ans = int(data[0][0])
    elif x == 1:
        ans = int(data[0][0]) + int(data[x][y])
    else:
        if y == 0:
            ans = max_n[x - 1][0] + int(data[x][y])
        elif x == y:
            ans = max_n[x - 1][x - 1] + int(data[x][y])
        else:
            ans = max(max_n[x-1][y-1], max_n[x-1][y]) + int(data[x][y])
    return ans


def max_num(data, nx):
    max_n = [[0 for i in range(nx+1)] for j in range(nx+1)]
    for i in range(0, nx):
        for s in range(0, i+1):
            max_n[i][s] = max_sum(i, s, data, max_n)
    return max(max_n[nx-1])


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    row = [[0 for i in range(n)] for j in range(n)]
    for a1 in range(n):
        row[a1] = input().split()
    print(max_num(row, n))

# print(max_num(row, n))



