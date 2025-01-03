from aoc_utils import fetch_aoc_input


def solve(input):
    rules, updates = parse_rules_and_updates(input)

    def isgoodupdate(u):
        for idx, i in enumerate(u):
            for j in u[idx + 1 :]:
                s = f"{i}|{j}"
                if s not in rules:
                    return False

        return True

    sum_mid = 0
    bad_updates = []
    for u in updates:
        # print(f"Processing update : {u}")
        if isgoodupdate(u):
            mid_idx = int((len(u) - 1) / 2)
            # print(f"{u=},{len(u)=},{mid_idx=}")
            mid = int(u[mid_idx])
            sum_mid += mid
        else:
            bad_updates.append(u)

    print(f"Sum of Good update mids = {sum_mid}")

    # For a given update vector u, start with the first element u[0] = k
    # if all the elements to the right of k falls in the after_set of k, then pop k and append to a new vector (cirrected)
    # if this condition is not met, then move k one slot to the right until this condition is met
    # then start with the first element again (a new k)

    def good_from_index(idx, u):
        if idx == len(u) - 1:
            return True
        # The element being compared is at index idx
        # if all elements to the right of idx falls in the after_set of u[idx], return true
        for k in u[idx + 1 :]:
            s = f"{u[idx]}|{k}"
            if s not in rules:
                # print (f"{s} is not in rules !")
                return False
        return True

    print("Processing bad updates")
    corrected_updates = []
    for u in bad_updates:
        corrected = []
        while u:
            if good_from_index(0, u):
                corrected.append(u.pop(0))
            else:
                idx = 0
                while not good_from_index(idx, u):
                    # print(u)
                    u.insert(idx + 1, u.pop(idx))  # move the element one to the right
                    idx += 1

        # print ("Corrected = ", corrected)
        corrected_updates.append(corrected)

    sum_corr_mid = 0
    for u in corrected_updates:
        mid_idx = int((len(u) - 1) / 2)
        # print(f"{u=},{len(u)=},{mid_idx=}")
        mid = int(u[mid_idx])
        sum_corr_mid += mid

    print(f"Sum of mids in corrected updates = {sum_corr_mid}")


def parse_rules_and_updates(input):
    rules = []
    updates = []
    for line in input:
        if "|" in line:
            rules.append(line)

        if "," in line:
            u = line.split(",")
            updates.append(u)

    # for idx, r in enumerate(rules):
    #     print(f"{idx}:{r}")
    # for idx, u in enumerate(updates):
    #     print(f"{idx}:{u}")

    return rules, updates


if __name__ == "__main__":
    trial_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    trial_input = trial_input.split()
    input = trial_input
    input = fetch_aoc_input(5, 2024)
    solve(input)
