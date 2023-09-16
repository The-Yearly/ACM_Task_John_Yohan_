#!/bin/python3

import sys


t = int(input())
for a0 in range(t):
    n = int(input())
    c=0
    c2=1
    s=0
    while c2<=n:
        if c2%2==0:
            s+=c2
        c2,c=c+c2,c2
    print(s)
