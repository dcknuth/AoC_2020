'''AoC Day 9 Part1: find the first number in the list which is not the sum
of two of the 25 numbers before it'''
from itertools import combinations
import sys
sys.path.append("..")
import timef

#filename = "test09.txt"
filename = "input09.txt"
#PREAMBLE = 5
#PREVIOUS = 5
PREAMBLE = 25
PREVIOUS = 25

with open(filename) as f:
    ls = f.read().strip().split('\n')

# Get into a list of integers
l = [int(x) for x in ls]

@timef.timef
def FindInvalid(l, pa, pv):
    for i, x in enumerate(l[pa:]):
        found = False
        for y1, y2 in combinations(l[i:i+pv], 2):
            if y1 + y2 == x:
                found = True
                break
        if not found:
            print(f"{x} is the first number without a sum")
            return(x)

inval = FindInvalid(l, PREAMBLE, PREVIOUS)


'''Part2: find a contiguous set of at least two numbers in your
list which sum to the invalid number from step 1. add together the smallest
and largest number in this contiguous range'''

@timef.timef
def FindEW(l, inval):
    i = 0
    while i < len(l):
        j = 1
        while i + (j-1) < len(l):
            if sum(l[i:j]) == inval:
                ew = min(l[i:j]) + max(l[i:j])
                print("Encryption weakness is", ew)
                return(ew)
            elif sum(l[i:j]) > inval:
                break
            j += 1
        i += 1

ew = FindEW(l, inval)
