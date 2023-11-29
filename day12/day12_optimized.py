'''AoC Day 12 Part 1: Figure out where the navigation instructions lead.
What is the Manhattan distance between that location and the ship's starting
position?
I'm a bit surprised on how fast the first part ran and how close to the
same time the second part was. We could try to delay converting the value
in part 1 and remove that variable; maybe a very slight speed up, but almost
nothing. Assuming the rotations are always < 360 we could try to get rid of
the modulus operators; doesn't seem to make any difference'''
import sys
sys.path.append("..")
import timef

#filename = "test12.txt"
filename = "input12.txt"

with open(filename) as f:
    ls = f.read().strip().split("\n")

def move(x, y, f, instruction):
    '''Take a current xy coord, the direction the ship is facing and an
    instruction and return the new xy cord and the direction'''
    action = instruction[0]
    if action == 'N':
        y += int(instruction[1:])
    elif action == 'S':
        y -= int(instruction[1:])
    elif action == 'E':
        x += int(instruction[1:])
    elif action == 'W':
        x -= int(instruction[1:])
    elif action == 'L':
        f -= int(instruction[1:])
        if f < 0:
            f += 360
    elif action == 'R':
        f += int(instruction[1:])
        if f >= 360:
            f -= 360
    elif action == 'F':
        if f == 90:
            x += int(instruction[1:])
        elif f == 180:
            y -= int(instruction[1:])
        elif f == 270:
            x -= int(instruction[1:])
        elif f == 0:
            y += int(instruction[1:])
        else:
            print("Error: direction invalid")
    return(x, y, f)

@timef.timef
def part1(ls):
    x = y = 0
    f = 90
    for i in ls:
        x, y, f = move(x, y, f, i)
    print("Manhattan distance from start is", abs(x) + abs(y))

part1(ls)
# was 0.00063 seconds and now is 0.00059

'''Part 2: Using the modified instructions, figure out where the navigation
instructions actually lead. What is the Manhattan distance between that
location and the ship's starting position?
To optimize we can just compute the sin and cos once, but given the results
of part 1, I don't think it will do much; maybe slightly better, but so
small that we would need to use timeit to average a 1000 to see if there
was a real difference. We could try to remove the math module operations
or use complex numbers, but I think this is just how long it takes to go
through the list'''
import math
def newMove(x, y, wpx, wpy, instruction):
    '''Given xy for the ship and xy for the waypoint, perform the given
    instruction and return the two positions'''
    action = instruction[0]
    value = int(instruction[1:])
    if action == 'N':
        wpy += value
    elif action == 'S':
        wpy -= value
    elif action == 'E':
        wpx += value
    elif action == 'W':
        wpx -= value
    elif action == 'L':
        radians = math.radians(value)
        my_cos = math.cos(radians)
        my_sin = math.sin(radians)
        newx = wpx * my_cos - wpy * my_sin
        wpy = round(wpx * my_sin + wpy * my_cos)
        wpx = round(newx)
    elif action == 'R':
        radians = math.radians(-value)
        my_cos = math.cos(radians)
        my_sin = math.sin(radians)
        newx = wpx * my_cos - wpy * my_sin
        wpy = round(wpx * my_sin + wpy * my_cos)
        wpx = round(newx)
    elif action == 'F':
        x += value * wpx
        y += value * wpy
    return(x, y, wpx, wpy)

@timef.timef
def part2(ls):
    x = y = 0
    wpx = 10
    wpy = 1
    for i in ls:
        x, y, wpx, wpy = newMove(x, y, wpx, wpy, i)
        #print(f"x={x} y={y} wpx={wpx} wpy={wpy}")
    print("Manhattan distance from start is", abs(x) + abs(y))

part2(ls)
# was 0.00064 seconds, and now 0.00060