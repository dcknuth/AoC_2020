'''AoC Day10 Part1: If you use every adapter in your bag at once, find
the distribution of joltage differences between the charging outlet, the
adapters, and your device. What is the nuber of 1-jolt differences
multiplied by the number of 3-jolt differences?'''
import sys
sys.path.append("..")
import timef
from collections import Counter

#filename = "test10.txt"
filename = "input10.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

@timef.timef
def part1(ls):
    # get a list of integers
    l = [int(x) for x in ls]
    # sort them
    l.sort()
    # make a counter and count all the differences
    counts = Counter()
    last = 0
    for j in l:
        counts[j-last] += 1
        last = j
    # and one more 3 for the last jump to the device
    counts[3] += 1
    print("1Js * 3Js is", counts[1] * counts[3])

part1(ls)
# Ran in 0.00037 seconds

'''Part2: What is the total number of distinct ways you can arrange the
adapters to connect the charging outlet to your device?'''
@timef.timef
def part2(ls):
    # start the same with integers and a sort
    l = [int(x) for x in ls]
    # sort them
    l.sort()
    '''
    Now... how do the number of counts of these affect the possibilities?
    maybe we start at one and walk the list and multiply by two if there are
    two ways to go in a group of three and by three if there are three ways
    to go?
    No, this is a good bit harder than that. Note a first thing, there are
    only differences of 1 or three while we walk the list. This means that
    we only need to consider the runs with differences of 1. From the two
    examples with answers we can say that a run of two, like 0, 3,4, 7,
    does not do anything as you need both numbers. A run of three, you
    can include the middle number or not, so 2 possibilities. A run of four
    has four possibilities and a run of 5 has 7. I can't see the pattern yet
    so let's look at what the longest run is and see if we could make a
    program to output all possibilties and count the number of valid ones.
    We could do that up to a run of at least 16 and maybe up to 30
    '''
    counts = Counter()
    last = 0
    for j in l:
        counts[j-last] += 1
        last = j
    # and one more 3 for the last jump to the device
    counts[3] += 1
    print(f"1Js {counts[1]} 2Js {counts[2]}")
    # see what the max run is
    max_run = 0
    this_run = 1
    i = 1
    while i < len(l):
        if l[i] - l[i-1] == 1:
            this_run += 1
            if this_run > max_run:
                max_run = this_run
        else:
            this_run = 1
        i += 1
    print("The longest run is", max_run)
    # like a gift from heaven, the longest run is only 5, so we can make a
    #  lookup table and just keep multiplying by 2, 4 or 7
    p = {3:2, 4:4, 5:7}
    combos = 1
    this_run = 1
    i = 1
    # add 0 to our list to handle a run at the beggining of our list
    l.insert(0, 0)
    while i < len(l):
        if l[i] - l[i-1] == 1:
            this_run += 1
        else:
            if this_run > 2:
                combos *= p[this_run]
            this_run = 1
        i += 1
    if this_run > 2:
        combos *= p[this_run]
    print("Total number of possible combinations is", combos)

part2(ls)
# Ran in 0.00047 seconds