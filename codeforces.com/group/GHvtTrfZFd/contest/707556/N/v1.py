def solve(chars: list[str]) -> str:
    first = chars[0]
    minchar = min(chars[1:])

    if first < minchar:
        return "".join(chars)

    for i in range(len(chars) - 1, 0, -1):
        if chars[i] == minchar:
            chars.pop(i)
            break

    return minchar + "".join(chars)


def main() -> None:
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        _ = input()
        chars = list(input())

        answers.append("".join(chars) if len(chars) == 1 else solve(chars))

    print("\n".join(answers))


if __name__ == "__main__":
    main()
