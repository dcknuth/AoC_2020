'''This probably will not benifit much from optimization, so
let's just do it in a different way, with regex.
Part 1 How many passwords are valid given the policy list'''
import re, time
#filename = "test02.txt"
filename = "input02.txt"
with open(filename) as f:
    ls = f.read().strip().split("\n")

T0 = time.time()
count = 0
pattern = re.compile(r'(\d+)-(\d+) (\w): (.*)')
for l in ls:
    match = pattern.match(l)
    low = int(match.group(1))
    high = int(match.group(2))
    if low <= len(re.findall(match.group(3), match.group(4))) <= high:
        count += 1
T1 = time.time()
print("Number of valid passwords is", count)
print("They were found in", T1-T0, "seconds")

'''Part 2 How many passwords are valid given the change in
validation instructions'''
T0 = time.time()
count = 0
# We can still use the pattern above to get the initial parts
for l in ls:
    match = pattern.match(l)
    low = int(match.group(1)) - 1
    high = int(match.group(2)) - 1
    delta = (high - low) -1
    c = match.group(3)
    # We need something that can get the exact position of the letter
    #  in the final string and that it is only in one of the two
    #  positions. Unfortunatly, I think this has to go inside the loop
    pat2 = re.compile(f'^.{{{low}}}{c}{{1}}.{{{delta}}}[^{c}]{{1}}.*|'
                      f'^.{{{low}}}[^{c}]{{1}}.{{{delta}}}{c}{{1}}.*')
    mat2 = pat2.match(match.group(4))
    if mat2 != None:
        count += 1
T1 = time.time()
print("Updated number of valid passwords is", count)
print("Found in", T1-T0, "seconds")

# The first part ran in 0.001 seconds and the second in 0.07 seconds
# We only had to generate the pattern once in the first part, which
#  seems to have kept it competitive with the first solution attempt.
#  Since we had to keep compiling the pattern inside the loop for the
#  second part, it took a bit longer. Good regex practice though