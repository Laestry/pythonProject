target = int(input("ПИРАМИДА СИМУЛЯТОР 2021!! Пожалуйста напишите размер пирамиды: "))
spaces = target
num = target
while 0 <= num + 2:
    for x in range(0, spaces):
        print(" ", end="")
    for x in range(0, target - num + 1):
        print("*", end="")

    print()
    spaces -= 1
    num -= 2
