"""Binary search algorithm
    Args:
        values: unsorted list
        target: value to find
    Returns:
        mid: index of value
"""


def search(values, target):
    values = sorted(values)
    min = 0
    max = len(values) - 1
    while min <= max:
        mid = (min + max) // 2
        if target < values[mid]:
            max = mid - 1
        elif target > values[mid]:
            min = mid + 1
        else:
            return mid
    return
