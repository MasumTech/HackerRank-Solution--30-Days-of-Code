#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    if N%int(2)!=0:
       print('Weird')

    elif N%int(2)==0:
        if N>=int(2) and N<=int(5):
            print('Not Weird')
        elif N>=int(6) and N<=int(20):
            print('Weird')
        elif N>int(20):
            print('Not Weird')



