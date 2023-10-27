'''AoC Day08 Part1: Immediately before any instruction is executed a second
time, what value is in the accumulator?
This time, I am using a timing function to get the times with a decorator,
but I'm not sure it's worth doing. Still, will probably do it this way for
a few days'''
import sys
sys.path.append("..")
import timef

#filename = "test08.txt"
filename = "input08.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

@timef.timef
def run(prog):
    i = [0]
    a = [0]
    has_run = dict()
    def acc(a, i, n):
        a[0] += n
        i[0] += 1

    def jmp(a, i, n):
        i[0] += n
    
    def nop(a, i, n):
        i[0] += 1
    
    instructions = {"acc":acc, "jmp":jmp, "nop":nop}
    while i[0] not in has_run:
        has_run[i[0]] = True
        ins, num = prog[i[0]].split()
        num = int(num)
        instructions[ins](a, i, num)
    return(a[0])

a = run(ls)
print(f"Value in acc before looping is {a}")
# part 1 took 0.00011 seconds


'''Part 2: Fix the program so that it terminates normally by changing
exactly one jmp (to nop) or nop (to jmp). What is the value of the
accumulator after the program terminates?
We can make a terminates() function to test for proper execution and a
findProg() function to replace nops and jmps until one works'''
def terms(prog):
    '''Same as the run function in part1 but returns True plus the acc value
    if the program teminates properly and False plus the acc value if not'''
    i = 0
    a = [0]
    has_run = dict()
    def acc(a, i, n):
        a[0] += n
        return(i + 1)

    def jmp(a, i, n):
        return(i + n)
    
    def nop(a, i, n):
        return(i + 1)
    
    instructions = {"acc":acc, "jmp":jmp, "nop":nop}
    while i < len(prog) and i not in has_run:
        has_run[i] = True
        ins, num = prog[i].split()
        num = int(num)
        i = instructions[ins](a, i, num)
    if i >= len(prog):
        return(True, a[0])
    return(False, a[0])

@timef.timef
def findProg(orig):
    '''Take the original program and change nops and jmps until we get
    proper termination and return that acc value'''
    line = 0
    while line < len(orig):
        ins, num = orig[line].split()
        if ins == 'nop':
            cur_prog = orig[:line]
            cur_prog.append(f"jmp {num}")
            cur_prog.extend(orig[line+1:])
            termed, a = terms(cur_prog)
            if termed:
                return(a)
        elif ins == 'jmp':
            cur_prog = orig[:line]
            cur_prog.append(f"nop {num}")
            cur_prog.extend(orig[line+1:])
            termed, a = terms(cur_prog)
            if termed:
                return(a)
        line += 1
    print("Didn't seem to find a replacement that worked")
    return(-1)

a = findProg(ls)
print(f"Acc value for the working program was {a}")
# part2 took 0.01004 seconds