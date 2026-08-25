def main() -> None:
    _, team_size = map(int, input().split())
    ratings = list(map(int, input().split()))

    unique_ratings = set(ratings)

    if len(unique_ratings) < team_size:
        print("NO")
        return

    selected_students: list[int] = []
    existing_ratings: list[int] = []

    for i, rating in enumerate(ratings):
        if len(selected_students) >= team_size:
            break

        if rating in existing_ratings:
            continue

        selected_students.append(i + 1)
        existing_ratings.append(rating)

    print("YES")
    print(" ".join(map(str, selected_students)))


if __name__ == "__main__":
    main()
