num = int(input("Пожалуйста напишите количество строк: "))
miau = "НЕТ"

while num > 0:
    num -= 1
    catTime = input("Напишите котику: ")

    if "К" in catTime or "к" in catTime and "о" in catTime and "т" in catTime:
        miau = "МЯУ"

print(miau)
