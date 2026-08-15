def binary_search(l: list[float], x: float) -> int:  # O(log n)
    """
    Find the index of element `x` in sorted list `l`, or `-1` if not found.
    """
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if l[mid] == x:
            return mid
        elif l[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1
