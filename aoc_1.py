from aoc_utils import fetch_aoc_input


def main():
    print("Hola 2025 Advent of Code")
    input_data = None

    # Fetch input for Day 1 of 2024
    try:
        day = 1
        year = 2024
        input_lines = fetch_aoc_input(day, year)
    except Exception as e:
        print(e)

    col1 = []
    col2 = []

    for line in input_lines:
        print("Line: ", line)
        x, y = map(int, line.split())
        col1.append(x)
        col2.append(y)

    col1 = sorted(col1)
    col2 = sorted(col2)

    print("Length col1 = ", len(col1))
    print("Length col2 = ", len(col2))

    print(col1)
    print(col2)

    sumd = 0
    for i in range(len(col1)):
        d = abs(col1[i] - col2[i])
        sumd += d
        print(f"{i} : [{col1[i]},{col2[i]}] ==> {d}, Sumd = {sumd}")

    # col1 = [3,4,2,1,3,3]
    # col2 = [4,3,5,3,9,3]
    similarity = 0
    for num1 in col1:
        w = 0
        for num2 in col2:
            if num1 == num2:
                w += 1
        similarity += num1 * w

    print("Sum of distance = ", sumd)
    print("Similarity = ", similarity)


if __name__ == "__main__":
    main()
