'''AoC Day07 Part1: How many individual bags are required inside your
single shiny gold bag?
The second part ran quite fast, so maybe I will leave that, but the
first part feels like it is a bit of a mess. We could try to search
outwards from the gold bag. However, we would still need the inward
rules dict for the second part'''
import time
from collections import defaultdict

#filename = "test07.txt"
filename = "input07.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

def canContain(target, rules):
    yes_list = [target,]
    # we should find a new containing bag in each loop, otherwise we
    #  are done
    done = False
    while not done:
        bags_left = set(rules.keys() ) - set(yes_list)
        found = False
        for bag in bags_left:
            if len(rules[bag]) == 0:
                continue
            contains_list = [x for x, y in rules[bag]]
            # test for shared colors with yes list
            if len(set(yes_list) & set(contains_list)) > 0:
                yes_list.append(bag)
                found = True
        if not found:
            done = True
    return(yes_list)

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
print("Number of colors that can contain a gold bag is", \
      len(contains_gold)-1)
print(f"Time taken was {T1-T0:0.5f} seconds")
''' 0.00975 (vs 0.01721 before) so a good speed up and this still
includes the creation of the rules dict. A next step might be to rework
the dict so that instead of a list of pairs (color, num) it has a list
of colors and a list of numbers or a sub-dict with colors as keys'''

'''Part 2: How many individual bags are required inside your single
shiny gold bag? (same as previous version)'''
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
