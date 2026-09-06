import sys

input = sys.stdin.readline
print = sys.stdout.write


def main() -> None:
    partners, rounds = map(int, input().split())
    gold = [0] * (partners + 1)

    for _ in range(rounds):
        x, y = map(int, input().split())
        choices = list(map(int, input().split()))

        sharing = choices.count(1)

        if y > x // (sharing + 1):
            choices.append(2)
        else:
            choices.append(1)
            sharing += 1

        for i, c in enumerate(choices):
            gold[i] += y if c == 2 else x // sharing

    print(" ".join(str(x) for x in gold) + "\n")


if __name__ == "__main__":
    main()
