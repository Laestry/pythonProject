again = True
miau = 0
flag = -1
while True:
    catTime = input("Напишите котику: ")
    miau += 1

    if again and "К" in catTime or "к" in catTime and "о" in catTime and "т" in catTime:
        flag = miau
        again = False

    if "СТОП" in catTime:
        break

print(flag)