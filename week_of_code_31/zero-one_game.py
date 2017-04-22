#!/usr/bin/python

q = int(raw_input())
for _ in range(q):
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    out = 0
    i = 1
    while(True):
        # print arr[i-1], arr[i+1]
        print i
        if (arr[i-1] == 0) and (arr[i+1] == 0):
            # print 'maamla', arr[:i]+arr[i+1:]
            arr = arr[:i] + arr[i+1:]
            n -= 1
            out += 1
            # print arr
            # break
        if i+2 == n:
            break
        i += 1
    if out%2 == 0:
        print 'Bob'
    else:
        print 'Alice'
