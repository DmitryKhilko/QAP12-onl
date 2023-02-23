# Задание 1
def number_operations(number: int):
    if number > 0:
        number += 1
    return number


# Задание 2
def number_of_positive_numbers(original_list: list):
    count_positive = 0
    for i in range(len(original_list)):
        if original_list[i] > 0:
            count_positive += 1
    return count_positive


# Задание 3
def days_a_year(year: int):
    if year % 4 != 0:
        return f"В {year} году 365 дней"
    elif year % 100 != 0:
        return f"В {year} году 366 дней"
    elif year % 400 != 0:
        return f"В {year} году 365 дней"
    else:
        return f"В {year} году 366 дней"


# Задание 4
def name_of_day(day_number: int):
    if day_number == 1:
        return "понедельник"
    elif day_number == 2:
        return "вторник"
    elif day_number == 3:
        return "среда"
    elif day_number == 4:
        return "четверг"
    elif day_number == 5:
        return "пятница"
    elif day_number == 6:
        return "суббота"
    elif day_number == 7:
        return "воскресенье"
    else:
        return "нет такого дня недели"


# Задание 5
def conversion_to_kilograms(unit_of_mass: int, body_mass: int):
    if unit_of_mass == 1:
        return f"Масса тела в килограммах: {body_mass}"
    elif unit_of_mass == 2:
        return f"Масса тела в миллиграммах: {body_mass * 1000000}"
    elif unit_of_mass == 3:
        return f"Масса тела в граммах: {body_mass * 1000}"
    elif unit_of_mass == 4:
        return f"Масса тела в тоннах: {body_mass / 1000}"
    elif unit_of_mass == 5:
        return f"Масса тела в центнерах: {body_mass / 100}"
    else:
        return f"В условиях задачи такой единицы массы не задано"
