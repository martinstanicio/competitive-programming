def solve(worms: list[int]) -> tuple[bool, list[int]]:
    n = len(worms)
    iworms = sorted((w, i) for i, w in enumerate(worms))

    for target, i in iworms[::-1]:
        left = 0
        right = n - 1

        while left != right:
            if iworms[left][1] == i:
                left += 1
                continue

            if iworms[right][1] == i:
                right -= 1
                continue

            total = iworms[left][0] + iworms[right][0]

            if total == target:
                j = iworms[left][1]
                k = iworms[right][1]

                return (True, [i, j, k])

            if total > target:
                right -= 1

            if total < target:
                left += 1

    return (False, [])


def main() -> None:
    _ = input()
    worms = list(map(int, input().split()))

    success, indexes = solve(worms)

    if success:
        print(" ".join(str(i + 1) for i in indexes))
    else:
        print(-1)


if __name__ == "__main__":
    main()
