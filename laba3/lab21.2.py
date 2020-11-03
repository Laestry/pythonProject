matrix = [[1, 2], [3, 4]]


def transpose(matrix):
    newmatrix = []
    size = len(matrix[0])
    for _ in range(size):
        newmatrix += [[0] * len(matrix)]

    for y in range(len(newmatrix)):
        for x in range(len(newmatrix[0])):
            newmatrix[y][x] = matrix[x][y]

    matrix.clear()
    matrix.extend(newmatrix)
    print(matrix)


transpose(matrix)
