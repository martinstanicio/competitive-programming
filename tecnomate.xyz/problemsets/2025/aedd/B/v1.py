MAXN = 44  # fib(45) > 10 ** 9


def bsearch(target: int, array: list[int]) -> int:
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2

        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


def main() -> None:
    size = max(map(int, input().split()))
    fib = [1] * (MAXN + 1)

    for i in range(2, MAXN + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    answer = bsearch(size, fib)

    print(answer)


if __name__ == "__main__":
    main()
