y = int(input("ПРЯМОУГОЛЬНИК СИМУЛЯТОР 2049!! Пожалуйста напишите размер y: "))
x = int(input("Теперь размер x: "))
sign = input("Ваш знак: ")
spaces = x - 2

counter = y - 2

for z in range(0, x):
    print(sign, end="")

print()

while counter > 0:
    print(sign, end="")
    for z in range(0, spaces):
        print(" ", end="")
    print(sign, end="")
    print()
    counter -= 1

for z in range(0, x):
    print(sign, end="")

