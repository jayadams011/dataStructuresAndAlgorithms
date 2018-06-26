def blendArr(arrA, arrB):
    """ Define function."""
    i = 0
    j = 0
    total = len(arrA) + len(arrB)
    arrAB = []

    while len(arrAB) != total:
        if len(arrA) == i:
            arrAB += arrB[j:]
        elif len(arrB) == j:
            arrAB += arrA[i:]
        elif arrA[i] < arrB[j]:
                arrAB.append(arrA[i])
                i += 1
        else:
            arrB[j] < arrA[i]
            arrAB.append(arrB[j])
            j += 1
    return arrAB

arrA = [10, 22, 35, 40]
arrB = [1, 5, 17]
result = blendArr(arrA, arrB,)
