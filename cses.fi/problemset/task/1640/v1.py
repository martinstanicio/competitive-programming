def solve(numbers: list[int], target: int) -> tuple[bool, list[int]]:
    _numbers = sorted((n, i) for i, n in enumerate(numbers))

    low = 0
    high = len(numbers) - 1

    while low < high:
        result = _numbers[low][0] + _numbers[high][0]

        if result == target:
            return (True, [_numbers[low][1], _numbers[high][1]])
        elif result < target:
            low += 1
        else:
            high -= 1

    return (False, [])


def main() -> None:
    _, target = map(int, input().split())
    numbers = list(map(int, input().split()))

    success, indexes = solve(numbers, target)

    print(" ".join(str(i + 1) for i in indexes) if success else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
