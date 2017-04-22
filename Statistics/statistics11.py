#!/usr/bin/python

def findMedian(a):
    length = len(a)
    if length%2==0:
        length /= 2
        return (float(a[length-1]+a[length]))/2
    else:
        return float(a[length/2])
n = int(raw_input())
quartile_list = [int(x) for x in raw_input().split()]
frequency_list = [int(x) for x in raw_input().split()]
frequency_map = {}
for i in range(n):
    if quartile_list[i] in frequency_map:
        frequency_map[quartile_list[i]] += frequency_list[i]
    else:
        frequency_map[quartile_list[i]] = frequency_list[i]
quartile_list = sorted(frequency_map.keys())
# print quartile_list
# print frequency_map
quartile_list = [x for x in quartile_list for _ in range(frequency_map[x])]
q2 = findMedian(quartile_list)
# print quartile_list
n = sum(frequency_list)
# print n
if n%2 == 0:
    q1 = findMedian(quartile_list[:(n/2)])
    q3 = findMedian(quartile_list[(n/2):])
else:
    q1 = findMedian(quartile_list[:(n/2)])
    q3 = findMedian(quartile_list[(n/2)+1:])
# print q1,q2,q3
print round(float(q3-q1), 1)
