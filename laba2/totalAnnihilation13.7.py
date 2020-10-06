listLength = int(input("Введите длину списка: "))
name = ["Марк", "Валерий", "Акакий", "Антонин", "Иннокентий", "Ипполит", "Юлий"]

# for y in range(0, listLength):
#     name.append(input("Введите имя: "))

order = int(input("Введите порядок: "))

while listLength > 0:
    print(name[0])
    i = 0
    executionList = []

    if listLength == 2:
        print(name[1])
        break

    while i < listLength-1:
        i += 3
        print(name[i])
        executionList.append(i)
    
    listLength -= len(executionList) + 1

    name.pop(0)
    j = 1
    for x in range(0, len(executionList)):
        name.pop(executionList[x] - j)
        j += 1


# 7
# Марк
# Валерий
# Акакий
# Антонин
# Иннокентий
# Ипполит
# Юлий
# 3

# Марк
# Антонин
# Юлий
# Валерий
# Ипполит
# Акакий
# Иннокентий