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
                           bool_or_3, bool_or_4)


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

# dictionaries. Задание 1
# dictionaries. Задание 2
# dictionaries. Задание 3

# type_conversion. Задание 1
# type_conversion. Задание 2
# type_conversion. Задание 3
# type_conversion. Задание 4
# type_conversion. Задание 5

# conditions. Задание 1
# conditions. Задание 2
# conditions. Задание 3
# conditions. Задание 4
# conditions. Задание 5

# loop_for. Задание 1
# loop_for. Задание 2
# loop_for. Задание 3
# loop_for. Задание 4
# loop_for. Задание 5

# loop_while. Задание 1
# loop_while. Задание 2
# loop_while. Задание 3
# loop_while. Задание 4
