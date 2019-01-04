#!/bin/python3

import sys

def prime_eratosthenes():
    prime = [0] * 1000
    data = [i + 1 for i in range(1, 100000)]
    s = 0
    while True:
        p = data[0]
        if 100000 <= p*p:
            del prime[s+1:len(prime)]
            return prime + data
        prime[s] = p
        s = s + 1
        data = [e for e in data if e % p != 0]


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
