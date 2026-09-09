from math import isqrt, sqrt


def solve(numbers: list[int]) -> str:
    numbers = sorted(numbers)

    if len(numbers) == 1:
        return "*" if numbers[0] == 1 else f"{numbers[0]} 1"

    if sqrt(numbers[-1]).is_integer() and isqrt(numbers[-1]) not in numbers:
        return f"{numbers[-1]} {isqrt(numbers[-1])}"

    candidates = [
        numbers[-1],
        numbers[1] * numbers[-1],
    ]

    for c in candidates:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            p = numbers[left] * numbers[right]

            if p == c:
                left += 1
                right -= 1
            elif p < c and c % numbers[left] == 0:
                return f"{c} {c // numbers[left]}"
            elif p > c and c % numbers[right] == 0:
                return f"{c} {c // numbers[right]}"
            else:
                break

    return "*"


def main() -> None:
    _ = input()
    numbers = list(map(int, input().split()))
    answer = solve(numbers)

    print(answer)


if __name__ == "__main__":
    main()
