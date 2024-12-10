# 1. Функция с параметрами по умолчанию:
# Создаем функцию print_params,
# которая принимает три параметра со значениями по умолчанию.
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Тестируем функцию
print_params(b=25)
print_params(c=[1, 2, 3])

print("--------------")

# 2. Распаковка параметров.
# Создаем список с тремя элементами разных типов.
values_list = [5, True, "Строка"]
key_list = ["a", "b", "c"]

# Создаем словарь с тремя ключами, соответствующими параметрам
# функции print_params, и значениями разных типов.
# values_dict = dict(zip(key_list, values_list))
values_dict = {key_list[i]: values_list[i] for i in range(len(key_list))}

# Тестируем функцию
print_params(*values_list)
print_params(**values_dict)

print("--------------")

# 3. Распаковка + отдельные параметры.
# Создаем список с двумя элементами разных типов.
values_list_2 = [54.32, 'Строка']

# Тестируем функцию
print_params(*values_list_2, c=42)
