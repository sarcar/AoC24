import itertools
import math
import re

from aoc_utils import fetch_aoc_input


class Antenna:
    # Constructor to initialize attributes
    def __init__(self, x, y, name):
        self.row = int(x)
        self.col = int(y)
        self.name = name

    def __str__(self):
        return f"Antenna: [{self.name}] at ({self.row},{self.col})"

    def antinodes_at(self, other, harmonics=False):
        r1, c1 = self.row, self.col
        r2, c2 = other.row, other.col
        dr, dc = abs(r2 - r1), abs(c2 - c1)
        sr, sc = int((r2 - r1) / dr), int((c2 - c1) / dc)  # Signs; ensure they are integers (-1,+1)

        # Outputs
        if not harmonics:
            r3, c3 = r1 - sr * dr, c1 - sc * dc
            r4, c4 = r1 + 2 * sr * dr, c1 + 2 * sc * dc

            return r3, c3, r4, c4
        else:
            ret = []
            max_harm = 100
            for i in range(max_harm):
                hr = r1 - (i - 1) * sr * dr
                hc = c1 - (i - 1) * sc * dc
                ret.append((hr, hc))

            for i in range(max_harm):
                hr = r1 + (i + 2) * sr * dr
                hc = c1 + (i + 2) * sc * dc
                ret.append((hr, hc))

            return ret

class AntiNode:
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def __str__(self):
        return f"Antinode: ({self.row},{self.col})"

    def __eq__(self, other):
        if not isinstance(other, AntiNode):
            return False
        return self.row == other.row and self.col == other.col


class MapManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            return super().__new__(cls)
        else:
            return cls._instance

    def __init__(self, rowmax, colmax):
        # Assuming that we actually call (create this class) this once in our code,
        # so not fretting about double initialization
        self.ante_hash = {}
        self.anti_list = []
        self.ROW = rowmax
        self.COL = colmax
        print(f"Created Map Manager with {self.ROW} rows and {self.COL} columns.")

    def add_antenna(self, ante):
        if ante.name not in self.ante_hash.keys():
            self.ante_hash[ante.name] = []

        self.ante_hash[ante.name].append(ante)

    def add_antinode(self, anti):
        if anti.row > self.ROW or anti.col > self.COL or anti.row < 1 or anti.col < 1:
            print(f"Rejecting AntiNode because if is out of bounds at [{anti.row},{anti.col}]")
        else:
            if not anti in self.anti_list:
                self.anti_list.append(anti)

    def get_antenna_list(self):
        ret = []
        for _, vector in self.ante_hash.items():
            for v in vector:
                ret.append(v)

        return ret

    def get_antinode_list(self):
        ret = sorted(self.anti_list, key=lambda x: (x.row, x.col))
        return ret

    def count_antennas(self):
        return len(self.get_antenna_list())

    def count_antinodes(self):
        return len(self.anti_list)

    def subset_antennas(self, name):
        ret = self.ante_hash[name]
        return ret

    def get_antenna_names(self):
        return list(self.ante_hash.keys())


test_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
if __name__ == "__main__":
    input_data = test_data.split()
    input_data = fetch_aoc_input(8, 2024)
    rowmax = len(input_data)
    colmax = len(input_data[0])  # assuming all rows have equal columns
    mmgr = MapManager(rowmax, colmax)

    for idx, r in enumerate(input_data):
        print(f"{idx + 1:3d}:{r}")
        for i, c in enumerate(r):
            col = i + 1
            row = idx + 1
            if re.match(r"[a-zA-Z0-9]", c):
                antenna = Antenna(row, col, c)
                mmgr.add_antenna(antenna)

    [print(a) for a in mmgr.get_antenna_list()]

    print(f"{mmgr.count_antennas()} antennas installed")
    a_names = mmgr.get_antenna_names()
    for name in a_names:
        antes = mmgr.subset_antennas(name)

        print()
        for combo in itertools.combinations(antes, 2):
            a, b = combo
            print(f"{a} paired with {b}")
            harmonics = True # or False
            anti_vec = a.antinodes_at(b,harmonics)
            for r,c in anti_vec:
                anti = AntiNode(r,c)
                mmgr.add_antinode(anti)

    print(f"{mmgr.count_antinodes()} antinodes added.")
    # for anti in mmgr.get_antinode_list():
    #     print(f"{anti}")
