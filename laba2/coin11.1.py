coinToss = input("Введите результат бросков: ")

tossLength = len(coinToss)
oLength = 0
oLengthArr = []

for y in range(0, tossLength-1):
    if coinToss[y] == "о":
        oLength += 1
    else:
        oLengthArr.append(oLength)
        oLength = 0

print(max(oLengthArr))