'''AoC Day08 Part1: Immediately before any instruction is executed a second
time, what value is in the accumulator?
I might try removing the fuctions from the first part in favor of if
statements and flatten the lists to just integers for i and a'''
import sys
sys.path.append("..")
import timef

#filename = "test08.txt"
filename = "input08.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

@timef.timef
def run(prog):
    i = 0
    a = 0
    has_run = dict()
    while i not in has_run:
        has_run[i] = True
        ins, num = prog[i].split()
        if ins == 'acc':
            a += int(num)
            i += 1
        elif ins == 'jmp':
            i += int(num)
        else:
            i += 1
    return(a)

a = run(ls)
print(f"Value in acc before looping is {a}")
# part 1 took 0.0008 seconds (vs. 0.00011 for first solution)
# not bad. Tried a list of has_run instead of a dict, but it was slower,
#  as would be expected


'''Part 2: Fix the program so that it terminates normally by changing
exactly one jmp (to nop) or nop (to jmp). What is the value of the
accumulator after the program terminates?
Since our part1 speedup worked, we should adopt that here. Since we are now
running through the program many times, it might be worth some additional
pre-processing on the prog format to save on splits and int conversions'''
def terms(prog):
    '''Same as the run function in part1 but returns True plus the acc value
    if the program teminates properly and False plus the acc value if not'''
    i = 0
    a = 0
    has_run = dict()
    while i < len(prog) and i not in has_run:
        has_run[i] = True
        ins, num = prog[i]
        if ins == 'acc':
            a += num
            i += 1
        elif ins == 'jmp':
            i += num
        else:
            i += 1
    if i >= len(prog):
        return(True, a)
    return(False, a)

@timef.timef
def findProg(orig):
    '''Take the original program and change nops and jmps until we get
    proper termination and return that acc value'''
    # make a base program list so we can reduce int() and split()
    prog = []
    for line in orig:
        x, y = line.split()
        prog.append([x, int(y)])
    line = 0
    while line < len(prog):
        ins, num = prog[line]
        if ins == 'nop':
            prog[line][0] = "jmp"
            termed, a = terms(prog)
            prog[line][0] = "nop"
            if termed:
                return(a)
        elif ins == 'jmp':
            prog[line][0] = "nop"
            termed, a = terms(prog)
            prog[line][0] = "jmp"
            if termed:
                return(a)
        line += 1
    print("Didn't seem to find a replacement that worked")
    return(-1)

a = findProg(ls)
print(f"Acc value for the working program was {a}")
# With just the changes from part1, part2 took 0.00823 seconds (vs 0.01004
#  for first solution). It went down to 0.00464 with the reformat to only
#  do the int() and split() once per line. A final modification to just
#  change the list item between jmp/nop and back instead of a new list only
#  showed a small improvement to 0.00444