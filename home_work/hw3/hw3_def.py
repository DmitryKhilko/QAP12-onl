# Задание 1
def convert_to_int(number: float) -> int:
    """
       Задание 1. Привести к целому типу -1.6, 2.99
       :param number: исходное число, которое необходимо привести к integer
       :return: преобразование float в int
       """
    return int(number)


# Задание 2
def replace_char_in_str(string: str, symbol_old: str, symbol_new: str) -> str:
    """
    Замена в строке одного символа на другой
    :param string: исходная текстовая строка
    :param symbol_old: заменяемый символ
    :param symbol_new: символ замены
    :return: функция замены символа в строке
    """
    return string.replace(symbol_old, symbol_new)


# Задание 3
def add_to_string(string: str, string_to_be_added: str) -> str:
    """
    Добавление в конец строки дополнительной строки
    :type string_to_be_added: str
    :param string: исходная строка
    :param string_to_be_added: добавляемая строка
    :return: соединение строк
    """
    return string + string_to_be_added


# Задание 4
def changing_position_words(string: str) -> str:
    """
    Изменение положения слов в строке из 2-х слов
    :param string: исходная строка
    :return: вывод строки с измененным порядком слов
    """
    return string.split(" ")[1] + " " + string.split(" ")[0]


# Задание 5. Напишите программу, которая удаляет пробел в начале и конце строки
""" Чек-лист для проверки функции:
1. Удаление начальных и конечных пробелов для строки с начальным, внутренними
и конечным пробелом. Ожидаемый результат: выведена строка без начального и  
конечного пробелов; внутренние пробелы остались.
2. Удаление начальных и конечных пробелов для строки с начальным и внутренними 
пробелами. Ожидаемый результат: выведена строка без начального и конечного 
пробелов; внутренние пробелы остались.
3. Удаление начальных и конечных пробелов для строки с внутренними и конечным 
пробелами. Ожидаемый результат: выведена строка без начального и конечного 
пробелов; внутренние пробелы остались.
4. Удаление начальных и конечных пробелов для строки с внутренними пробелами. 
Ожидаемый результат: выведена строка без начального и конечного пробелов; 
внутренние пробелы остались.
5. Удаление начальных и конечных пробелов для пустой строки. Ожидаемый 
результат: выведено сообщение, что строка пустая.
"""


def remove_begin_and_end_spaces(string: str) -> str:
    """
    Удаление пробелов в начале и конце строки
    :type string: basestring
    :param string: строка с начальными и конечными пробелами
    :return: строка без начальных и конечных пробелов
    """
    return string.strip()


# Задание 6
def add_class(name: dict, class_with_letter: str, students: int) -> dict:
    """
    Добавление в школу очередного ученического класса
    :type name: dict
    :type class_with_letter: str
    :param name: имя словаря
    :param class_with_letter: ученический класс
    :param students: количество учеников в классе
    :return: вывод словаря с добавленной новой записью
    """
    name[class_with_letter] = students  # Добавление в словарь новой записи
    return name


# Задание 7
def extracting_element_from_list(user_list: list, element_number: int):
    """
    Извлечение из списка n-го элемента
    :param user_list: пользовательский список
    :param element_number: номер извлекаемого элемента
    :return: отображение искомого элемента списка
    """
    if element_number <= len(user_list):
        return user_list[element_number]
    else:
        return (f"Номер запрашиваемого элемента списка '{element_number}' "
                f"больше количества элементов списка")


# Задание 8
def string_occurrence(original_string: str, search_string: str) -> bool:
    if original_string.find(search_string) == -1:
        return False
    else:
        return True


# Задание 9.1
def char_output_1(string: str, index: int) -> str:
    return string[index]


# Задание 9.2
def char_output_2(string: str, start: int, stop: int, step: int) -> str:
    return string[start:stop:step]


# Задание 10
def unique_number(given_array: list):
    for i in range(len(given_array)):
        if given_array.count(given_array[i]) == 1:
            return given_array[i]
