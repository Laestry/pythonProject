alphabet = 'abcdefghijklmnopqrstuvwyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift):
    cipher = ''

    for letter in message:
        index = (letter_to_index[letter] + shift) % len(alphabet)
        shifted_letter = index_to_letter[index]

        cipher += shifted_letter;

    return cipher


def main():
    message = encrypt('we ride at dawn', 3)
    print(message)
    print(encrypt(message, -3))


main()
