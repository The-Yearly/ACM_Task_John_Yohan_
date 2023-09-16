#!/bin/python3


t = int(input())
if t>10**5:
    t=10**5
for a0 in range(t):
    n = int(input())
    c=0
    for g in range(n):
        if g%3==0 or g%5==0:
            c+=g
    print(c)        
