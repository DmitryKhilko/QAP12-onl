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
