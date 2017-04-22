#!/usr/bin/python

n = int(raw_input())
arr = [int(x) for x in raw_input().split()]
mean = float(sum(arr))/n
arr = sorted(arr)
if n%2 == 0:
    median = (float(arr[n/2-1]+arr[n/2]))/2
else:
    median = arr[n/2]
dic = {}
for i in range(n):
    dic[arr[i]] = 0
# print dic
for i in range(n):
    dic[arr[i]] += 1
mode = -1
maxt = 0
for i in dic.keys():
    if maxt < dic[i]:
        maxt = dic[i]
        mode = i
    elif maxt == dic[i] and mode > i:
        mode = i
print mean
print median
print mode
