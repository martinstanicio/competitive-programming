def solve(rectangles: int) -> bool:
    heights: list[int] = [0] * rectangles

    for i in range(rectangles):
        w, h = map(int, input().split())

        maxh = max(w, h)
        minh = min(w, h)

        if i == 0 or maxh <= heights[i - 1]:
            heights[i] = maxh
        elif minh <= heights[i - 1]:
            heights[i] = minh
        else:
            return False

    return True


def main() -> None:
    rectangles = int(input())

    success = solve(rectangles)

    print("YES" if success else "NO")


if __name__ == "__main__":
    main()
