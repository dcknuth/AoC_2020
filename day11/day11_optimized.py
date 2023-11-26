'''AoC Day 11 Part 1: Simulate your seating area by applying the seating rules
repeatedly until no seats change state. How many seats end up occupied?
To optimize, let's look at the SeatStatus functions as they are at the inside
of a loop through the matrix. We can set a couple variables to have the sizes
of the matrix without repeatedly computing/fetching them, this helps a little.
I tried removing the custom compare function, that seems the same for time, but
is less code and reads a bit easier. Trying to remove the final whole matrix
compare by moving the test by element actually takes longer. We can also jump
out of counting when we get over 3 in the # case'''
import sys
sys.path.append("..")
import timef

#filename = "test11.txt"
filename = "input11.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')
MHEIGHT = len(ls)
MWIDTH = len(ls[0])
TEST_HEIGHT = len(ls) - 1
TEST_WIDTH = len(ls[0]) - 1

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
            if x < TEST_WIDTH and m[y-1][x+1] == '#':
                return('L')
        if x > 0 and m[y][x-1] == '#':
            return('L')
        if x < TEST_WIDTH and m[y][x+1] == '#':
            return('L')
        if y < TEST_HEIGHT:
            if m[y+1][x] == '#':
                return('L')
            if x > 0 and m[y+1][x-1] == '#':
                return('L')
            if x < TEST_WIDTH and m[y+1][x+1] == '#':
                return('L')
        return('#')
    if m[y][x] == '#':
        total = 0
        if y > 0:
            if m[y-1][x] == '#':
                total += 1
            if x > 0 and m[y-1][x-1] == '#':
                total += 1
            if x < TEST_WIDTH and m[y-1][x+1] == '#':
                total += 1
        if x > 0 and m[y][x-1] == '#':
            total += 1
            if total > 3:
                return('L')
        if x < TEST_WIDTH and m[y][x+1] == '#':
            total += 1
            if total > 3:
                return('L')
        if y < TEST_HEIGHT:
            if m[y+1][x] == '#':
                total += 1
                if total > 3:
                    return('L')
            if x > 0 and m[y+1][x-1] == '#':
                total += 1
                if total > 3:
                    return('L')
            if x < TEST_WIDTH and m[y+1][x+1] == '#':
                total += 1
                if total > 3:
                    return('L')
    return(m[y][x])

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
        for y in range(MHEIGHT):
            cur_row = []
            for x in range(MWIDTH):
                cur_row.append(SeatStatus(cur_state, y, x))
            next_state.append(cur_row)
        #PrintState(next_state)
        if cur_state == next_state:
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
# was 0.34329 seconds, now 0.28940

'''Part 2: Given the new visibility method and the rule change for occupied
seats becoming empty, once equilibrium is reached, how many seats end up
occupied?
To speed up this part we can move the test of the current cell up front and
then drop out of counting up visable items as soon as we know the answer for
the type we have. We will just be OK with the code getting long for the
moment'''
def SeatStatus2(m, y, x):
    '''Given a seating matrix and a seat, walk in each of the eight
    directions until seeing something or running off the matrix.
    Return the correct seat status'''
    if m[y][x] == 'L':
        # go North West
        cury = y
        curx = x
        moving = True
        while moving:
            cury -= 1
            curx -= 1
            if cury > -1 and cury < len(m) and curx > -1 and curx < len(m[0]):
                if m[cury][curx] == '#':
                    return('L')
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
                    return('L')
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
                    return('L')
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
                    return('L')
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
                    return('L')
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
                    return('L')
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
                    return('L')
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
                    return('L')
                elif m[cury][curx] == 'L':
                    moving = False
            else:
                moving = False
        return('#')
    elif m[y][x] == '#':
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
        if seen > 4:
            return('L')
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
        if seen > 4:
            return('L')
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
        if seen > 4:
            return('L')
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
        if seen > 4:
            return('L')
        return('#')
    else:
        return('.')

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
        if cur_state == next_state:
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
# was 0.94135 seconds, now 0.62439
