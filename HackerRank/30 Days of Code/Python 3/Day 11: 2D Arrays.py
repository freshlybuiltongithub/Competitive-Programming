"""
Hackerrank Solution for Day 11: 2D Arrays
"""
import math
import os
import random
import re
import sys

def hourglasssum(arr):
    maxsum = -99
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            hourglass = top + mid +bot
            maxsum = max(hourglass,maxsum)
    return maxsum

if __name__ == '__main__':
    
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglasssum(arr))

