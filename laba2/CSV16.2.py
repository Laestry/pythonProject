phrases = []
phrasesTemp = []
for _ in range(int(input("Введите количество строк: "))):
    phrasesTemp = (input("Пишите фразу: ").split(","))
    phrases.append(phrasesTemp)

coordinates = []
for _ in range(int(input("Введите количество координат: "))):
    coordinates = (input("Введите координату: ").split(","))
    print(phrases[int(coordinates[0])][int(coordinates[1])])


