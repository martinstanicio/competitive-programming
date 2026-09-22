def main() -> None:
    _ = input()
    dials = map(int, input().split())

    unscramble = {
        0: 0,
        1: 5,
        2: 1,
        3: 6,
        4: 2,
        5: 7,
        6: 3,
        7: 8,
        8: 4,
    }

    answer = [unscramble[x] for x in dials]

    print(" ".join(str(x) for x in answer))


if __name__ == "__main__":
    main()
