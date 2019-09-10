#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(float(meal_cost) * (int(tip_percent) / int(100)))

    tax = float(float(meal_cost) * (int(tax_percent) / int(100)))

    total = float(meal_cost + tip + tax)

    return total


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total = solve(meal_cost, tip_percent, tax_percent)

    print(round(total))
