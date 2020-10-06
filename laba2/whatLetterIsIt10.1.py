word = input("Введите слово: ")
position = int(input("Введите место: ")) - 1

if position > len(word) or position < 0:
    print("ОШИБКА!")
else:
    print(word[position])

