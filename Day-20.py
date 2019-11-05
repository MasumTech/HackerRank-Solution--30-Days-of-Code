#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaping = int(0)
f = int(0)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swaping+=1
    if swaping==0:
        f=1
        print('Array is sorted in 0 swaps.')
        print('First Element: '+ str(a[0]))
        print('Last Element: '+ str(a[n-1]))
        break
if f==0:
    print('Array is sorted in {0} swaps.'.format(swaping))
    print('First Element: '+ str(a[0]))
    print('Last Element: '+ str(a[n-1]))

