#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
dec_num = int(n)
cnv_bin = ''
while dec_num//2 > 0:
    if dec_num%2 == 0:
        cnv_bin += '0'
    else:
        cnv_bin += '1'

    dec_num = dec_num//2

cnv_bin += str(dec_num)
b = cnv_bin[::-1]
c = int(0)
mx = int(0)
for i in range(len(b)):
    if b[i]=='1':
        c+=1
    else:
          c = 0
    if c > mx:
        mx = c
    #print('c='+ str(c))
    #print('b=' + b[i])
print(mx)