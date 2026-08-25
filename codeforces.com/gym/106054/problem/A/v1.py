def solve(string: str) -> bool:
    tap = [False] * 3

    for char in string:
        if not tap[0]:
            if char == "T":
                tap[0] = True
            else:
                continue

        if not tap[1]:
            if char == "A":
                tap[1] = True
            else:
                continue

        if not tap[2]:
            if char == "P":
                return True
            else:
                continue

    return False


def main() -> None:
    string = input()
    answer = "S" if solve(string) else "N"

    print(answer)


if __name__ == "__main__":
    main()
