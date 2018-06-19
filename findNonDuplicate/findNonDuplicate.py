"""Binary search based function to find the element that appears only once."""


def find(arr, low, high):
    """Define function find."""
    # Base cases
    if low > high:
        return None

    if low == high:
        return arr[int(low)]

    # Find the middle point
    mid = high//2

    # If mid is even and element next to mid is
    # same as mid, then output element lies on
    # right side, else on left side
    if mid % 2 == 0:
        if arr[int(mid)] == arr[int(mid+1)]:
            return find(arr, mid+2, high)
        else:
            return find(arr, low, mid)

    else:
        # if mid is odd
        if arr[int(mid)] == arr[int(mid-1)]:
            return find(arr, mid+1, high)
        else:
            return find(arr, low, mid-1)
