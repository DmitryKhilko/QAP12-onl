import unittest
# Задание 1. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.
"""
Чек-лист для проверки функции:

А и В - целые числа
A < B
1 < A <= 5
5 < B < 10

1.  Сумма целых чисел (А: целое число меньше В; В: целое число больше A).
    Ожидаемый результат: вывод суммы
2.  Сумма целых чисел (А: целое число на нижней границе; В: целое число на нижней границе).
    Ожидаемый результат: вывод суммы
3.  Сумма целых чисел (А: целое число выше нижней границы; В: целое число выше нижней границы).
    Ожидаемый результат: вывод суммы
4.  Сумма целых чисел (А: целое число на верхней границе; В: целое число на верхней границе).
    Ожидаемый результат: вывод суммы
5.  Сумма целых чисел (А: целое число ниже верхней границы; В: целое число ниже верхней границы).
    Ожидаемый результат: вывод суммы
6.  Сумма целых чисел (А: целое число больше В; В: целое число меньше A).
    Ожидаемый результат: вывод сообщения, что В должно быть числом, большим А.
7.  Сумма целых чисел (А: позитивное число; В: дробное число).
    Ожидаемый результат: вывод сообщения, число В должно быть целым числом в диапазоне 6 до 9.
8.  Сумма целых чисел (А: позитивное число; В: не число).
    Ожидаемый результат: вывод сообщения, что В должно быть целым числом.
9.  Сумма целых чисел (А: позитивное число; В: 0).
    Ожидаемый результат: вывод сообщения, что В должно быть целым числом в диапазоне от 6 до 9.
10. Сумма целых чисел (А: позитивное число; В: пусто).
    Ожидаемый результат: вывод сообщения, что В целым числом в диапазоне от 6 до 9.
11. Сумма целых чисел (А: дробное число; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что число А должно быть целым числом в диапазоне от 2 до 5.
12. Сумма целых чисел (А: не число; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
13. Сумма целых чисел (А: 0; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
14. Сумма целых чисел (А: пусто; В: позитивное число).
    Ожидаемый результат: вывод сообщения, что А должно быть целым числом в диапазоне от 2 до 5.
"""


def sum_of_integers(number_1: int, number_2: int):
    if type(number_1) in [int]:
        if type(number_2) in [int]:
            if 1 < number_1 <= 5:
                if 5 < number_2 <= 10:
                    sum_numbers = 0
                    for i in range(number_1, number_2 + 1):
                        sum_numbers += i
                    return sum_numbers
                else:
                    return "B должно быть в диапазоне от 6 до 10"
            else:
                return "А должно быть в диапазоне от 2 до 5"
        else:
            return "В должно быть целым числом в диапазоне от 6 до 10"
    else:
        return "А должно быть целым числом в диапазоне от 2 до 5"


class TestSumOfIntegers(unittest.TestCase):

    def test_01(self):
        self.assertEqual(25, sum_of_integers(3, 7))

    def test_02(self):
        self.assertEqual(20, sum_of_integers(2, 6))

    def test_03(self):
        self.assertEqual(25, sum_of_integers(3, 7))

    def test_04(self):
        self.assertEqual(35, sum_of_integers(5, 9))

    def test_05(self):
        self.assertEqual(30, sum_of_integers(4, 8))

    def test_06(self):
        self.assertEqual("А должно быть в диапазоне от 2 до 5",
                         sum_of_integers(7, 5))

    def test_07(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, 7.1))

    def test_08(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, "6"))

    def test_09(self):
        self.assertEqual("B должно быть в диапазоне от 6 до 10",
                         sum_of_integers(3, 0))

    def test_10(self):
        self.assertEqual("В должно быть целым числом в диапазоне от 6 до 10",
                         sum_of_integers(3, ""))

    def test_11(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers(3.1, 6))

    def test_12(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers("3", 6))

    def test_13(self):
        self.assertEqual("А должно быть в диапазоне от 2 до 5",
                         sum_of_integers(0, 6))

    def test_14(self):
        self.assertEqual("А должно быть целым числом в диапазоне от 2 до 5",
                         sum_of_integers("", 6))



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
