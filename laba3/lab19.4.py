def palindrome(s):
    i = len(s)
    temp = ""
    while i > 0:
        temp += s[i-1]
        i -= 1

    if s == temp:
       return "Палиндром"
    return "Не палиндром"

print(palindrome('12321'))
print(palindrome('Палиндром'))