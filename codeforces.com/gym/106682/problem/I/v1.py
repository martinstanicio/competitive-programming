def main() -> None:
    players, rounds = map(int, input().split())

    print("S" if rounds == 1 or (players == 2 and rounds % 2 != 0) else "N")


if __name__ == "__main__":
    main()
