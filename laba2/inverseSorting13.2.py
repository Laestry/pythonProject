listLength = int(input("Введите длину списка: "))
amount = []

for y in range(0, listLength):
    amount.append(input("Введите цифру: "))

while listLength > 0:
    print(amount[listLength - 1])
    listLength -= 1