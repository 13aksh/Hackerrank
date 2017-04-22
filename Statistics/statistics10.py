#!/usr/bin/python

def findMedian(a):
    length = len(a)
    if length%2==0:
        length /= 2
        return (a[length-1]+a[length])/2
    else:
        return a[length/2]
n = int(raw_input())
quartile_list = [int(x) for x in raw_input().split()]
quartile_list = sorted(quartile_list)
q2 = findMedian(quartile_list)
if n%2 == 0:
    q1 = findMedian(quartile_list[:(n/2)])
    q3 = findMedian(quartile_list[(n/2):])
else:
    q1 = findMedian(quartile_list[:(n/2)])
    q3 = findMedian(quartile_list[(n/2)+1:])
print q1,"\n",q2,"\n",q3
