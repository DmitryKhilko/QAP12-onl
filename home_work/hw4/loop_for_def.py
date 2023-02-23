# Задание 1
def sum_of_integers(number1: int, number2: int):
    sum_numbers = 0
    for i in range(number1, number2 + 1):
        sum_numbers += i
    return sum_numbers


# Задание 2
def sum_of_natural_numbers(list_natural_numbers: list):
    sum_numbers = 0
    for i in range(len(list_natural_numbers)):
        if list_natural_numbers[i] > 0 and not isinstance(
            list_natural_numbers[i], float
        ):
            sum_numbers += list_natural_numbers[i]
    return sum_numbers


# Задание 3
def integer_operations(list_integers_numbers: list):
    multiplication_of_positive_num = 1
    sum_of_negative_num = 0
    count_of_negative_num = 0

    for i in range(len(list_integers_numbers)):
        if list_integers_numbers[i] > 0:
            multiplication_of_positive_num *= list_integers_numbers[i]
        else:
            sum_of_negative_num += list_integers_numbers[i]
            count_of_negative_num += 1
    return multiplication_of_positive_num, sum_of_negative_num, \
        count_of_negative_num


# Задание 4
def best_result(dict_swimmers: dict):
    for key, value in dict_swimmers.items():
        if value == max(dict_swimmers.values()):
            return f"Лучший результат заплыва: {key} - " \
                   f"{max(dict_swimmers.values())}"
