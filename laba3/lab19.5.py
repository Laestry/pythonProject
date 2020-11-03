def prime(number):
    i = number - 1
    while i > 1:
        if (number % i) == 0:
            return print("Составное")
        i -= 1

    return print("Простое")


prime(int(input('Введите число: ')))

