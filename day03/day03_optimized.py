'''Part 1: Starting at the top-left corner of your map and following
a slope of right 3 and down 1, how many trees would you encounter?
This probably is another case where this does not really need an
optimization. Maybe it would be interesting to do it as a numpy
solution for the sake of practice?'''
import time
import numpy as np

#filename = 'test03.txt'
filename = 'input03.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')
# create a nice array of 0s and 1s
m = [[1 if x == '#' else 0 for x in y] for y in ls]
matrix = np.array(m)
T0 = time.time()
# need to generate a list of all the column indexes that would match
#  the one down three over steps so that we can use it in a numpy
#  array selection
cols = np.array([x % len(ls[0]) for x in range(0, len(ls) * 3, 3)])
rows = np.array([x for x in range(0, len(ls))])
trees_hit = np.sum(matrix[rows, cols])
T1 = time.time()
print("We hit", trees_hit, "trees with run time of", T1-T0, "seconds")

'''Part 2: Check some additional slopes and multiply all the totals
together'''
T0 = time.time()
total = trees_hit
# steps we did not already try, x,y
step_list = [[1,1], [5,1], [7,1], [1,2]]
for step_x, step_y in step_list:
    cols = np.array([x % len(ls[0]) for x in range(0, len(ls) * step_x, step_x)])
    rows = np.array([x for x in range(0, len(ls), step_y)])
    # when we start skipping rows, we need to trim the number of columns
    #  to match
    trees_hit = np.sum(matrix[rows, cols[0:len(rows)]])  
    total *= trees_hit
T1 = time.time()
print("Part2 answer is", total, "in a time of", T1-T0, "seconds")
# Once again, this ran fast enough to round to 0 with this timing
#  method, but is a little convoluted and probably only good for
#  numpy practice
