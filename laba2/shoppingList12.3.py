shoppingList = []
amount = []
listLength = int(input("Введите длину списка: "))

for y in range(0, listLength):
    amount.append(input("Введите количество: "))
    shoppingList.append(input("Введите что хотите купить: "))

while listLength > 0:
    print(shoppingList[listLength - 1] + " " + amount[listLength - 1])
    listLength -= 1