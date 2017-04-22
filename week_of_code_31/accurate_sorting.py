#!/usr/bin/python

q = int(raw_input())
for _ in range(q):
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    for i in range(n-1):
        if arr[i] - arr[i+1] == 1:
            arr[i] = arr[i] + arr[i+1]
            arr[i+1] = arr[i] - arr[i+1]
            arr[i] = arr[i] - arr[i+1]
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            print 'No'
            break
        elif i+2 == n:
            print 'Yes'
