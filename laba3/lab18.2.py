def ask_password():
    answer = "password"
    for _ in range(3):
        if input("Введите пароль: ") == answer:
            return print("Пароль принять")

    print("В доступе отказано")

ask_password()
