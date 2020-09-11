target = int(input("Пожалуйста напишите количество камней: "))

while target != 0:
    print("Осталось", target, "Введите сколько хотите взять")
    takeAmount = int(input(": "))
    checker = target - takeAmount
    if checker < 0 or takeAmount > 3:
        print("Как-то много...")
        continue
    else:
        target -= takeAmount
        print("Осталось", target)

    if target == 0:
        print("Victory royal!")
        break

    if target >= 3:
        target -= 3
        print("Комп взял 3")
    elif target == 2:
        target -= 2
        print("Комп взял 2")
    elif target == 1:
        target -= 1
        print("Комп взял 1")

    if target == 0:
        print("Мой элитный ии победил!")
        break
