'''Part 1 How many passwords are valid given the policy list'''
import time
#filename = "test02.txt"
filename = "input02.txt"
with open(filename) as f:
    ls = f.read().strip().split("\n")
T0 = time.time()
count = 0
for l in ls:
    r, c, s = l.split()
    low, high = map(int, r.split('-'))
    n = s.count(c[0])
    if n >= low and n <= high:
        count += 1
T1 = time.time()
print("Number of valid passwords is", count)
print("First set fround in", T1-T0, "seconds")

'''Part 2 How many passwords are valid given the change in
validation instructions'''
T0 = time.time()
count = 0
for l in ls:
    r, c, s = l.split()
    low, high = map(int, r.split('-'))
    if s[low-1] == c[0] and s[high-1] != c[0]:
        count += 1
    elif s[low-1] != c[0] and s[high-1] == c[0]:
        count += 1
T1 = time.time()
print("Updated number of valid passwords is", count)
print("Second set found in", T1-T0, "seconds")

# Both finish in about 0.001 seconds