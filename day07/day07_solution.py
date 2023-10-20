'''AoC Day07 Part1: How many individual bags are required inside your
single shiny gold bag?'''
import time
from collections import defaultdict

#filename = "test07.txt"
filename = "input07.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

def canContain(bag, rules):
    '''Takes the bag color you want to know about and a dict of the bag
    rules and returns the list of bags that might, eventually, contain it'''
    yes_list = []
    no_list = []
    # First get a list of possibles, removing the "no other" and those
    #  that directly contain the bag we are looking for
    possible_bags = []
    for color in rules.keys():
        if len(rules[color]) == 0 or color == bag:
            no_list.append(color)
            continue
        for sub_bag in rules[color]:
            sub_color, num_bags = sub_bag
            if sub_color == bag:
                yes_list.append(color)
            elif color not in no_list and color not in yes_list \
                and color not in possible_bags:
                possible_bags.append(color)
    # Now work through the list of possible bags until it's empty
    while len(possible_bags) > 0:
        cur_bag = possible_bags.pop()
        cur_list = [x for x, y in rules[cur_bag]]
        found = False
        while not found:
            new_list = []
            for sub_bag in cur_list:
                if sub_bag in no_list:
                    continue
                if sub_bag in yes_list:
                    yes_list.append(cur_bag)
                    found = True
                    break
                sub_list = [x for x, y in rules[sub_bag]]
                if bag in sub_list:
                    found = True
                    yes_list.append(sub_bag)
                    break
                new_list.append(sub_bag)
            if len(new_list) == 0 and not found:
                no_list.append(cur_bag)
                break
            cur_list = new_list
    # should be done, return yes_list
    return(yes_list)

# I guess perf_counter() is a better fit than the time() function we
#  have used a couple times. It should give a more accurate measure of
#  how long we have been running, but is not seconds-since-epoch and so
#  can't be used to get the current time.
# timeit() might still be better, but let's try this
T0 = time.perf_counter()
# make the rules dict
rules = defaultdict()
for l in ls:
    p1, p2 = l.split(" contain ")
    color = p1.split()
    if "no other" in p2:
        rules[' '.join(color[:2])] = []
    else:
        contains = []
        for bag in list(p2.split(',')):
            words = bag.split()
            contains.append([' '.join(words[1:3]), int(words[0])])
        rules[' '.join(color[:2])] = contains
# get the bags that can contain a gold bag
contains_gold = canContain("shiny gold", rules)
T1 = time.perf_counter()
print("Number of colors that can contain a gold bag is", len(contains_gold))
print("Took", T1-T0, "seconds")
