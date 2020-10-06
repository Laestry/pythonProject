M = int(input("Введите количетсво блюд: "))
N = int(input("Введите количетсво дней: "))

dishes = []
triedDishes = []
notTriedDishes = []

for y in range(1, M):
    dishes.append(input("Введите блюдо: "))

for x in range(1, N):
    dailyDishCount = int(input("Введите сколько блюд было в этот день: "))
    for z in range(1, dailyDishCount):
        triedDishes.append(input("Введите блюдо которое пробовали: "))

notTriedDishes = list(set(dishes) - set(triedDishes))

print(notTriedDishes)

