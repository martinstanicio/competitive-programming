def solve(heights: list[int]) -> bool:
    blocks = len(heights)

    if blocks == 1:
        return True

    for i, h in enumerate(heights):
        if h - i < 0:
            return False

        if i < blocks - 1:
            heights[i + 1] += h - i

    return True


def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        _ = int(input())
        heights = list(map(int, input().split()))

        success = solve(heights)
        print("YES" if success else "NO")


if __name__ == "__main__":
    main()
