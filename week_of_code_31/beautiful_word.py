#!/usr/bin/python

vowels = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True, 'y':True}
inp = raw_input()

for i in range(len(inp)-1):
    if inp[i] in vowels:
        if inp[i+1] in vowels:
            print 'No'
            break
        if i+2 == len(inp):
            print 'Yes'
        else:
            continue
    elif inp[i] == inp[i+1]:
        print 'No'
        break
    elif i+2 == len(inp):
        print 'Yes'
    else:
        continue
