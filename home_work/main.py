from home_work.hw3 import (convert_to_int, replace_char_in_str, add_to_string,
                           changing_position_words,
                           remove_begin_and_end_spaces, add_class,
                           extracting_element_from_list, string_occurrence,
                           char_output_1, char_output_2, unique_number)
from home_work.hw4 import (variables, len_string, string_operations,
                           inserting_name_into_string, string_operations_1,
                           list_operations, intersection_of_many,
                           list_unique_values, bool_and_1, bool_and_2,
                           bool_and_3, bool_and_4, bool_or_1, bool_or_2,
                           bool_or_3, bool_or_4, bool_str_1, bool_str_2,
                           count_student, change_count_students,
                           add_school_classes, delete_class, str_to_arr,
                           greetings, list_to_str, add_pop_list,
                           merging_dictionaries, number_operations,
                           number_of_positive_numbers, days_a_year,
                           name_of_day, conversion_to_kilograms,
                           sum_of_integers, sum_of_natural_numbers,
                           integer_operations, best_result,
                           multiplication_of_numbers, calculation_of_years,
                           count_and_sum_number, difference_calculation)

# hw3. Задание 1
print(convert_to_int(-1.6))
print(convert_to_int(2.99))

# hw3. Задание 2
str_old = "www.my_site.com#about"
s_old = "#"
s_new = "/"
print(replace_char_in_str(str_old, s_old, s_new))

# hw3. Задание 3
string_1 = "stroka"
string_2 = "ing"
print(add_to_string(string_1, string_2))

# hw3. Задание 4
fio_old = "Ivanov Ivan"
print(changing_position_words(fio_old))

# hw3. Задание 5
string = " Мама мыла мылом раму "
print(remove_begin_and_end_spaces(string))

# hw3. Задание 6
school = {}
add_class(school, "1а", 21)
add_class(school, "2а", 20)
add_class(school, "3а", 25)
add_class(school, "4а", 23)
add_class(school, "5а", 22)
add_class(school, "6а", 21)
add_class(school, "7а", 24)
add_class(school, "8а", 27)
add_class(school, "9а", 22)
add_class(school, "10а", 25)
print(f"Школьные классы: {school}")

# hw3. Задание 7
list_1 = ["стол", "стул", "кровать", "шкаф"]
print(extracting_element_from_list(list_1, 1))

# hw3. Задание 8
string_1 = "employment"
string_2 = "employ"
print(string_occurrence(string_1, string_2))

# hw3. Задание 9.1
string_1 = "My name is Agent Smith"
index = 1
print(char_output_1(string_1, index))

# hw3. Задание 9.2
string_1 = "My name is Agent Smith"
start_index = 3
stop_index = 16
step = 3
print(char_output_2(string_1, start_index, stop_index, step))

# hw3. Задание 10
list_1 = [1, 5, 2, 9, 2, 9, 1]
print(unique_number(list_1))

# variables. Задание 1 - 5
var_int = 10
var_float = 8.4
var_str = "No"
print(variables(var_int, var_float, var_str))

# strings. Задание 1
string_1 = "Не менее 8 символов"
print(len_string(string_1))

# strings. Задание 2
string_1 = "абвгдеёжзийклм"
print(string_operations(string_1))

# strings. Задание 3
string_1 = "my name is name"
string_2 = "name"
string_3 = "Dmitry"
print(inserting_name_into_string(string_1, string_2, string_3))

# strings. Задание 4
string_1 = "Hello world!"
sub_str_1 = "qwe"
print(string_operations_1(string_1, sub_str_1))

# lists. Задание 1 - 6
x = ["стол", "стул", "кровать", "шкаф"]
y = ["1", "2", "3", "4"]
print(list_operations(x, y))

# lists. Задание 7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersection_of_many(a, b))

# lists. Задание 8
d = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list_unique_values(d))

# boolean_operations. Задание 1 - 3
a = 3
b = 4
print(bool_and_1(a, b))
print(bool_and_2(a, b))
print(bool_and_3(a, b))
print(bool_and_4(a, b))
print(bool_or_1(a, b))
print(bool_or_2(a, b))
print(bool_or_3(a, b))
print(bool_or_4(a, b))

# boolean_operations. Задание 4
string_1 = 'Строка первая'
string_2 = 'Строка вторая'
print(bool_str_1(string_1, string_2))
print(bool_str_2(string_1, string_2))

# dictionaries. Задание 1 - 3
school = {
    '1a': 20,
    '2б': 18,
    '3в': 23,
    '4г': 21,
    '5а': 20,
    '6б': 19,
    '7в': 24,
    '8г': 22,
    '9а': 25,
    '10а': 24,
}

print(count_student('3в', school))
change_count_students('2б', 21, school)
change_count_students('5а', 23, school)
change_count_students('10а', 20, school)
add_school_classes('2в', 22, school)
add_school_classes('10б', 25, school)
delete_class('8г', school)
print(school)

# type_conversion. Задание 1
string_1 = 'Robin Singh'
string_2 = 'I love arrays they are my favorite'
print(str_to_arr(string_1))
print(str_to_arr(string_2))

# type_conversion. Задание 2
list_fio = ['Ivan', 'Ivanov']
city = 'Minsk'
country = 'Belarus'
print(greetings(list_fio, city, country))

# type_conversion. Задание 3
list_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(list_to_str(list_1))

# type_conversion. Задание 4
list_1 = ["стол", "стул", "кресло", "тумбочка", "кровать", "диван",
          "табуретка", "полка для обуви", "шкаф", "горка"]
new_value = "журнальный столик"
print(add_pop_list(new_value, list_1))

# type_conversion. Задание 5
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {}
print(merging_dictionaries(a, b, c))

# conditions. Задание 1
a = 10
print(number_operations(a))

# conditions. Задание 2
list_1 = [-3, 5, 7]
print(f"Количество положительных чисел: {number_of_positive_numbers(list_1)}")

# conditions. Задание 3
year = 2024
print(days_a_year(year))

# conditions. Задание 4
day_number = 3
print(name_of_day(day_number))

# conditions. Задание 5
unit_of_mass = 4
body_mass = 5
print(conversion_to_kilograms(unit_of_mass, body_mass))

# loop_for. Задание 1
a = 3
b = 9
print(f"Сумма целых чисел от {a} до {b} включительно: {sum_of_integers(a, b)}")

# loop_for. Задание 2
list_1 = [1, -3, 2, 2.2, 3, 4.1]
print(f"Сумма всех натуральных чисел: {sum_of_natural_numbers(list_1)}")

# loop_for. Задание 3
list_1 = [1, -2, -3, -4, 5, 6, 7, 8, 9, -10]
integer_operations(list_1)
print(f"Произведение положительных чисел: {integer_operations(list_1)[0]}")
print(f"Сумма отрицательных чисел: {integer_operations(list_1)[1]}")
print(f"Количество отрицательных чисел: {integer_operations(list_1)[2]}")

# loop_for. Задание 4
dict_1 = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}
print(best_result(dict_1))

# loop_for. Задание 5
# Реализовано ранее - # hw3. Задание 10

# loop_while. Задание 1
n = 10
print(f"Произведение всех чисел от 0 до {n} = {multiplication_of_numbers(n)}")

# loop_while. Задание 2
s_1 = 10
s_2 = 10
print(f"Через {calculation_of_years(s_1, s_2)} лет площадь первых сортов "
      f"будет составлять меньше 10% от площади вторых сортов")

# loop_while. Задание 3
n = 2222
print(f"Сумма цифр = {count_and_sum_number(n)[0]}\nКоличество цифр ="
      f" {count_and_sum_number(n)[1]}")

# loop_while. Задание 4
m = 30
n = 12
print(f"Дед станет вдвое старше внука через:{difference_calculation(m, n)[0]}")
print(f"Деду будет: {difference_calculation(m, n)[1]}")
print(f"Внуку будет: {difference_calculation(m, n)[2]}")
