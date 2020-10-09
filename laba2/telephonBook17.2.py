while True:
    numberCount = int(input("Введите количество номеров: "))
    if 1 <= numberCount <= 1000:
        break
    else:
        print("Введите больше чем 0 и меньше чем 1001")

number = []
for _ in range(numberCount):
    number.append(input("Введите номер и имя: "))

while True:
    requestCount = int(input("Введите количество запросов: "))
    if 1 <= numberCount <= 100:
        break
    else:
        print("Введите больше чем 0 и меньше чем 101")

for _ in range(requestCount):
    name = input("Введите имя: ")
    counter = 0
    for x in range(numberCount):
        if name in number[x]:
            numberTemp = number[x].split(" ")
            print(numberTemp[0])
        else:
            counter += 1
        if counter == numberCount:
            print("Нет в телефоной книге")
