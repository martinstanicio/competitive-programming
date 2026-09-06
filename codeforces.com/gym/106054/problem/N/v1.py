import sys

input = sys.stdin.readline
print = sys.stdout.write

MINN = 1
MAXN = 10**8


def main() -> None:
    trees = int(input())

    minx = miny = MAXN
    maxx = maxy = MINN

    for _ in range(trees):
        x, y = map(int, input().split())

        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)

    perimeter = 2 * (maxx - minx + 2) + 2 * (maxy - miny + 2)

    print(str(perimeter) + "\n")


if __name__ == "__main__":
    main()
