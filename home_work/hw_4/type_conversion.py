# Задание 1. Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"],
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
print("Задание 1")

string_1 = 'Robin Singh'
list_1 = [string_1.split(" ")[0], string_1.split(" ")[1]]
print(list_1)

string_2 = 'I love arrays they are my favorite'
list_2 = []
for i in range(len(string_2.split(" "))):  # количество слов в строке
    list_2.append(string_2.split(" ")[i])
print(list_2)

# Задание 2. Дан список: [‘Ivan’, ‘Ivanov’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanov! Добро пожаловать в Minsk Belarus”
print("")
print("Задание 2")

list_fio = ['Ivan', 'Ivanov']
city = 'Minsk'
country = 'Belarus'
print("Привет,", list_fio[0], list_fio[1], "! Добро пожаловать в", city,
      country)

# Задание 3. Дан список,  сделайте из него строку.
print("")
print("Задание 3")

list_3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string_3 = ''
for i in range(len(list_3)):
    string_3 = string_3 + list_3[i] + ' '
print(string_3)

# Задание 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6
print("")
print("Задание 4")

list_4 = ["стол", "стул", "кресло", "тумбочка", "кровать", "диван",
          "табуретка", "полка для обуви", "шкаф", "горка"]
list_4.insert(2, "журнальный столик")
print(list_4)
list_4.pop(5)
print(list_4)

# Задание 5. Есть 2 словаря. Необходимо их объединить по ключам, а значения
# ключей поместить в список, если у одного словаря есть ключ "а", а у другого
# нет, то поставить значение None на соответствующую позицию(1-я позиция для
# 1-ого словаря, вторая для 2-ого) # ab = {'a': [1, None], 'b': [2, None],
# 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
print("")
print("Задание 5")

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {}

for key, value in a.items():
    if key in b:
        c[key] = [a[key], b[key]]
    else:
        c[key] = [value, None]

for key, value in b.items():
    if key in a:
        c[key] = [a[key], b[key]]
    else:
        c[key] = [None, value]

print(c)
