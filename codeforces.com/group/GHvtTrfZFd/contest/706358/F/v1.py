from copy import copy


def is_valid_hash(password: str, hash: str) -> bool:
    char_count: dict[str, int] = {}

    for char in password:
        if char not in char_count:
            char_count[char] = 0

        char_count[char] += 1

    char_count_copy = copy(char_count)
    char_count_was_modified = False
    last_position_char_count_was_modified: int
    i = 0
    while i < len(hash):
        if char_count_copy.get(hash[i], 0):
            char_count_copy[hash[i]] -= 1

            if not char_count_was_modified:
                char_count_was_modified = True
                last_position_char_count_was_modified = i

            i += 1
            continue

        if all(char_count_copy[char] == 0 for char in char_count_copy):
            return True

        if char_count_was_modified:
            i = last_position_char_count_was_modified + 1
            char_count_copy = copy(char_count)
            char_count_was_modified = False
            continue

        i += 1

    return all(char_count_copy[char] == 0 for char in char_count_copy)


def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        password = input()
        hash = input()
        answer = "YES" if is_valid_hash(password, hash) else "NO"

        print(answer)


if __name__ == "__main__":
    main()
