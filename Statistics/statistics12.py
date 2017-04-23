#!/usr/bin/python

n = int(raw_input())
inp = [int(x) for x in raw_input().split()]

mean = float(sum(inp))/n
inp = [(x - mean)**2 for x in inp]
variance = float(sum(inp))/n
std_dev = (float(variance))**(.5)

print round(std_dev, 1)
