from typing import Callable
from day2p1 import multiline_str_to_list, p_input


def check_diff(seq: list[int]) -> bool:
    acceptable_diffs: list[int] = list(range(1, 4))
    diff_list: list[int] = list(set([y - x for x, y in zip(seq[0::], seq[1::])]))
    diff_list.sort()
    # for i in range(len(seq) - 1):
    #     diff: int = abs(seq[i] - seq[i + 1])
    #     if diff in acceptable_diffs:
    #         continue
    #     else:
    #         safe_diff = False
    #         break
    return diff_list == acceptable_diffs


def check_order(seq: list[int]) -> bool:
    return seq == sorted(seq) or seq == sorted(seq, reverse=True)


def check_safety_damp(seq: list[int]) -> tuple[bool, ...]:
    safe_order = check_order(seq)
    safe_diff = check_diff(seq)
    retry_list: list[int] = seq.copy()

    if not safe_diff:
        safe_diff = restest_list(check_diff, retry_list)

    if not safe_order:
        safe_order = restest_list(check_order, retry_list)

    return safe_order, safe_diff


def restest_list(func: Callable[[list[int]], bool], seq: list[int]) -> bool:
    for i, _ in enumerate(seq):
        test_list = seq.copy()
        _ = test_list.pop(i)
        new_res = func(test_list)
        if not new_res:
            continue
        else:
            return True
    return False


def main() -> None:
    test: str = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    lists_input: list[list[int]] = multiline_str_to_list(test)

    safe_reports: int = 0
    good = []
    for sequence in lists_input:
        safe_order, safe_diff = check_safety_damp(sequence)
        # if safe_order and safe_diff:
        #     safe_reports += 1 if safe_order and safe_diff else 0
        if safe_diff and safe_order:
            good.append(sequence)
        safe_reports += 1 if safe_order and safe_diff else 0

    print(f"Counted {safe_reports} in the input.")
    print(*good, sep="\n")
    print(list(range(1, 4)))


if __name__ == "__main__":
    main()
