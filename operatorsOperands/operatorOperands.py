"""Operators and operands."""


def evaluate(someStr):
    """Define function."""
    stack = []
    sum = []

    # Iterate over the expression for conversion
    for i in someStr:

            # If the scanned character is an operand
            # (number here) push it to the stack
        if i.isdigit():
            stack.append(i)

            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            x = eval(val2 + i + val1)
            y = str(x)
            stack.append(y)

    return stack.pop()


someStr = "231*+"
result = evaluate(someStr)
