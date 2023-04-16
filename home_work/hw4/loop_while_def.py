import unittest

# Задание 1. Дано число N. Найти произведение всех чисел от 0 до N
"""
Уточнение требований:
1.  N целое число.
2.  1 <= N <= 10.

Чек-лист для проверки функции:
1.  Произведение чисел от 0 до N (N равно минимальному значению).
    Ожидаемый результат: вывод произведения чисел.
2.	Произведение чисел от 0 до N (N внутри класса эквивалентности).
    Ожидаемый результат: вывод произведения чисел.
3.	Произведение чисел от 0 до N (N равно максимальному значению).
    Ожидаемый результат: вывод произведения чисел.
4.	Произведение чисел от 0 до N (N отрицательное число).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
5.	Произведение чисел от 0 до N (N равно 0).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
6.	Произведение чисел от 0 до N (N больше максимального значения).
    Ожидаемый результат: вывод сообщения, что N должно быть больше или равно 1
    и меньше или равно 10.
7.	Произведение чисел от 0 до N (N пустое).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
8.	Произведение чисел от 0 до N (N - None).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
9.	Произведение чисел от 0 до N (N - несколько пробелов).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
10.	Произведение чисел от 0 до N (N символьное значение).
    Ожидаемый результат: вывод сообщения, что N должно быть числом целого типа.
"""


def multiplication_of_numbers(number: int):
    try:
        if type(number) not in [int]:
            raise TypeError(f"Вы ввели значение '{number}'. Вводимое значение "
                            f"должно быть числом целого типа")
        if number < 1 or number > 10:
            raise ValueError(
                f"Вы ввели число {number}. Вводимое число должно быть"
                f" от 1 до 10")

        multiplication = 1
        i = 1
        while i <= number:
            multiplication *= i
            i += 1
        return multiplication

    except TypeError as exc:
        print(exc)
    except ValueError as exc:
        print(exc)


class TestMultiplicationOfNumber(unittest.TestCase):

    def test_min_value(self):
        self.assertEqual(1, multiplication_of_numbers(1),
                         "Произведение чисел не равно 1")

    def test_internal_value(self):
        self.assertEqual(multiplication_of_numbers(5), 120,
                         "Произведение чисел не равно 120")

    def test_max_value(self):
        self.assertEqual(3628800, multiplication_of_numbers(10),
                         "Произведение чисел не равно 3628800")

    def test_negative_value(self):
        self.assertIsNone(multiplication_of_numbers(-1))

    def test_zero_value(self):
        self.assertIsNone(multiplication_of_numbers(0))

    def test_more_max_value(self):
        self.assertIsNone(multiplication_of_numbers(11))

    def test_empty_value(self):
        self.assertIsNone(multiplication_of_numbers(""))

    def test_none_value(self):
        self.assertIsNone(multiplication_of_numbers(None))

    def test_spaces_value(self):
        self.assertIsNone(multiplication_of_numbers("   "))

    def test_symbol_value(self):
        self.assertIsNone(multiplication_of_numbers("проверка"))


# Задание 2. Поле засеяли цветами двух сортов на площади S1 и S2.
# Каждый год площадь цветов первого сорта увеличивается вдвое,
# а площадь второго сорта увеличивается втрое.
# Через сколько лет площадь первых сортов будет составлять меньше 10%
# от площади вторых сортов.
""" 
Чек-лист для проверки функции:

Уточнение требований:
1.  S1, S2 - целые числа
2.  0 < S1 <= 5
3.  0 < S2 <= 3

1.  Вычисление количества лет (S1, S2: числа на нижней границе).
    Ожидаемый результат: вычисленное количество лет.
2.  Вычисление количества лет (S1, S2: числа внутри классов эквивалентности).
    Ожидаемый результат: вычисленное количество лет.
3.  Вычисление количества лет (S1, S2: числа на верхней границе).
    Ожидаемый результат: вычисленное количество лет.
4.  Вычисление количества лет (S1, S2: числа ниже верхней границы).
    Ожидаемый результат: вычисленное количество лет.
5.  Вычисление количества лет (S1, S2: числа выше верхней границы).
    Ожидаемый результат: сообщение, что введенные цифры вне разрешенных диапазонов.
6.  Вычисление количества лет (S1, S2: числа ниже нижней границы).
    Ожидаемый результат: вычисленное количество лет.
7.  Вычисление количества лет (S1, S2: числа на нижней границы).
    Ожидаемый результат: вычисленное количество лет.
8.  Вычисление количества лет (S1, S2: числа выше нижней границы).
    Ожидаемый результат: вычисленное количество лет.
9.  Вычисление количества лет (S1: 0; S2: позитивное число).
    Ожидаемый результат: вывод сообщение, что S1 должна быть в разрешенном диапазоне.
10. Вычисление количества лет (S1: не целое число; S2: позитивное число).
    Ожидаемый результат: вывод сообщение, что S1 должна быть числом в разрешенном диапазоне.
11. Вычисление количества лет (S1: позитивное число; S2: пусто).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
12. Вычисление количества лет (S1: позитивное число; S2: 0).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
13. Вычисление количества лет (S1: позитивное число; S2: не целое число).
    Ожидаемый результат: вывод сообщение, что S2 должна быть числом в разрешенном диапазоне.
"""


def calculation_of_years(area_1: int, area_2: int):
    if type(area_1) in [int]:
        if type(area_2) in [int]:
            if 0 < area_1 <= 5:
                if 0 < area_2 <= 3:
                    year = 1
                    while area_1 > area_2 * 0.1:
                        area_1 *= 2
                        area_2 *= 3
                        year += 1
                    return area_1, area_2, year
                else:
                    return "S2 должна быть в диапазоне от 1 до 3"
            else:
                return "S1 должна быть в диапазоне от 1 до 5"
        else:
            return "S2 должно быть целым числом в диапазоне от 1 до 3"
    else:
        return "S1 должно быть целым числом в диапазоне от 1 до 5"


class TestCalculationOfYears(unittest.TestCase):

    def test_01(self):
        self.assertEqual((64, 729, 7), calculation_of_years(1, 1))

    def test_02(self):
        self.assertEqual((384, 4374, 8), calculation_of_years(3, 2))

    def test_03(self):
        self.assertEqual((640, 6561, 8), calculation_of_years(5, 3))

    def test_04(self):
        self.assertEqual((1024, 13122, 9), calculation_of_years(4, 2))

    def test_05(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(6, 4))

    def test_06(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(-1, 0))

    def test_07(self):
        self.assertEqual((64, 729, 7), calculation_of_years(1, 1))

    def test_08(self):
        self.assertEqual((1024, 13122, 9), calculation_of_years(4, 2))

    def test_09(self):
        self.assertEqual("S1 должна быть в диапазоне от 1 до 5",
                         calculation_of_years(0, 2))

    def test_10(self):
        self.assertEqual("S1 должно быть целым числом в диапазоне от 1 до 5",
                         calculation_of_years("проверка", 2))

    def test_11(self):
        self.assertEqual("S2 должно быть целым числом в диапазоне от 1 до 3",
                         calculation_of_years(4, None))

    def test_12(self):
        self.assertEqual("S2 должна быть в диапазоне от 1 до 3",
                         calculation_of_years(4, 0))

    def test_13(self):
        self.assertEqual("S2 должно быть целым числом в диапазоне от 1 до 3",
                         calculation_of_years(4, 1.2))





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
