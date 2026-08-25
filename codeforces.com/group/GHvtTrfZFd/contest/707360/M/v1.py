def main() -> None:
    test_cases = int(input())
    answers: list[int] = []

    for _ in range(test_cases):
        n, k = map(int, input().split())
        d, m = divmod(k, n - 1)

        answer = d * n + m

        if m == 0:
            answer -= 1

        answers.append(answer)

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
