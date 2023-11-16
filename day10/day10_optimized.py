'''AoC Day10 Part1: If you use every adapter in your bag at once, find
the distribution of joltage differences between the charging outlet, the
adapters, and your device. What is the nuber of 1-jolt differences
multiplied by the number of 3-jolt differences?
To optimize, there is not going to be a huge shift, but since we now know
the structure we can save work as we go from part one to two and we will
not need the pass to see what the max run length is'''
import sys
sys.path.append("..")
import timef
from collections import Counter

#filename = "test10.txt"
filename = "input10.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

run_lengths = []
@timef.timef
def part1(ls, rls):
    # get a list of integers
    l = [int(x) for x in ls]
    l.insert(0, 0)
    l.sort()
    # make a counter and count all the differences
    counts = Counter()
    this_run = 1
    i = 1
    while i < len(l):
        counts[l[i] - l[i-1]] += 1
        if l[i] - l[i-1] == 1:
            this_run += 1
        else:
            if this_run > 2:
                rls.append(this_run)
            this_run = 1
        i += 1
    if this_run > 2:
        rls.append(this_run)
    # and one more 3 for the last jump to the device
    counts[3] += 1
    print("1Js * 3Js is", counts[1] * counts[3])

part1(ls, run_lengths)
# First run was 0.00037 seconds, this time 0.00036
# There is no reason this would be faster, so will say it is the same

'''Part2: What is the total number of distinct ways you can arrange the
adapters to connect the charging outlet to your device?
Since we now have the list of runs >2, we should just be able to
run through and multiply'''
@timef.timef
def part2(rls):
    p = {3:2, 4:4, 5:7}
    combos = 1
    for j in rls:
        combos *= p[j]
    print("Total number of possible combinations is", combos)

part2(run_lengths)
# First ran in 0.00047 seconds and now 0.00017
# We got to avoid two runs through the list and I guess we could have
#  also done this part as we were in P1 for some more savings, but we
#  relied a good bit on knowing what part 2 would ask
