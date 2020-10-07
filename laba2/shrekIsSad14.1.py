recipesCount = int(input("Введите количество рецептов: "))
recipes = []

while recipesCount > 0:
    recipesCount -= 1
    tempRecipe = input("Введите рецепт: ")
    if not tempRecipe.__contains__("лук") and recipesCount > 1:
        recipes.append(tempRecipe + ",")
    elif not tempRecipe.__contains__("лук"):
        recipes.append(tempRecipe)

print(recipes)