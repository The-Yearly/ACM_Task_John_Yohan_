#!/bin/python3

import sys


t = int(input())
for a0 in range(t):
    n = int(input())
    hi=0
    for g in range(100,1000):
        for h in range(100,1000):
            if hi<g*h<n:
                l=list(str(g*h))
                l2=l[:]
                l.reverse()
                if l==l2:
                    hi=g*h
    print(hi)                    
        
