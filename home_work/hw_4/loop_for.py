# Задание 1. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.
print("Задание 1")

a = 3
b = 9
sum_numbers = 0

for i in range(a, b + 1):
    sum_numbers += i

print(f"Сумма всех целых чисел от {a} до {b} включительно: {sum_numbers}")

# Задание 2. Найти сумму всех натуральных чисел от A до B
print()
print("Задание 2")

list_1 = [1, -3, 2, 2.2, 3, 4.1]
sum_numbers = 0

for i in range(len(list_1)):
    if list_1[i] > 0 and not isinstance(list_1[i], float):
        sum_numbers += list_1[i]

print(f"Сумма всех натуральных чисел: {sum_numbers}")

# Задание 3. Найти произведение положительных, сумму и количество
# отрицательных из 10 введенных целых значений
print()
print("Задание 3")

list_1 = [1, -2, -3, -4, 5, 6, 7, 8, 9, -10]

multiplication_of_positive_num = 1
sum_of_negative_num = 0
count_of_negative_num = 0

for i in range(len(list_1)):
    if list_1[i] > 0:
        multiplication_of_positive_num *= list_1[i]
    else:
        sum_of_negative_num += list_1[i]
        count_of_negative_num += 1

print(f"Произведение положительных чисел: {multiplication_of_positive_num}")
print(f"Сумма отрицательных чисел: {sum_of_negative_num}")
print(f"Количество отрицательных чисел: {count_of_negative_num}")

# Задание 4. Дан словарь пловцов с их результатами.
# Напечатать лучший результат заплыва среди 6 участников

print()
print("Задание 4")

dict_1 = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}

for key, value in dict_1.items():
    if value == max(dict_1.values()):
        print(f"Лучший результат заплыва: {key} - {max(dict_1.values())}")

# Задание 5. Есть массив чисел. Известно, что каждое число в этом массиве
# имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число

print()
print("Задание 5")

list_1 = [1, 2, 1, 9, 2, 9, 5]

for i in range(len(list_1)):
    if list_1.count(list_1[i]) == 1:
        print(f"Уникальное число списка: {list_1[i]}")
