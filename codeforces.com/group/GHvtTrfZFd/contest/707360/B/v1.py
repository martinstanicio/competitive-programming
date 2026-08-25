def main() -> None:
    test_cases = int(input())
    answers: list[int] = []

    for _ in range(test_cases):
        _ = int(input())
        candies = list(map(int, input().split()))
        oranges = list(map(int, input().split()))
        movements = 0

        min_candies = min(candies)
        min_oranges = min(oranges)

        for c, o in zip(candies, oranges):
            common = min(c - min_candies, o - min_oranges)
            c -= common
            o -= common
            movements += common

            extra_candies = c - min_candies
            c -= extra_candies
            movements += extra_candies

            extra_oranges = o - min_oranges
            o -= extra_oranges
            movements += extra_oranges

        answers.append(movements)

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
