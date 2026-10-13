def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        students, pizzas, minutes = map(float, input().split())
        target_students, target_hours = map(float, input().split())
        target_minutes = target_hours * 60

        pizzas_per_student_per_minute = pizzas / students / minutes

        answer = pizzas_per_student_per_minute * target_students * target_minutes

        print(round(answer, 2))


if __name__ == "__main__":
    main()
