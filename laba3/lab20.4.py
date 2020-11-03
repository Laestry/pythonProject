base = ["Иван", "Жора"]

s=input("Введите ваше имя: ")

def hello(s):
    print("Здравствуйте, ", s, "! Вашу карту ищут...")


def search_card(s):
    if s in base:
        print("Ваша карта с номером", str(base.index(s) + 1), "найдена")
    else:
        print("Ваша карта не найдена")

hello(s)
search_card(s)