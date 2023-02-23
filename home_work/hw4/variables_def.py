# Задание 1 - 5
def variables(var_int: int, var_float: float, var_str: str):
    big_int = var_int * 3.5
    var_float = var_float - 1
    var_str = var_str * 2 + "Yes" * 3
    return big_int, var_float, var_int / var_float, big_int / var_float, var_str