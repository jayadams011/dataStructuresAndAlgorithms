# Python 3 program to rearrange 
# positive and negative numbers


def rearrange(a, n):
    """Define function."""
    positive = 0
    negative = 1

    while True:

        # Move forward the positive
        # pointer till negative number
        # number not encountered
        while positive < n and a[positive] % 2 == 0:
            positive = positive + 2

        # Move forward the negative
        # pointer till positive number
        # number not encountered
        while negative < n and a[negative] % 2 == 1:
            negative = negative + 2

        # Swap array elements to fix
        # their position.
        if (positive < n and negative < n):
            temp = a[positive]
            a[positive] = a[negative]
            a[negative] = temp

        # Break from the while loop when
        # any index exceeds the size of
        # the array
        else:
            break

# Driver code
a = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
n = len(a)

rearrange(a, n)
