"""Magic Index."""


def magic(arr, start=0):
    """Define function."""
    mid = len(arr)//2
    while mid != start:
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            mid = mid // 2
            continue
        start = mid
        mid += mid // 2
    return -1

arr = [-1, 0, 1, 2, 4, 10]
magic(arr, start=0)
