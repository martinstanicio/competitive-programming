def main() -> None:
    n = int(input())
    numbers = sorted(map(int, input().split()))
    answer = numbers[(n - 1) // 2]

    print(answer)


if __name__ == "__main__":
    main()
