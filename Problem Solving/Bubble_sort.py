#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
l = len(a)
NumberOfSwaps = 0

for i in range(l):
    sorter = 0
    for j in range(l-1):    
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            sorter +=1
            NumberOfSwaps +=1
    if sorter == 0:
        break
    
print("Array is sorted in {} swaps.".format(NumberOfSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[l-1]))

    
    
