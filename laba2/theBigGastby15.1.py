forbidden = input("Буква которая запрешена: ")
text = input("Пишите: ").split(' ')

for x in range(0, len(text)):
    if forbidden in text[x]:
        print(text[x])
