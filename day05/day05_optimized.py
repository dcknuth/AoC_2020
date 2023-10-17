'''AOC Day 5: Part 1: What is the highest seat ID on a boarding pass?
Since we now know that we will have to look for a gap in part 2, we
can change our part 1 a little to save the IDs and only do one pass
through the list'''
import time

filename = "input05.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

T0 = time.time()
seats = []
for l in ls:
    row = ['1' if x == 'B' else '0' for x in l[0:7]]
    rn = int(''.join(row), 2)
    col = ['1' if x == 'R' else '0' for x in l[7:]]
    cn = int(''.join(col), 2)
    seats.append(rn * 8 + cn)
# sort them
seats.sort()
T1 = time.time()
print("The highest seat ID is", seats[-1])
print("Time taken for part one was", T1-T0, "seconds")

'''Part 2: Your seat wasn't at the very front or back, though;
 the seats with IDs +1 and -1 from yours will be in your list.
What is the ID of your seat?'''
T0 = time.time()
# This time we only need to find the missing seat
cur_seat = seats[0]
for seat in seats[1:]:
    if seat != cur_seat + 1:
        print("Our seat ID is", cur_seat + 1)
        break
    cur_seat = seat
T1 = time.time()
print("Time taken for part two was", T1-T0, "seconds")
'''This seems to have taken about 0.001 seconds for the first part
and 0 for the second part'''
