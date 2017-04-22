#!/usr/bin/python

n = int(raw_input())
arr = map(int, raw_input().strip().split())
warr = map(int, raw_input().strip().split())
numerator = 0
for i in range(n):
    numerator += arr[i]*warr[i]
denominator = sum(warr)
print round(float(numerator)/denominator, 1)
