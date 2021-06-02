#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zeros=negetives=positives = 0
    for element in arr:
        if element == 0: zeros+= 1
        elif element> 0: positives += 1
        else: negetives += 1
    n = float(len(arr))
    zeros = round(float(zeros)/n,4)
    positives = round(float(positives)/n, 4)
    negetives = round(float(negetives)/n, 4)
    return positives,negetives, zeros

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))

