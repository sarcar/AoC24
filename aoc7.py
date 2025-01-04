from aoc_utils import fetch_aoc_input
import itertools

test_data = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""



def eval(v):
    ans = v.pop(0)
    while v:
        oper = v.pop(0)
        op2 = v.pop(0)
        if oper == "*":
            ans *= op2
        if oper == "+":
            ans += op2
        if oper == "||":
            ans = int(str(ans)+str(op2))

    return ans


if __name__ == "__main__":
    #test_data=test_data.split("\n")[1:-1] # discard the first and last empty
    #input_data = test_data
    input_data = fetch_aoc_input(7, 2024)
    print(input_data)
    calibration = 0
    for e in input_data:
        ans, operands = e.split(":")
        ans = int(ans)
        operands =  [int(k) for k in operands.strip().split(" ")]

        slots = len(operands) - 1
        print(f"{ans} = {operands} {slots=}")

        operator_set = ["+","*","||"]
        for s_oper in itertools.product(operator_set,repeat=slots):
            s_oper = list(s_oper)
            ops = operands.copy()
            lhs = []
            while ops:
                lhs.append(ops.pop(0))
                if s_oper:
                    lhs.append(s_oper.pop(0))

            print (lhs)
            k = eval(lhs)
            print ("Answer = ", k)

            if k == ans:
                calibration += k
                break

        print (f"Calibration = {calibration}")

