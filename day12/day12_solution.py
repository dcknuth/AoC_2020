'''AoC Day 12 Part 1: Figure out where the navigation instructions lead.
What is the Manhattan distance between that location and the ship's starting
position?'''
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
    value = int(instruction[1:])
    if action == 'N':
        y += value
    elif action == 'S':
        y -= value
    elif action == 'E':
        x += value
    elif action == 'W':
        x -= value
    elif action == 'L':
        f = (f - value) % 360
    elif action == 'R':
        f = (f + value) % 360
    elif action == 'F':
        if f == 90:
            x += value
        elif f == 180:
            y -= value
        elif f == 270:
            x -= value
        elif f == 0:
            y += value
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
# took .00063 seconds

'''Part 2: Using the modified instructions, figure out where the navigation
instructions actually lead. What is the Manhattan distance between that
location and the ship's starting position?'''
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
        newx = wpx * math.cos(radians) - wpy * math.sin(radians)
        wpy = round(wpx * math.sin(radians) + wpy * math.cos(radians))
        wpx = round(newx)
    elif action == 'R':
        radians = math.radians(-value)
        newx = wpx * math.cos(radians) - wpy * math.sin(radians)
        wpy = round(wpx * math.sin(radians) + wpy * math.cos(radians))
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
# Took 0.00065 seconds