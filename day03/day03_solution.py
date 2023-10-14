'''Part 1: Starting at the top-left corner of your map and following
a slope of right 3 and down 1, how many trees would you encounter?'''
import time

#filename = 'test03.txt'
filename = 'input03.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

T0 = time.time()
# Starting x position is 0
x = 0
# We go right 3 each time
step = 3
trees_hit = 0
# We need to step down the number of lines in the input, minus 1
for y in range(1, len(ls)):
    # add the step and loop around if needed
    x = (x+step) % len(ls[0])
    if ls[y][x] == '#':
        trees_hit += 1
T1 = time.time()
print("We hit", trees_hit, "trees with run time of", T1-T0, "seconds")
# This ran fast enough to round to 0 with this timing method

'''Part 2: Check some additional slopes and multiply all the totals
together'''
T0 = time.time()
total = trees_hit
# steps we did not already try, x,y
step_list = [[1,1], [5,1], [7,1], [1,2]]
for step_x, step_y in step_list:
    trees_hit = 0
    x = y = 0
    y += step_y
    while y < len(ls):
        x = (x+step_x) % len(ls[0])
        if ls[y][x] == '#':
            trees_hit += 1
        y += step_y
    total *= trees_hit
T1 = time.time()
print("Part2 answer is", total, "in a time of", T1-T0, "seconds")
# This was also fast enough to round to 0
