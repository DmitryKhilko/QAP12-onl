# Задание 1 - 3
def bool_and_1(var_1: int, var_2: int) -> bool:
    if 2 < var_1 < 5 and 3 < var_2 <= 4:  # True
        return True
    else:
        return False


def bool_and_2(var_1: int, var_2: int) -> bool:
    if 0 < var_1 < var_2 and var_1 < var_2 < 10:  # True
        return True
    else:
        return False


def bool_and_3(var_1: int, var_2: int) -> bool:
    if var_2 < var_1 < var_1 + 1 and 10 < var_2 < 11:  # False
        return True
    else:
        return False


def bool_and_4(var_1: int, var_2: int) -> bool:
    if 0 < var_1 < 2 and 10 < var_2 < var_1:  # False
        return True
    else:
        return False


def bool_or_1(var_1: int, var_2: int) -> bool:
    if var_1 < var_2 or var_2 <= 4:  # True
        return True
    else:
        return False


def bool_or_2(var_1: int, var_2: int) -> bool:
    if 0 < var_1 < var_2 or var_1 < var_2 < 10:  # True
        return True
    else:
        return False


def bool_or_3(var_1: int, var_2: int) -> bool:
    if not (var_1 < var_2 or var_2 <= 4):  # False
        return True
    else:
        return False


def bool_or_4(var_1: int, var_2: int) -> bool:
    if var_2 < var_1 or 10 < var_2 <= 20:  # False
        return True
    else:
        return False


# Задание 4
def bool_str_1(string_1: str, string_2: str) -> bool:
    if 0 < len(string_1) < 20 and string_2.find('вторая'):  # True
        return True
    else:
        return False


def bool_str_2(string_1: str, string_2: str) -> bool:
    if string_1 == string_2 or string_1 in string_2:  # False
        return True
    else:
        return False
