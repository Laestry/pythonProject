values = [0, 2, 10, 6]
values2 = [1, 2, 3, 4]


def same_by(x, val):
    for v in val:
        if x(v) > 0:
            return False

    return True


if same_by(lambda x: x % 2, values2):
    print('same')
else:
    print('different')
