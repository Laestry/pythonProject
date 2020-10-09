bacteriaCount = [10, 10, 9], [10, 10, 10], [10, 10, 10]
bacteriaCountTemp = []

matrixSize = int(input("Введите размер матрицы: "))
# for _ in range(matrixSize):
#     bacteriaCountTemp = []
#     for _ in range(matrixSize):
#         bacteriaCountTemp.append(int(input("Количесто бактерии: ")))
#     bacteriaCount.append(bacteriaCountTemp)

attackCount = int(input("Количество капель: "))
coordinates = []
for _ in range(attackCount):
    x = int(input("Первая координата: "))
    y = int(input("Вторая координата: "))

    if bacteriaCount[x][y] - 8 < 0:
        bacteriaCount[x][y] = 0
    else:
        bacteriaCount[x][y] -= 8

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i != x or j != y) and 0 <= i < matrixSize and 0 <= j < matrixSize:
                if bacteriaCount[i][j] - 4 < 0:
                    bacteriaCount[i][j] = 0
                else:
                    bacteriaCount[i][j] -= 4

for z in range(matrixSize):
    for g in range(matrixSize):
        print(bacteriaCount[z][g] + " ", end='')
    print()
