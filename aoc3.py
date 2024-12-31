import re

from aoc_utils import fetch_aoc_input


def part_1(input):
    # print(input)
    # print(len(input))

    regex = "mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, input)
    # print("Matches =",len(matches))
    sum = 0
    for i in matches:
        regex = "\d{1,3}"
        [x, y] = re.findall(regex, i)
        ans = int(x) * int(y)
        sum += ans
        print(f"{i}={ans}", end=" ")

    # print(f"\n{sum=}")
    return sum


def part_2(input):
    memory = f"do(){input}don't()"
    print(f"{memory=}")
    active = re.findall(r"do\(\).+?don\'t\(\)", memory, re.DOTALL)
    print(f"{active=}")
    sum = 0
    for a in active:
        s = part_1(a)
        sum += s
        print(f"\n>>{a=}\nSum={s}\n")
    print(f"Final Part 2 {sum=}")


if __name__ == "__main__":
    input = fetch_aoc_input(3, 2024, raw_string=True)
    # input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    sum = part_1(input)
    print("\n***Part 1 sum = ", sum)
    part_2(input)
