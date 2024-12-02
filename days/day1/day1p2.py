from days.day1.day1p1 import q_input, build_l_r

test_input: str = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""


def get_sim_score(integer: int, list_integers: list[int]) -> int:
    integer_count: int = list_integers.count(integer)
    sim_score: int = integer_count * integer
    return sim_score


def main() -> None:
    total_sim_score: int = 0
    # build the two lists, from day1
    left, right = build_l_r(q_input)
    # left, right = build_l_r(test_input)

    # for i in left:
    #     total_sim_score += get_sim_score(i, right)
    total_sim_score += sum([get_sim_score(i, right) for i in left])

    print(total_sim_score)


if __name__ == "__main__":
    main()
