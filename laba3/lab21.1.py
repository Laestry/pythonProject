a = [1, 2, 3]


def from_string_to_list(string, container):
    for x in range(len(string)):
        container.append(string[x])

    for y in range(len(a)):
        if a[y] == " ":
            continue
        print(str(a[y]) + " ", end='')


from_string_to_list("1 3 99 52", a)
