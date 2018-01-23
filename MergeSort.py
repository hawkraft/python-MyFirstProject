#!/usr/bin/python3
import math


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    temp1 = [0] * (n1 + 1)
    temp2 = [0] * (n2 + 1)

    for i in range(0, n1):
        temp1[i] = arr[p + i]

    for j in range(0, n2):
        temp2[j] = arr[q + j + 1]

    temp1[n1] = math.inf
    temp2[n2] = math.inf

    i = 0
    j = 0
    for k in range(p, r+1):
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i = i + 1
        else:
            arr[k] = temp2[j]
            j = j + 1


def mergesort(arr, l, n):
    if l < n:
        m = int((l + (n-l)/2))
        mergesort(arr, l, m)
        mergesort(arr, m + 1, n)
        merge(arr, l, m, n)