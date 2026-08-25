def main() -> None:
    price, bill, candy = map(int, input().split())
    answer = "S" if (bill - price) % candy == 0 else "N"

    print(answer)


if __name__ == "__main__":
    main()
