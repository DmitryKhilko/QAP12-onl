# Задание 1
def len_string(string: str):
    list_of_string = list(string)
    list_of_string.pop(0)
    list_of_string.pop()  # удаляем последний символ
    list_of_string.pop(2)
    list_of_string.pop(-2)
    return len(list_of_string)


# Задание 2
def string_operations(string: str):
    # первые восемь символов
    o_1 = string[0:8]
    # четыре символа из центра строки
    o_2 = string[int(len(string) / 2 - 1):int(len(string) / 2 + 3)]
    # символы с индексами кратными трем
    o_3 = string[2:int(len(string)):3]
    # перевернуть строку
    o_4 = string[::-1]
    return o_1, o_2, o_3, o_4


# Задание 3
def inserting_name_into_string(original_string: str, substring_to_replace: str,
                               name: str):
    return original_string.replace(substring_to_replace,
                                   name).replace(name, substring_to_replace, 1)


# Задание 4
def string_operations_1(string: str, sub_str: str):
    o_1 = string.find("Hello")  # 0
    o_2 = string.find("e")  # 1
    o_3 = string.find("w") + 1
    o_4 = string.count("l")

    if string.find("Hello") == 0:
        o_5 = "Строка начинается с подстроки 'Hello'"
    else:
        o_5 = "Строка не начинается с подстроки 'Hello'"

    if string.find(sub_str, len(string) - len(sub_str), len(string)) != -1:
        o_6 = f"Строка оканчивается на подстроку '{sub_str}'"
    else:
        o_6 = f"Строка не оканчивается на подстроку '{sub_str}'"

    return o_1, o_2, o_3, o_4, o_5, o_6
