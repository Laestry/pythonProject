jokes = []


def print_only_new(s):
    if s in jokes:
        return
    else:
        print(s)
        jokes.append(s)


while True:
    print_only_new(input("Шутка сбда ->"))
