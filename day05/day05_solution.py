'''AOC Day 5: Part 1: What is the highest seat ID on a boarding pass?'''
import time

filename = "input05.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

T0 = time.time()
max_id = 0
for l in ls:
    row = ['1' if x == 'B' else '0' for x in l[0:7]]
    rn = int(''.join(row), 2)
    col = ['1' if x == 'R' else '0' for x in l[7:]]
    cn = int(''.join(col), 2)
    seat_id = rn * 8 + cn
    if seat_id > max_id:
        max_id = seat_id
T1 = time.time()
print("The highest seat ID is", max_id)
print("Time taken for part one was", T1-T0, "seconds")
