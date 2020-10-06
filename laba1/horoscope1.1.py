def horoscope():
    forename = input("Привет я ии гороскоп, напишите ваше имя: ")
    surname = input("Теперь вашу фамилию: ")
    animal = input("Ваше живтное: ")
    zodiac = input("Ваш знак зодиака: ")

    print("Индивидуальный гороскоп для пользователя", forename, " ", surname)
    print("Кем вы были в прошлой жизни:", animal)
    print("Ваш знак зодиака - ", zodiac, ", поэтому вы - тонко чувствующая натура.")

horoscope()