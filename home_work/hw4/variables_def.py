# Задание 1 - 5
def variables(var_int: int, var_float: float, var_str: str):
    big_int = var_int * 3.5
    var_float = var_float - 1
    var_str = var_str * 2 + "Yes" * 3
    return big_int, var_float, var_int / var_float, big_int / var_float, var_str

# # Задание 1. Переменной var_int присвойте значение 10,
# # var_float - значение 8.4, var_str - "No".
#
# var_int = 10
# var_float = 8.4
# var_str = "No"
#
# # Задание 2. Измените значение, хранимое в переменной var_int,
# # увеличив его в 3.5 раза, результат свяжите с переменной big_int.
#
# big_int = var_int * 3.5
# print(big_int)
#
# # Задание 3. Измените значение, хранимое в переменной var_float,
# # уменьшив его на единицу, результат свяжите с той же переменной.
#
# var_float = var_float - 1
# print(var_float)
#
# # Задание 4. Разделите var_int на var_float, а затем big_int на var_float.
# # Результат данных выражений не привязывайте ни к каким переменным.
#
# print(var_int / var_float)
# print(big_int / var_float)
#
# # Задание 5. Измените значение переменной var_str на "NoNoYesYesYes".
# # При формировании нового значения используйте операции конкатенации (+)
# # и повторения строки (*).
#
# var_str = var_str * 2 + "Yes" * 3
# print(var_str)
