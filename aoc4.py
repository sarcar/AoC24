from pipenv.cli.options import pass_state

from aoc_utils import fetch_aoc_input


def main():
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
XMASAMXMAS"""
    input = input.split()
    input = fetch_aoc_input(4, 2024)
    for r in input:
        print(r)
    part_1(input)


def part_1(input):
    lengths = [len(r) for r in input]
    n_rows = len(lengths)
    n_cols = lengths[0]

    def isXMAS_new(vec):
        l = len(vec)
        w = ""
        for i in range(l):
            row, col = vec[i]
            if row >= n_rows or col >= n_cols or row < 0 or col < 0:
                return False
            w += input[row][col]

        return True if w == "XMAS" else False

    count_XMAS = 0
    for row in range(n_rows):
        for col in range(n_cols):
            key = "E"
            vec = [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "W"
            vec = [(row, col), (row, col - 1), (row, col - 2), (row, col - 3)]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "N"
            vec = [(row, col), (row - 1, col), (row - 2, col), (row - 3, col)]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "S"
            vec = [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "NE"
            vec = [
                (row, col),
                (row - 1, col + 1),
                (row - 2, col + 2),
                (row - 3, col + 3),
            ]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "SE"
            vec = [
                (row, col),
                (row + 1, col + 1),
                (row + 2, col + 2),
                (row + 3, col + 3),
            ]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "SW"
            vec = [
                (row, col),
                (row + 1, col - 1),
                (row + 2, col - 2),
                (row + 3, col - 3),
            ]
            if isXMAS_new(vec):
                count_XMAS += 1

            key = "NW"
            vec = [
                (row, col),
                (row - 1, col - 1),
                (row - 2, col - 2),
                (row - 3, col - 3),
            ]
            if isXMAS_new(vec):
                count_XMAS += 1

    print(f"Final XMAS count = {count_XMAS}")


if __name__ == "__main__":
    main()
