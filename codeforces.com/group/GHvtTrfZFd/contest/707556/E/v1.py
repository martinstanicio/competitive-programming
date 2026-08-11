def main() -> None:
    _ = input()
    boys = sorted(map(int, input().split()))
    _ = input()
    girls = sorted(map(int, input().split()))

    pairs = 0
    b = 0
    g = 0

    while b < len(boys):
        while g < len(girls):
            if boys[b] + 1 < girls[g]:
                break
            elif boys[b] - 1 > girls[g]:
                g += 1
            else:
                pairs += 1
                g += 1
                break

        b += 1

    print(pairs)


if __name__ == "__main__":
    main()
