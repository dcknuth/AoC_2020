'''AoC Day 9 Part1: find the first number in the list which is not the sum
of two of the 25 numbers before it.
Since we are checking the sum of two numbers, maybe we can optimize by just
looking for the number we need. Also used the walrus operator to save an
extra minus operation'''
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
        for j, y in enumerate(l[i:i+pv]):
            if (d := x - y > 0) and d in l[i+j+1:i+pv]:
                found = True
                break
        if not found:
            print(f"{x} is the first number without a sum")
            return(x)

inval = FindInvalid(l, PREAMBLE, PREVIOUS)
# original was 0.0019, optimized is 0.0006

'''Part2: find a contiguous set of at least two numbers in your
list which sum to the invalid number from step 1. add together the smallest
and largest number in this contiguous range
To optimize, let's try to save the sum as we go'''

@timef.timef
def FindEW(l, inval):
    i = 0
    while i < len(l):
        j = i
        total = 0
        while j < len(l):
            total += l[j]
            if total == inval:
                ew = min(l[i:j+1]) + max(l[i:j+1])
                print("Encryption weakness is", ew)
                return(ew)
            elif total > inval:
                break
            j += 1
        i += 1

ew = FindEW(l, inval)
# original was 0.2046 and optimized is 0.0075
