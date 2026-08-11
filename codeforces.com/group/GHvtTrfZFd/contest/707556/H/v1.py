def main() -> None:
    _ = input()
    sequence = map(int, input().split())
    answer = sum(abs(x) for x in sequence)

    print(answer)


if __name__ == "__main__":
    main()
