# Самостоятельная работа по уроку "Рекурсия".
# Задача "Рекурсивное умножение цифр.

def get_multiplied_digits(number):

    str_number = str(number)

    first = str_number[0]

    if first == "0":
        return 1

    if len(str_number) <= 1:
        return int(first)

    return int(first) * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)

print(result)
print(result2)


