from virtualenv.config.convert import NoneType

from aoc_utils import fetch_aoc_input


input_lines = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
input_lines = input_lines.split("\n")


def main():
    input_lines = fetch_aoc_input(2, 2024)

    safe_without_dampener = process_report(input_lines, dampener=False)
    safe_with_dampener = process_report(input_lines, dampener=True)

    print(f"{safe_without_dampener=} : {safe_with_dampener=}")


def check_level_safety(levels):
    gaps = [b - a for a, b in zip(levels, levels[1:])]

    if len(levels) < 2:
        print("Report has fewer than 2 levels. Cannot proceed.")
        exit()

    direction = -1 if gaps[0] < 1 else +1

    for g in gaps:
        if abs(g) > 3 or abs(g) == 0 or (direction > 0 and g < 0) or (direction < 0 and g > 0):
            return False
    return True


def process_report(input_lines, dampener):
    total_safe = 0
    for line, report in enumerate(input_lines):
        levels = [int(x) for x in report.split()]
        safe_vector = []
        safe = check_level_safety(levels)
        safe_vector.append(safe)
        if dampener:
            for i in range(len(levels)):
                new_level = levels.copy()
                del new_level[i]
                safe = check_level_safety(new_level)
                safe_vector.append(safe)

        if any(safe_vector):
            total_safe += 1

        # DEBUG
        # print (f"{line=} : {levels=} : {safe_vector=} : {total_safe=}")

    return total_safe


if __name__ == "__main__":
    main()
