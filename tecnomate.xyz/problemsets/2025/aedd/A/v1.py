from math import gcd


def main() -> None:
    a, b, g = map(int, input().split())

    answer = round(1 / gcd(a, b, g), 2)

    print(f"Minutos Transcurridos: {answer}")


if __name__ == "__main__":
    main()
