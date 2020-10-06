schoolFilter = []
schoolFilterLength = int(input("Введите длину филтра: "))

for y in range(0, schoolFilterLength):
    schoolFilter.append(input("Введите слово для филтра: "))

wordsFilterCheck = []
wordsFilterCheckLength = int(input("Введите количество ваших слов: "))

for x in range(0, wordsFilterCheckLength):
    wordsFilterCheck.append(input("Введите слово: "))

print(list(set(wordsFilterCheck) & set(schoolFilter)))