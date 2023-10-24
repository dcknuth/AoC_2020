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
    visited = []
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
    def contains(target, cbag, rules, no_list, yes_list):
        '''Given a bag, a target bag and rules, return True if the
        target is in the bag (or sub-bag) or False if not'''
        if cbag in no_list:
            return(False)
        cur_list = [x for x, y in rules[cbag]]
        if target in cur_list:
            return(True)
        for sub_bag in cur_list:
            if contains(target, sub_bag, rules, no_list, yes_list):
                return(True)
        return(False)

    # Now work through the list of possible bags until it's empty
    for cur_bag in possible_bags:
        if contains(bag, cur_bag, rules, no_list, yes_list):
            yes_list.append(cur_bag)
        else:
            no_list.append(cur_bag)
    # Remove any duplicates
    yes_list = list(set(yes_list))
    return(yes_list)

# I guess perf_counter() is a better fit than the time() function we
#  have used a few times so far. It should give a more accurate measure
#  of how long we have been running, but is not seconds-since-epoch and
#  so can't be used to get the current time.
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
print(f"Time taken was {T1-T0:0.5f} seconds")
# 0.01721

'''Part 2: How many individual bags are required inside your single
shiny gold bag?'''
# We still have our rules dict, so maybe just a recursive function
def bagsIn(bag, rules):
    '''Take a bag color and the dict of rules and return the total number
    of bags it contains'''
    sub_bags = rules[bag]
    if len(sub_bags) == 0:
        return(0)
    num_bags = sum([x[1] for x in sub_bags])
    for sub_bag in sub_bags:
        col, num = sub_bag
        num_bags += num * bagsIn(col, rules)
    return(num_bags)

T0 = time.perf_counter()
total_bags = bagsIn("shiny gold", rules)
T1 = time.perf_counter()
print("The number of bags in a shiny gold bag is", total_bags)
print(f"Time taken was {T1-T0:0.5f} seconds")
# 0.00003