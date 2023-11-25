'''AoC Day 11 Part 1: Simulate your seating area by applying the seating rules
repeatedly until no seats change state. How many seats end up occupied?'''
import sys
sys.path.append("..")
import timef

#filename = "test11.txt"
filename = "input11.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

def SeatStatus(m, y, x):
    '''Given a matrix of seats and a seat by its row (y) and column (x),
    return if it is occupied (#), or empty (L). No need to look at floor (.)'''
    if m[y][x] == '.':
        return('.')
    if m[y][x] == 'L':
        if y > 0:
            if m[y-1][x] == '#':
                return('L')
            if x > 0 and m[y-1][x-1] == '#':
                return('L')
            if x < (len(m[y-1]) - 1) and m[y-1][x+1] == '#':
                return('L')
        if x > 0 and m[y][x-1] == '#':
            return('L')
        if x < (len(m[y]) - 1) and m[y][x+1] == '#':
            return('L')
        if y < (len(m) - 1):
            if m[y+1][x] == '#':
                return('L')
            if x > 0 and m[y+1][x-1] == '#':
                return('L')
            if x < (len(m[y+1]) - 1) and m[y+1][x+1] == '#':
                return('L')
        return('#')
    if m[y][x] == '#':
        total = 0
        if y > 0:
            if m[y-1][x] == '#':
                total += 1
            if x > 0 and m[y-1][x-1] == '#':
                total += 1
            if x < (len(m[y-1]) - 1) and m[y-1][x+1] == '#':
                total += 1
        if x > 0 and m[y][x-1] == '#':
            total += 1
        if x < (len(m[y]) - 1) and m[y][x+1] == '#':
            total += 1
        if y < (len(m) - 1):
            if m[y+1][x] == '#':
                total += 1
            if x > 0 and m[y+1][x-1] == '#':
                total += 1
            if x < (len(m[y+1]) - 1) and m[y+1][x+1] == '#':
                total += 1
        if total > 3:
            return('L')
    return(m[y][x])

def MCompare(m1, m2):
    for y, r in enumerate(m1):
        for x, c in enumerate(r):
            if c != m2[y][x]:
                return(False)
    return(True)

def PrintState(m):
    print("Current state is:")
    for row in m:
        print(''.join(row))
    print('\n')

@timef.timef
def part1(ls):
    cur_state = []
    for row in ls:
        cur_state.append([x for x in row])
    #PrintState(cur_state)
    found = False
    steps = 0
    while not found:
        next_state = []
        for y in range(len(cur_state)):
            cur_row = []
            for x in range(len(cur_state[0])):
                cur_row.append(SeatStatus(cur_state, y, x))
            next_state.append(cur_row)
        #PrintState(next_state)
        if MCompare(cur_state, next_state) == True:
            found = True
        else:
            cur_state = next_state
            steps += 1

    print("The number of steps to stabilize was", steps)
    total = 0
    for row in cur_state:
        total += ''.join(row).count('#')
    print("Number of occupied seats is", total)

part1(ls)
# Took 0.34329 seconds

'''Part 2: Given the new visibility method and the rule change for occupied
seats becoming empty, once equilibrium is reached, how many seats end up
occupied?'''
def SeatStatus2(m, y, x):
    '''Given a seating matrix and a seat, walk in each of the eight
    directions until seeing something or running off the matrix.
    Return the correct seat status'''
    if m[y][x] == '.':
        return(m[y][x])
    seen = 0
    # go North West
    cury = y
    curx = x
    moving = True
    while moving:
        cury -= 1
        curx -= 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go North
    cury = y
    curx = x
    moving = True
    while moving:
        cury -= 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go North East
    cury = y
    curx = x
    moving = True
    while moving:
        cury -= 1
        curx += 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go West
    cury = y
    curx = x
    moving = True
    while moving:
        curx -= 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go East
    moving = True
    cury = y
    curx = x
    while moving:
        curx += 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go South West
    cury = y
    curx = x
    moving = True
    while moving:
        cury += 1
        curx -= 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go South
    cury = y
    curx = x
    moving = True
    while moving:
        cury += 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # go South East
    cury = y
    curx = x
    moving = True
    while moving:
        cury += 1
        curx += 1
        if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
            if m[cury][curx] == '#':
                seen += 1
                moving = False
            elif m[cury][curx] == 'L':
                moving = False
        else:
            moving = False
    # and then the new measure of seen seats
    if m[y][x] == '#' and seen > 4:
        return('L')
    elif m[y][x] == 'L' and seen == 0:
        return('#')
    return(m[y][x])

@timef.timef
def part2(ls):
    cur_state = []
    for row in ls:
        cur_state.append([x for x in row])
    #PrintState(cur_state)
    found = False
    steps = 0
    while not found:
        next_state = []
        for y in range(len(cur_state)):
            cur_row = []
            for x in range(len(cur_state[0])):
                cur_row.append(SeatStatus2(cur_state, y, x))
            next_state.append(cur_row)
        #PrintState(next_state)
        if MCompare(cur_state, next_state) == True:
            found = True
        else:
            cur_state = next_state
            steps += 1

    print("The number of steps to stabilize was", steps)
    total = 0
    for row in cur_state:
        total += ''.join(row).count('#')
    print("Number of occupied seats is", total)

part2(ls)
# took 0.94135 seconds