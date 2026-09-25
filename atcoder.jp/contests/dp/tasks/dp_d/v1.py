def main() -> None:
    items, capacity = map(int, input().split())
    weights = []
    values = []

    for _ in range(items):
        w, v = map(int, input().split())

        weights.append(w)
        values.append(v)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]

    for i in range(1, items + 1):
        for x in range(capacity + 1):
            if x >= weights[i - 1]:
                dp[i][x] = max(
                    dp[i - 1][x],
                    dp[i - 1][x - weights[i - 1]] + values[i - 1],
                )
            else:
                dp[i][x] = dp[i - 1][x]

    answer = dp[items][capacity]

    print(answer)


if __name__ == "__main__":
    main()
