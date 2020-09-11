x = float(input("The Division! Пожалуйста напишите размер x: "))
y = float(input("Теперь размер y: "))

counter = y

for z in range(1, int(x + 1)):
    print(float(z), " ", end="")

print()

while counter > 1:
    for z in range(1, int(x + 1)):
        print(round(z/counter, 1), " ", end="")
    print()

    counter -= 1
