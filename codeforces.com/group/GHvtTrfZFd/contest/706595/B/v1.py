def distinct_points(figures: list[int]) -> int:
    answer = 0
    i = 0

    while i < len(figures) - 1:
        current_figure = figures[i]
        next_figure = figures[i + 1]

        match current_figure:
            case 1:  # circle
                match next_figure:
                    case 2:  # triangle in circle
                        answer += 3
                    case 3:  # square in circle
                        answer += 4
            case 2:  # triangle
                match next_figure:
                    case 1:  # circle in triangle
                        answer += 3
                    case 3:  # square in triangle
                        return -1
            case 3:  # square
                match next_figure:
                    case 1:  # circle in square
                        answer += 4

                        if (
                            i + 2 < len(figures) and figures[i + 2] == 2
                        ):  # triangle in circle in square
                            answer -= 1

                    case 2:  # triangle in square
                        return -1

        i += 1

    return answer


def main() -> None:
    _ = input()
    figures = list(map(int, input().split()))

    answer = distinct_points(figures)

    if answer == -1:
        print("Infinite")
    else:
        print("Finite")
        print(answer)


if __name__ == "__main__":
    main()
