# Задание 1. Свяжите переменную с любой строкой,
# состоящей не менее чем из 8 символов. Извлеките из
# строки первый символ, затем последний, третий с начала
# и третий с конца. Измерьте длину вашей строки.
print("Задание 1")

string_1 = "Не менее 8 символов"
print(string_1[0])
print(string_1[len(string_1) - 1])
print(string_1[2])
print(string_1[len(string_1) - 3])
print(len(string_1))

# Задание 2. Присвойте произвольную строку длиной 10-15
# символов переменной и извлеките из нее следующие срезы:
# первые восемь символов;
# четыре символа из центра строки;
# символы с индексами кратными трем;
# перевернуть строку
print("")
print("Задание 2")

string_2 = "абвгдеёжзийклм"
print(string_2[0:8])  # первые восемь символов
print(
    string_2[int(len(string_2) / 2 - 1):int(len(string_2) / 2 + 3)]
)  # четыре символа из центра строки
print(string_2[2: int(len(string_2)):3])  # символы с индексами кратными трем
print(string_2[::-1])  # перевернуть строку

# Задание 3. Есть строка: “my name is name”. Напечатайте ее,
# но вместо 2-го “name” вставьте ваше имя.
print("")
print("Задание 3")
string_3 = "my name is name"
print(string_3.replace("name", "Dmitry").replace("Dmitry", "name", 1))

# Задание 4. Есть строка: test_tring = "Hello world!", необходимо:
# напечатать на каком месте находится буква w;
# кол-во букв l;
# проверить начинается ли строка с подстроки: “Hello”;
# проверить заканчивается ли строка подстрокой: “qwe”
print("")
print("Задание 4")

test_tring = "Hello world!"
print(test_tring.find("w") + 1)
print(test_tring.count("l"))

if test_tring.find("Hello") == 0:
    print("Строка начинается с подстроки 'Hello'")

sub_str = "qwe"
if test_tring.find(sub_str, len(test_tring) - len(sub_str), len(test_tring)) != -1:
    print("Строка оканчивается на подстроку '", sub_str, "'")
else:
    print("Строка не оканчивается на подстроку '", sub_str, "'")
