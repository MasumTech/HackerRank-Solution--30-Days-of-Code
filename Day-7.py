#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    lth = len(arr)
for i in range(0,lth):
    print(arr[lth-i-1], end=' ')
