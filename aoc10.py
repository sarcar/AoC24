from typing import Tuple

from aoc_utils import fetch_aoc_input


class Cell:
    def __init__(self,r,c,v):
        self.r = r
        self.c = c
        self.value = v

class Map:
    def __init__(self, vec):
        self.ROWS = len(vec)
        self.COLS = len(vec[0])
        self.c_OOB = "X"  # character to denote Out of Bounds
        #self.cellmap = [[r[y] for y in range(self.COLS)] for r in vec]

        self.cellmap = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]

        for i,row in enumerate(vec):
            cell = None
            for j,c in enumerate(row):
                if c == ".":
                    c = -99
                cell = Cell(i+1,j+1,c)
                #print (cell)
                self.cellmap[i][j] = cell
                #print(f"cellmap[{i}][{j}] = {c}({cell.value}<{self.cellmap[i][j].value}>)")
                #print(f"cellmap[2][2] = {self.cellmap[2][2]}")


    def getRC(self, row, col):
        # assert row >=1 and col >=1 and row <= self.ROWS and col <= self. COLS, f"Invalid row/col fetch {row=},{col=} from Map of size : {self.ROWS}, {self.COLS}"
        oob = row <= 0 or row > self.ROWS or col <=0 or col > self.COLS
        if oob:
            return None
        else:
            cell = self.cellmap[row - 1][col - 1]
            return cell.value


    def show(self):
        for r in range(1, self.ROWS + 1):
            for c in range(1, self.COLS + 1):
                ch = self.getRC(r, c)
                if ch == -99:
                    ch = "."
                #print(f"At {r=},{c=}, value is {ch}")
                print(ch,end='')
            print()

    def findall(self, char):
        ret = []
        for r in range(1, self.ROWS + 1):
            for c in range(1, self.COLS + 1):
                if self.getRC(r, c) == char:
                    ret.append((r, c))

        return ret

    def isPathOut(self, curr_row,curr_col, path, multipaths):
        # visited.append((curr_row,curr_col))
        path.append((curr_row, curr_col))
        print(f"Appended to path {path=}")
        potential = []

        v = self.getRC(curr_row,curr_col)
        if int(v) == 9:
            print (f"Ending at 9 : ({curr_row},{curr_col})")
            print(f"Final PATH = {path=}")
            multipaths.append(path.copy())
            path.pop(-1)
            return True

        nbors = self.neighbors((curr_row,curr_col))
        #print (f"Neighbours = {nbors}")
        for n in nbors:
            if n[1] is None:
                continue

            #print(f"Looking into nbor : {n=}")
            if int(n[1]) == int(v) + 1:
                potential.append(n[0])

        #print(f"Potential = {potential}")
        if len(potential) == 0:
            return False

        for p in potential:
            #print(f"Going down potential ({p[0]},{p[1]})")
            thisway = self.isPathOut(p[0],p[1],path, multipaths)
            if not thisway:
                path.pop(-1)
            else:
                continue

    # Given row, col, return a vec/hash of my neighbors
    def neighbors(self, tuprc):
        row,col = tuprc
        n = [None] * 4
        for idx,(d1,d2) in enumerate([(-1,0),(0,1),(1,0),(0,-1)]):
            loc = (row+d1,col+d2)
            nvalue = self.getRC(row+d1,col+d2)
            if nvalue is None:
                loc = None
            n[idx] = (loc,nvalue)

        return n

#######
# Data section
test_data = """
0123
1234
8765
9876
"""

test_data2 = """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

test_data3="""
..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

test_data4="""
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

test_data5="""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
#
########


if __name__ == "__main__":
    #input_data = test_data5.split()
    input_data = fetch_aoc_input(10,2024)
    topomap = Map(input_data)
    topomap.show()

    # Find trail heads
    th = topomap.findall("0")
    print(f"Found {len(th)} trailheads (0-s) at : {th}")

    total_th_score = 0
    total_rating = 0
    for h in th:
        p = []
        mp = []
        mpath = 0
        score = 0
        startrow, startcol = h
        topomap.isPathOut(startrow, startcol,p, mp)

        print()
        print (f"Multipaths for [{startrow},{startcol}]")
        z = set()
        for i,p in enumerate(mp):
            print(f"{i:02d}:{p}")
            z.add(p[-1])

        mpath = len(mp)
        score = len(z)
        print (f"Trail score = {score}")

        total_th_score += score
        total_rating += mpath


    print(f"FINAL TRAIL SCORE = {total_th_score}")
    print(f"FINAL TRAIL RATING = {total_rating}")