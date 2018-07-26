# Write an algorithm such that if an element in an MxN matrix is 0, its entire 
# row and column are set to 0.


def zerofy(mat):

    firstRowHasZeros = False
    firstColumnHasZeros = False

    # Check if first column has any zeros
    for i in range(0, len(mat)):
        if mat[i][0] == 0:
            firstColumnHasZeros = True

    # Check if first row has any zeros
    for i in range(0, len(mat[i])):
        if mat[0][i] == 0:
            firstRowHasZeros = True

    # Check rest of matrix for zeros, mark the row and the column using first
    # row and column
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if [i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    # Zerofy the marked columns and rows.
    for i in range(0, len(mat)):
        if mat[i][0] == 0:
            for j in range(1, len(mat[0])):
                mat[i][j] == 0

    for i in range(0, len([0])):
        if mat[0][i] == 0:
            for j in range(1, len(mat)):
                mat[j][i] = 0

    # Zero first column and row if necassary
    if firstRowHasZeros:
        for i in range(0, len(mat[0])):
            mat[0][i] = 0

    if firstColumnHasZeros:
        for i in range(0, len(mat)):
            mat[i][0] = 0

    return mat

mat = [[1, 1, 2, 3], [1, 0, 1, 5], [2, 3, 4, 5], [6, 7, 0, 8]]
result = zerofy(mat)
