counter = int(input("Пожалуйста напишите сколько цифр будете вводить: "))
flag = 0
target = int(input("Пожалуйста напишите первую цифру: "))

while counter >= 1:
    num = int(input("Напишите цифру: "))

    if not flag:
        target -= num
        flag = 1
    else:
        target += num
        flag = 0

    counter -= 1

print(target)
