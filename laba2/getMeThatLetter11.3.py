word = input("Введите слово: ")
position = int(input("Введите место: ")) - 1
letter = input("Введите букву: ")

if position > len(word) or position < 0 or len(letter) > 1:
    print("ОШИБКА!")
elif word[position] == letter:
    print("Да!")
else:
    print("Нет!")


