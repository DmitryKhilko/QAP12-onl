# Задание 1
def str_to_arr(string: str) -> list:
    return string.split()


# Задание 2
def greetings(name: list, city: str, country: str):
    grt = f"Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}"
    return grt


# Задание 3
def list_to_str(original_list: list):
    return " ".join(original_list)


# Задание 4
def add_pop_list(value: str, original_list: list):
    original_list.insert(2, value)
    original_list.pop(5)
    return original_list


# Задание 5
def merging_dictionaries(dict_1: dict, dict_2: dict, result_dict: dict):
    for key, value in dict_1.items():
        if key in dict_2:
            result_dict[key] = [dict_1[key], dict_2[key]]
        else:
            result_dict[key] = [value, None]

    for key, value in dict_2.items():
        if key in dict_1:
            result_dict[key] = [dict_1[key], dict_2[key]]
        else:
            result_dict[key] = [None, value]

    return result_dict




# # Задание 5. Есть 2 словаря. Необходимо их объединить по ключам, а значения
# # ключей поместить в список, если у одного словаря есть ключ "а", а у другого
# # нет, то поставить значение None на соответствующую позицию(1-я позиция для
# # 1-ого словаря, вторая для 2-ого) # ab = {'a': [1, None], 'b': [2, None],
# # 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
# print("")
# print("Задание 5")
#
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'c': 3, 'd': 4, 'e': 5}
# c = {}
#
# for key, value in a.items():
#     if key in b:
#         c[key] = [a[key], b[key]]
#     else:
#         c[key] = [value, None]
#
# for key, value in b.items():
#     if key in a:
#         c[key] = [a[key], b[key]]
#     else:
#         c[key] = [None, value]
#
# print(c)
