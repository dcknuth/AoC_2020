'''AoC Day07 Part1: How many individual bags are required inside your
single shiny gold bag?
OK, one more optimization as suggested in the last version, turn some
lists into dictionaries'''
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
        bags_left = set(rules.keys()) - set(yes_list)
        found = False
        for bag in bags_left:
            if len(rules[bag]) == 0:
                continue
            contains_list = rules[bag].keys()
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
        contains = dict()
        for bag in list(p2.split(',')):
            words = bag.split()
            contains[' '.join(words[1:3])] = int(words[0])
        rules[' '.join(color[:2])] = contains
T1 = time.perf_counter()
# get the bags that can contain a gold bag
contains_gold = canContain("shiny gold", rules)
T2 = time.perf_counter()
print("Number of colors that can contain a gold bag is", \
      len(contains_gold)-1)
print(f"Time taken to make rules was {T1-T0:0.5f} seconds")
print(f"Time taken to find gold bag containers was {T2-T1:0.5f} seconds")
print(f"Total time was {T2-T0:0.5f} seconds")
''' 0.00822 (vs 0.00975 for the last optimized version) so a small
improvement and cleaner code'''

'''Part 2: How many individual bags are required inside your single
shiny gold bag? (now updated to use the sub-dict)'''
# We still have our rules dict, so maybe just a recursive function
def bagsIn(bag, rules):
    '''Take a bag color and the dict of rules and return the total number
    of bags it contains'''
    sub_bags = rules[bag]
    if len(sub_bags) == 0:
        return(0)
    num_bags = sum(sub_bags.values())
    for sub_bag in sub_bags.keys():
        num_bags += sub_bags[sub_bag] * bagsIn(sub_bag, rules)
    return(num_bags)

T0 = time.perf_counter()
total_bags = bagsIn("shiny gold", rules)
T1 = time.perf_counter()
print("The number of bags in a shiny gold bag is", total_bags)
print(f"Time taken was {T1-T0:0.5f} seconds")
'''This ran in 0.00002 seconds, so a little faster and a little cleaner
code here also'''