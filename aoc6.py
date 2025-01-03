import re
import time

from aoc_utils import fetch_aoc_input

grid = []
loc = (0,0)
dir = (-1,0)
path = []

def next_step(loc):
    global dir
    x1, y1 = dir
    r, c = loc
    r = r + x1
    c = c + y1
    return r,c

def isblocked(loc):
    r,c = next_step(loc)
    if grid[r][c] == "#":
        #print(f"Blocked at {loc}")
        return True
    else:
        return False

def turn_right():
    global dir
    if dir == (-1,0):
        newdir = (0,1)
    if dir == (0,1):
        newdir = (1,0)
    if dir == (1,0):
        newdir = (0,-1)
    if dir == (0,-1):
        newdir = (-1,0)

    dir = newdir
    return

def check_loop_append(locdir,path):
    if locdir in path:
        print (f"LOOP DETECTED AT {locdir}")
        return False
    else:
        path.append(locdir)
        return True

def grid_edge(loc):
    r,c = loc
    if r == X - 1 or c == Y - 1 or r == 0 or c == 0:
        #print (f"Exiting grid at {loc=}")
        return True
    else:
        return False

test="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def insert_into_grid(r, c, new_value):
    if r > X - 1 or c > Y -1 :
        print(f"Fatal error : Trying to insert beyond grid ({r},{c})")
        exit()
    v = list(grid[r])
    v[c] = new_value
    grid[r] = ''.join(v)


if __name__ == "__main__":
    data_input = fetch_aoc_input(6, 2024)
    #data_input = test.split()
    grid = data_input
    Y = len(grid)
    X = len(grid[0])
    print (f"{X=},{Y=}")
    for r,i in enumerate(grid):
        c = i.find("^")
        print (i)
        if c >= 0:
            loc = (r,c)

    print (loc)
    start_loc = loc
    dir = (-1, 0)

    while not grid_edge(loc):
        if not isblocked(loc):
            loc = next_step(loc)
            check_loop_append((loc,dir),path)
        else:
            turn_right()
        print(loc)

    # Find the unique positions (irrespective
    # of direction)
    p1 = [loc for (loc,dir) in path]
    p1 = set(p1)
    print(f"Unique positions = {len(p1)}")

    # PART 2
    print ("======= PART 2 =========")
    print ("This takes about 45 mins on a MacBook M3")
    loops = 0
    loop_info=[]
    for r in range(X):
        print(f"Laying obstructions on row {r} of {X}")
        for c in range(Y):
            start_time = time.perf_counter()
            old = grid[r][c]
            if grid[r][c] == "^":
                continue

            #print(f"New obstruction at ({r},{c})")
            # print("Press Enter to proceed..")
            # input()
            insert_into_grid(r,c,"#")

            loc = start_loc
            dir = (-1,0)
            #print (f"Starting loc at : {loc}")
            path = []
            while not grid_edge(loc):
                if not isblocked(loc):
                    loc = next_step(loc)
                    # if not check_loop_append((loc, dir), path):
                    #     loops +=1
                    #     print (f"Loop detected at {(loc,dir)=}with obstruction at ({r},{c})")
                    #     loop_info.append((r,c))
                    #     break

                    if (loc,dir) in path:
                        print(f"Loop detected at {(loc,dir)=} with obstruction at ({r},{c})")
                        loop_info.append((r, c))
                        break
                    else:
                        path.append((loc,dir))
                    end_time = time.perf_counter()

                else:
                    turn_right()

            insert_into_grid(r,c,old)
            exec_time = end_time - start_time
            #print(f"Execution time {exec_time:.6f} seconds")

    # Print loop info
    print (f"Obstructions causing loops = {len(loop_info)}")



