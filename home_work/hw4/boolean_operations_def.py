# Задание 1 - 3
def bool_and_1(var1: int, var2: int) -> bool:
    if 2 < var1 < 5 and 3 < var2 <= 4:  # True
        return True
    else:
        return False


def bool_and_2(var1: int, var2: int) -> bool:
    if 0 < var1 < var2 and var1 < var2 < 10:  # True
        return True
    else:
        return False


def bool_and_3(var1: int, var2: int) -> bool:
    if var2 < var1 < var1 + 1 and 10 < var2 < 11:  # False
        return True
    else:
        return False


def bool_and_4(var1: int, var2: int) -> bool:
    if 0 < var1 < 2 and 10 < var2 < var1:  # False
        return True
    else:
        return False


def bool_or_1(var1: int, var2: int) -> bool:
    if var1 < var2 or var2 <= 4:  # True
        return True
    else:
        return False


def bool_or_2(var1: int, var2: int) -> bool:
    if 0 < var1 < var2 or var1 < var2 < 10:  # True
        return True
    else:
        return False


def bool_or_3(var1: int, var2: int) -> bool:
    if not (var1 < var2 or var2 <= 4):  # False
        return True
    else:
        return False


def bool_or_4(var1: int, var2: int) -> bool:
    if var2 < var1 or 10 < var2 <= 20:  # False
        return True
    else:
        return False


# # Задание 1. Присвойте двум переменным любые числовые значения.
# a = 3
# b = 4
#

# # Задание 4. Попробуйте использовать в сложных логических выражениях
# # работу с переменными строкового типа.
# string_1 = 'Строка первая'
# string_2 = 'Строка вторая'
#
# if 0 < len(string_1) < 20 and string_2.find('вторая'):  # True
#     print(True)
# else:
#     print(False)
#
# if string_1 == string_2 or string_1 in string_2:  # False
#     print(True)
# else:
#     print(False)
