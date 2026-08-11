from sys import stdout


def solve() -> str:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    divisors = []

    for prime in primes:
        print(prime)
        stdout.flush()

        is_divisor = input() == "yes"

        if is_divisor:
            divisors.append(prime)

        if len(divisors) == 2:
            return "composite"

    if len(divisors) == 0:
        return "prime"

    divisor = divisors[0]

    if divisor**2 <= 100:
        print(divisor**2)
        stdout.flush()

        is_divisor = input() == "yes"

        if is_divisor:
            return "composite"

    return "prime"


def main() -> None:
    answer = solve()

    print(answer)


if __name__ == "__main__":
    main()
