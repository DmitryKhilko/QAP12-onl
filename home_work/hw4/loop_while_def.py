# Задание 1. Дано число N. Найти произведение всех чисел от 0 до N
""" Чек-лист для проверки функции:
1.  Произведение чисел от 0 до N (N целое число).
    Ожидаемый результат: вывод произведения чисел.
2.  Произведение чисел от 0 до N (N дробное число).
    Ожидаемый результат: вывод произведения чисел.
3.  Произведение чисел от 0 до N (N текстовое число).
    Ожидаемый результат: вывод произведения чисел.
4.  Произведение чисел от 0 до N (N нечисловые символы).
    Ожидаемый результат: вывод сообщения, что N должно быть числом
5.  Произведение чисел от 0 до N (N равно 0).
    Ожидаемый результат: вывод сообщения, что N должно быть больше 0.
5.  Произведение чисел от 0 до N (N пустое значение).
    Ожидаемый результат: вывод сообщения, что N должно быть числом, большим 0.
"""


def multiplication_of_numbers(numbers: int):
    multiplication = 1
    i = 1
    while i <= numbers:
        multiplication *= i
        i += 1
    return multiplication


# Задание 2
def calculation_of_years(area_1: int, area_2: int):
    year = 0
    while area_1 > area_2 * 0.1:
        area_1 *= 2
        area_2 *= 3
        year += 1
    return year


# Задание 3
def count_and_sum_number(number: int):
    sum_of_numbers = 0
    count_of_numbers = 0
    while number > 0:
        sum_of_numbers += number % 10
        number //= 10
        count_of_numbers += 1
    return sum_of_numbers, count_of_numbers


# Задание 4
def difference_calculation(grandfather_age: int, grandson_age: int):
    year = 0
    while grandfather_age > grandson_age * 2:
        year += 1
        grandfather_age += 1
        grandson_age += 1
    return year, grandfather_age, grandson_age
