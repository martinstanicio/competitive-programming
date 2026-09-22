FIVE_HOURS_IN_SECONDS = 5 * 60 * 60


def main() -> None:
    h, m, s = map(int, input().split())
    seconds = s + m * 60 + h * 60 * 60

    if seconds > FIVE_HOURS_IN_SECONDS / 2:
        print("+")
    elif seconds < FIVE_HOURS_IN_SECONDS / 2:
        print("-")
    else:
        print("=")


if __name__ == "__main__":
    main()
