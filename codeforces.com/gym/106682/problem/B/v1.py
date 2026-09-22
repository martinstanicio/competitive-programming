def main() -> None:
    string = input()

    left = 0
    right = 5
    found = set()

    while right <= len(string):
        if (
            string[left] in "AEIOU"
            and string[left] == string[right - 1]
            and string[left + 1 : right - 1] == "GAS"
        ):
            found.add(string[: left + 1] + string[right:])

        left += 1
        right += 1

    if len(found) == 0:
        print("-")
    elif len(found) > 1:
        print("+")
    else:
        print(found.pop())


if __name__ == "__main__":
    main()
