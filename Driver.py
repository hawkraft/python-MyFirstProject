#!/usr/bin/python3

from MergeSort import mergesort
arr = [199, 173, 172, 123, 184, 156, 167, 169, 197, 121, 143, 157, 195, 135, 151, 146, 176, 180, 182]
n = len(arr)

print("Input Array:")
for x in arr:
    print(x, end=' ')

mergesort(arr, 0, n - 1)

print("\n\nSorted array:")
for x in arr:
    print(x, end=' ')