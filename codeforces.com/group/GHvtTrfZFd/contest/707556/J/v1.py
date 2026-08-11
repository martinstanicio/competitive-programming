def main() -> None:
    sellers, money = map(int, input().split())
    affordable = []

    for i in range(sellers):
        _, *prices = map(int, input().split())

        if any(price < money for price in prices):
            affordable.append(i + 1)

    print(len(affordable))
    print(" ".join(str(i) for i in affordable))


if __name__ == "__main__":
    main()
