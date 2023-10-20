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
print(timeit.timeit("part1(ls)", setup="from __main__ import part1, ls", \
                    number=1000))
# ~1.54 seconds for 1000 times

'''Part 2: For each group, count the number of questions to which everyone
answered "yes". What is the sum of those counts?'''
def part2(ls):
    count = 0
    # going to do the same thing, but use an intersection on the sets
    cur_answers = set(list(ls[0]))
    i = 1
    while i < len(ls):
        if ls[i] == '':
            count += len(cur_answers)
            if i + 1 < len(ls):
                cur_answers = set(list(ls[i+1]))
            i += 1
            continue
        cur_answers = cur_answers & set(list(ls[i]))
        i += 1
    count += len(cur_answers)
    return(count)

print("Sum of group answers is", part2(ls))
print(timeit.timeit("part2(ls)", setup="from __main__ import part2, ls", \
                    number=1000))
# ~1.75 seconds for 1000 times
