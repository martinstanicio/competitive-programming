from collections.abc import Callable


def binary_search_monotonic[T](l: list[T], f: Callable[[T], bool]) -> int:  # O(log n)
    """
    Find the index of the first element in sorted list `l` that satisfies the monotonic predicate `f`, or `-1` if no such element exists.
    """
    low = 0
    high = len(l) - 1
    index = -1

    while low <= high:
        mid = low + (high - low) // 2

        if f(l[mid]):
            index = mid
            high = mid - 1
        else:
            low = mid + 1

    return index
