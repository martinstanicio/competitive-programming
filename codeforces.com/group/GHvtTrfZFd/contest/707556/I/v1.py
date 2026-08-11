def main() -> None:
    visits_remaining = int(input()) - 1
    rabbit_owl = int(input())
    rabbit_eeyore = int(input())
    owl_eeyore = int(input())

    answer = 0

    if visits_remaining == 0:
        print(answer)
        return

    answer += min(rabbit_owl, rabbit_eeyore)
    visits_remaining -= 1

    if visits_remaining > 0:
        answer += min(rabbit_owl, rabbit_eeyore, owl_eeyore) * visits_remaining

    print(answer)


if __name__ == "__main__":
    main()
