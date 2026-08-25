def main() -> None:
    string = input()
    turnovers = 0

    for s in string:
        if s in "aeiou13579":
            turnovers += 1

    print(turnovers)


if __name__ == "__main__":
    main()
