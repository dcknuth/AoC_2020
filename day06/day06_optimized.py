'''AoC Day 6 part 1: For each group, count the number of questions to which
anyone answered "yes". What is the sum of those counts?
I actually liked the set based solution as it was a nice fit with part 2
Use of timeit was harder than in Spider with Ipython where you have a
magic %timeit that seems to not need the setup'''
# let's try a dict and a Counter to see if that will be faster
import timeit
from collections import Counter

#filename = "test06.txt"
filename = "input06.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

def part1(ls):
    count = 0
    cur_count = dict()
    for l in ls:
        if l == '':
            count += len(cur_count)
            cur_count = dict()
        else:
            for c in l:
                cur_count[c] = True
    count += len(cur_count)
    return(count)

print("Sum of group answer counts is", part1(ls))
print(timeit.timeit("part1(ls)", setup="from __main__ import part1, ls", \
                    number=1000))
# ~0.71 seconds for 1000 times

'''Part 2: For each group, count the number of questions to which everyone
answered "yes". What is the sum of those counts?'''
def part2(ls):
    count = 0
    # use a counter and then add the number of items matching the number
    #  of lines, or 0
    cur_count = Counter()
    num_people = 1
    for l in ls:
        if l == '':
            all_yes = [x for x, y in cur_count.items() if y == num_people - 1]
            count += len(all_yes)
            cur_count = Counter()
            num_people = 1
            continue
        for c in l:
            cur_count[c] += 1
        num_people += 1
    all_yes = [x for x, y in cur_count.items() if y == num_people - 1]
    count += len(all_yes)
    return(count)

print("Sum of group answers is", part2(ls))
print(timeit.timeit("part2(ls)", setup="from __main__ import part2, ls", \
                    number=1000))
# ~3.7 seconds for 1000 times
'''The first part with a dict was a good bit faster, but using the Counter
was a good bit slower for the second part'''
