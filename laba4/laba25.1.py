import random

alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0987654321'
numPass = []


def create_password(how_many, how_long):
    for _ in range(how_many):
        numPass.clear()
        for i in range(how_long):
            r = random.randint(0, len(alphabet) - 1)
            if r not in numPass:
                print(alphabet[r], end='')
        print(" ")


create_password(4, 10)
