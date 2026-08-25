def main() -> None:
    ROOMS = 10

    _ = input()
    events = input()
    assignment = [0] * ROOMS

    for event in events:
        match event:
            case "L":
                for i in range(ROOMS):
                    if assignment[i] == 0:
                        assignment[i] = 1
                        break
            case "R":
                for i in range(ROOMS - 1, 0 - 1, -1):
                    if assignment[i] == 0:
                        assignment[i] = 1
                        break
            case _:
                room = int(event)
                assignment[room] = 0

    answer = "".join(map(str, assignment))

    print(answer)


if __name__ == "__main__":
    main()
