#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr); m = len(arr[0])-1
    diagonal1 = 0
    diagonal2 = 0
    for index in range(n):
        diagonal1 += arr[index][index]
        diagonal2 += arr[index][m-index]
    return abs(diagonal1-diagonal2)
        
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()