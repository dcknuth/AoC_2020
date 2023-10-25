'''AoC Day08 Part1: Immediately before any instruction is executed a second
time, what value is in the accumulator?'''

filename = "test08.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

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
        ins, num = ls[i[0]].split()
        num = int(num)
        instructions[ins](a, i, num)

        


