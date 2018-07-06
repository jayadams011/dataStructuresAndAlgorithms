"""Missing Parenth."""


def missingParenth(str):
    """Define missing Parenth Function."""
    left = []
    right = []

    for i in str:
        if i == '(':
            left.append(i)
        if i == ')':
            right.append(i)
            if len(left) == len(right):
                return 'No missing parenth'
            if len(left) < len(right):
                return 'Missing left parenth'
            if len(left) > len(right):
                return 'Missing right parenth'

str = "2 * ( 3 + 5(sasdfasdfasd)"
result = missingParenth(str)
