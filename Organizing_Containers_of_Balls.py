#Organizing_Containers_of_Balls

#!/usr/bin/python

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    M = []
    for M_i in xrange(n):
        M_temp = map(int,raw_input().strip().split(' '))
        M.append(M_temp)
    