from itertools import pairwise


def solve(watered_on_day: list[int]) -> int:
    height = 1

    if watered_on_day[0]:
        height += 1

    for yesterday, today in pairwise(watered_on_day):
        if not yesterday and not today:
            return -1

        if yesterday and today:
            height += 5
        elif today:
            height += 1

    return height


def main() -> None:
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        _ = input()
        watered_on_day = list(map(int, input().split()))

        answers.append(solve(watered_on_day))

    print("\n".join(str(a) for a in answers) + "\n")


if __name__ == "__main__":
    main()
