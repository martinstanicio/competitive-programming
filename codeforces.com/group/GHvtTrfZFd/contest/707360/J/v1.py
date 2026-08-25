def main() -> None:
    test_cases = int(input())
    answers: list[int] = []

    for _ in range(test_cases):
        n = int(input())

        if n < 10:
            answers.append(n)
            continue

        l = len(str(n))

        answer = 9 * (l - 1)

        for _ in range(10 ** (l - 1) + int("1" * (l - 1)), n + 1, int("1" * l)):
            answer += 1

        answers.append(answer)

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
