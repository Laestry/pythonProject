while True:
    birthdayCount = int(input("Введите количество дней рождения: "))
    if 1 <= birthdayCount <= 1000:
        break
    else:
        print("Введите больше чем 0 и меньше чем 1001")

number = []
for _ in range(birthdayCount):
    number.append(input("Введите имя, день и месяц: "))

while True:
    requestCount = int(input("Введите количество запросов: "))
    if 1 <= birthdayCount <= 100:
        break
    else:
        print("Введите больше чем 0 и меньше чем 101")

for _ in range(requestCount):
    name = input("Введите месяц: ")
    counter = 0
    for x in range(birthdayCount):
        if name in number[x]:
            numberTemp = number[x].split(" ")
            print(numberTemp[0] + " " + numberTemp[1])
        else:
            counter += 1
        if counter == birthdayCount:
            print("")
