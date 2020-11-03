from numpy.core.defchararray import lower

alphabet = 'abcdefghijklmnopqrstuvwyz'
target = ['mother', 'Daddy', 'sIster']
d = {}
letter_to_index = dict(zip(alphabet, range(len(alphabet))))


def calculate_gematria(word):
    sum = 0
    for i in range(len(word)):
        sum += letter_to_index[word[i]]

    return sum


def add_to_dictionary():
    for word in target:
        d[word] = calculate_gematria(str(lower(word)))

    print(sorted(d))


add_to_dictionary()
