'''Part 1: Find the two entries that sum to 2020
then multiply those two numbers together'''
import time

#filename = 'test01.txt'
filename = 'input01.txt'
with open(filename) as f:
    ls = f.read().strip().split('\n')

l = [int(x) for x in ls]

# Since part one only took 0.002 seconds, we are not going to optimize
T0 = time.time()
# A nested loop is probably the easiest way to go
found = False
for i, x in enumerate(l):
    if found:
        break
    for y in l[i+1:]:
        if x + y == 2020:
            print("Answer is", x * y)
            found == True
            break
T1 = time.time()
print("Time for part one was", T1-T0, "seconds")


'''Part 2: Find the three entries that sum to 2020
then multiply those numbers together'''
T0 = time.time()
# Maybe we can sort the list and then find if there is a last
#  number match fast
l.sort()
#T1 = time.time()
#print("Time for sort was", T1-T0, "seconds")
# The sort was quick, so we might be on to something
# Let's use bisect and do a binary search for the third number
import bisect
found = False
for i, x in enumerate(l):
    if found:
        break
    for j, y in enumerate(l[i+1:]):
        if found:
            break
        zlist = l[i+j+2:]
        # Now we need to use the sorted order for a fast search
        index = bisect.bisect_left(zlist, 2020 - (x + y))
        if index != len(zlist) and zlist[index] == 2020 - (x + y):
            print("Answer is", x * y * (2020 - (x + y)))
            found == True
            break
T1 = time.time()
print("Time for part two was", T1-T0, "seconds")
# We were able to reduce the time from 0.187 sec to 0.016


# One more idea, we could store the list in a dict and see if
#  the number we need is there directly
T0 = time.time()
zdict = {x:True for x in l}
found = False
for i, x in enumerate(l):
    if found:
        break
    for j, y in enumerate(l[i+1:]):
        if found:
            break
        z = 2020 - (x + y)
        if z in zdict and z != x and z != y:
            print("Answer is", x * y * z)
            found = True
            break
T1 = time.time()
print("Time for part two with a dict was", T1-T0, "seconds")
# This seems to have gotten the time down to pretty much the same
#  as part one and below this timing method's threshold
