from itertools import permutations
from math import inf


def main() -> None:
    lamps = int(input())
    garland = input()
    answer = inf
    perms = permutations("RGB")

    for p in perms:
        changes = 0

        for i, c in enumerate(garland):
            if p[i % 3] != c:
                changes += 1

        if changes < answer:
            answer = changes
            d, m = divmod(lamps, 3)
            chain = p * d + p[:m]

    print(answer)
    print("".join(str(c) for c in chain))


if __name__ == "__main__":
    main()
