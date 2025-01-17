from aoc_utils import fetch_aoc_input

memory={}
def stonecount(s, blink):
    global memory
    ls = len(str(s))

    if blink == 0:
        return 1

    if (s,blink) in memory:
        return memory[(s,blink)]

    if s == 0:
        retval = stonecount(1, blink - 1)
    elif ls % 2 == 0:
        s1 = str(s)
        mid = int(ls / 2)
        d1 = int(s1[0:mid])
        d2 = int(s1[mid:])
        retval = stonecount(d1,blink-1) + stonecount(d2,blink-1)
    else:
        retval = stonecount(s * 2024, blink-1)

    # Push into memory
    memory[(s,blink)] = retval
    return retval


def main():
    input_data=fetch_aoc_input(11,2024)
    print(input_data)
    stones = [int(i) for i in input_data[0].split()]
    print(stones)

    count = 0
    blink = 75    # 25, 75 etc
    for node in stones:
        count = count + stonecount(node,blink)

    print (f"Stones after {blink} blinks = {count}")


if __name__ == "__main__":
    main()
