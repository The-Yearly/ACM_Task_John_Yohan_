#!/bin/python3
import sys
T = int(input())
for g in range(T):
    N = int(input())
    mp = -1
    while N % 2 == 0:
        mp = 2
        N //= 2
    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            mp = i
            N //= i
    if N > 1:
        mp = N
    print(mp)

