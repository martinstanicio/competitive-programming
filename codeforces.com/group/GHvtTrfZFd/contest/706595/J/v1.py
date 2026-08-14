def solve(heights: list[int]) -> int:
    return 0 if sum(heights) % len(heights) == 0 else 1


def main() -> None:
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        _ = input()
        heights = list(map(int, input().split()))

        answers.append(solve(heights))

    print("\n".join(str(a) for a in answers))


if __name__ == "__main__":
    main()
