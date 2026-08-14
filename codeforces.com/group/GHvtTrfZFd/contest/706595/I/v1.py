import sys

input = sys.stdin.readline
print = sys.stdout.write


def main() -> None:
    n = int(input())
    coders = 0
    lines = []

    for i in range(n):
        line = []

        for j in range(n):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                coders += 1
                line.append("C")
            else:
                line.append(".")

        lines.append("".join(line))

    print(f"{coders}\n")
    print("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
