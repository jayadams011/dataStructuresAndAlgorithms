"""Search an element in sorted and rotated array using single pass of
   binary Search.
"""

# Returns index of key in arr[start...end] if key is present,
# otherwise returns -1


def pivotSearch(arr, start, end, key):
    """Define function."""
    # Base case
    if start > end:
        return -1
    # find middle
    mid = (start + end) // 2
    if arr[mid] == key:
        return mid

    # If arr[start...mid] is sorted
    if arr[start] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[start] and key <= arr[mid]:
            return pivotSearch(arr, start, mid-1, key)
        return pivotSearch(arr, mid+1, end, key)

    # If arr[start..mid] is not sorted, then arr[mid...end]
    # must be sorted
    if key >= arr[mid] and key <= arr[end]:
        return pivotSearch(arr, mid+1, end, key)
    return pivotSearch(arr, start, mid-1, key)


arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
result = pivotSearch(arr, 0, len(arr)-1, 6)