def solve(bits: int, n: int) -> str:
    if n >= bits * 2:
        return "Nro no valido"

    if n <= bits:
        return "0" * (bits - n) + "1" * n

    return "1" * (2 * bits - n) + "0" * (n - bits)


def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        bits, n = map(int, input().split())

        answer = solve(bits, n)

        print(answer)


if __name__ == "__main__":
    main()
