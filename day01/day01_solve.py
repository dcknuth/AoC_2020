'''Part 1: Find the two entries that sum to 2020
then multiply those two numbers together'''
import time

#filename = 'test01.txt'
filename = 'input01.txt'
with open(filename) as f:
    ls = f.read().strip().split('\n')

l = [int(x) for x in ls]

# We will time the less accurate way for now
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
# A triple nested loop is probably the easiest way to go
found = False
for i, x in enumerate(l):
    if found:
        break
    for j, y in enumerate(l[i+1:]):
        if found:
            break
        for z in l[i+j+2:]:
            if x + y + z == 2020:
                print("Answer is", x * y * z)
                found == True
                break
T1 = time.time()
print("Time for part two was", T1-T0, "seconds")
