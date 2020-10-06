family = []

i = int(input("Введите количество сотрудников: "))

j = 0

for x in range(0, i):
    family.append(input("Введите фамилию: "))

for z in range(0, i):
    temp = family[z]
    for y in range(0, i):
        if temp == family[y]:
            j += 1
    j -= 1

print(j)
