# Задание 1 - 3
def count_student(number_of_class: str, school: dict):
    return school[number_of_class]


def change_count_students(number_of_class: str, count_students: int,
                          school: dict):
    class_count = school[number_of_class] = count_students
    return class_count


def add_school_classes(number_of_class: str, count_students: int,
                       school: dict):
    new_class = school[number_of_class] = count_students
    return new_class


def delete_class(number_of_class: str, school: dict):
    return school.pop(number_of_class)
