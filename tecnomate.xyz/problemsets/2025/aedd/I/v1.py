def main() -> None:
    participants = int(input())

    first = ""
    second = ""
    third = ""

    max_age = -1
    oldest_participant = ""

    for _ in range(participants):
        name, age, position = input().split()

        match position:
            case "1":
                first = name
            case "2":
                second = name
            case "3":
                third = name

        if int(age) > max_age:
            max_age = int(age)
            oldest_participant = name

    print(1, first)
    print(2, second)
    print(3, third)
    print()
    print("Mencion Veterano:", oldest_participant)


if __name__ == "__main__":
    main()
