'''AoC Day 6 part 1: For each group, count the number of questions to which
anyone answered "yes". What is the sum of those counts?'''
# lets use timeit as we might need a more accurate measure to see if we
#  were successful in optimizing this one
import timeit

#filename = "test06.txt"
filename = "input06.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

def part1(ls):
    count = 0
    # if we use a set, each answer will only count once
    cur_answers = set()
    for l in ls:
        if l == '':
            count += len(cur_answers)
            cur_answers = set()
        else:
            # we will union sets for each group, which should remove dups
            cur_answers = cur_answers | set(list(l))
    count += len(cur_answers)
    return(count)

print("Sum of group answer counts is", part1(ls))
print(timeit.timeit("part1(ls)", setup="from __main__ import part1, ls", number=100))
