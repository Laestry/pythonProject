import random
import string

alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0987654321'
numPass = []


def has_numbers(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False


def has_upper(input_string):
    for char in input_string:
        if char.isupper():
            return True
    return False


def create_password(how_many, how_long):
    password = ''

    for _ in range(how_many):
        numPass.clear()
        while True:
            password = ''
            for i in range(how_long):
                r = random.randint(0, len(alphabet) - 1)
                password += alphabet[r]
            if has_upper(password) and has_numbers(password):
                break

        print(password)


create_password(4, 10)
