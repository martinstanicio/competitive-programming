import sys

SWAMP = "w"
GRASS = '"'


def main() -> None:
    n = int(input())
    line = input()

    dp = [0] + [-1] * (n - 1)

    for i in range(1, n):
        if line[i] == SWAMP:
            continue

        options = []

        for steps in (1, 3, 5):
            if i >= steps and dp[i - steps] != -1:
                options.append(dp[i - steps])

        if options:
            dp[i] = (1 if line[i] == GRASS else 0) + max(options)

    answer = dp[n - 1]

    print(answer)


if __name__ == "__main__":
    with open("lepus.in", "r") as sys.stdin, open("lepus.out", "w") as sys.stdout:
        main()
