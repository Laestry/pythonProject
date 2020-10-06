target = float(input("Пожалуйста напишите обезьяне в компьютере вашу цыфру: "))
counter = 0

while target != 1:
    if target % 2 == 0:
        target /= 2
    else:
        target -= 1

    counter += 1

print(counter)
