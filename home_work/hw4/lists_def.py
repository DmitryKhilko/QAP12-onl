# Задание 1 - 6
def list_operations(list_1: list, list_2: list):
    list_1.pop(1)
    list_2[len(list_2) - 1] = "8"
    list_3 = list_1 + list_2
    result = list_3[len(list_1) - 1:len(list_1) + 1]
    list_3.append("гитара")
    list_3.append("флейта")

    return list_2, result, list_3


# Задание 7
def intersection_of_many(list_1: list, list_2: list):
    return list(set(list_1) & set(list_2))


# Задание 8
def list_unique_values(original_list: list):
    return list(set(original_list))

# # Задание 8. Есть список. Оставить в нем только уникальные значения.
# # !не использовать циклы
# d = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
# d = list(set(d))
# print(d)
#
