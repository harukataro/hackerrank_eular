#!/bin/python3

import sys

def prime_eratosthenes():
    prime = [i for i in range(0, 100001)]
    prime_sum = [0] *100001
    prime[1] = 0
    for i in range(2, 100002):
        if prime[i] != 0:
            while :
            prime[i*j] = 0






def make_prime_sum_list():
    prime_data = prime_eratosthenes()
    prime_sum = [0] * 100001
    prime_sum[2] = 2
    j = 1
    plen = len(prime_data)
    for i in range(3, 100001):
        if prime_data[j] == i:
            prime_sum[i] = prime_sum[i-1] + prime_data[j]
        else:
            prime_sum[i] = prime_sum[i - 1]
    return prime_sum


prime_sum_list = make_prime_sum_list()
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(prime_sum_read(n, prime_sum_list))
print(prime_sum_list[10])
