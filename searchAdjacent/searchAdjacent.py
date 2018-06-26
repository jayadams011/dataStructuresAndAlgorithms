"""Search an element in an array where difference between.

adjacent elements is 1.
For example: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}.
Search for 3 and Output: Found at index 7.
"""


def searchAdjacent(arr, x, n):
    """Define function."""
    i = 0
    while i < n:
        if arr[i] == x:
            return i

        i = i + abs(arr[i] - x)
    return -1
