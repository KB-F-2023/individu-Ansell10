from itertools import product

colors = ["Red", "Blue", "Green"]
states = ["SA", "WA", "NT", "Q", "NSW", "V", "T"]
neighbors = {}
neighbors["WA"] = ["NT", "SA"]
neighbors["NT"] = ["WA", "SA", "Q"]
neighbors["SA"] = ["WA", "NT", "Q", "NSW", "V"]
neighbors["Q"] = ["NT", "SA", "NSW"]
neighbors["NSW"] = ["Q", "SA", "V"]
neighbors["V"] = ["SA", "NSW"]
neighbors["T"] = []


def get_all_ans() -> list:
    all_solve = []
    solve = {}
    for color in product(colors, repeat=7):
        for i, c in enumerate(color):
            solve[states[i]] = c
        all_solve.append(solve)
        solve = {}
    print(f"There is {len(all_solve)}  solves in this question")
    return all_solve


def delete_invalid_ans(all_solve: list):
    is_ans = True
    ans_fit_rule = []
    for ans in all_solve:
        for state in ans.keys():
            for neighbor in neighbors.get(state):
                if ans.get(neighbor) == ans.get(state):
                    is_ans = False
                    break
        if is_ans:
            print(ans)
            ans_fit_rule.append(ans)
        is_ans = True
    return ans_fit_rule


def main():
    print(f"{len(delete_invalid_ans(get_all_ans()))}")


main()