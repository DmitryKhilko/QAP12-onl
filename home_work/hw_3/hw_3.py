# Задание 1. Привести к целому типу -1.6, 2.99
print("Задание 1")

number_1 = -1.6
number_2 = 2.99
print("Исходное число", number_1, "; целое число: ", int(number_1))
print("Исходное число", number_2, "; целое число: ", int(number_2))

# Задание 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
print("")
print("Задание 2")

string_old = "www.my_site.com#about"
symbol_old = "#"
symbol_new = "/"
string_new = string_old.replace(symbol_old, symbol_new)
print(
    "Необходимо заменить символ '",
    symbol_old,
    "' на символ '",
    symbol_new,
    "' в строке '",
    string_old,
    "'",
)
print("Измененная строка", string_new)

# Задание 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
print("")
print("Задание 3")

string_1 = "stroka"
string_2 = "ing"
print("Необходимо соединить две строки: '", string_1, "', '", string_2, "'")
print("Результат соединения строк: ", string_1 + string_2)

# Задание 4. В строке “Ivanov Ivan” поменяйте местами слова => "Ivan Ivanov"
print("")
print("Задание 4")

fio_old = "Ivanov Ivan"
fio_new = fio_old.split(" ")[1] + " " + fio_old.split(" ")[0]
print("Необходимо поменять местами слова в строке '", fio_old, "'")
print("Результат: ", fio_new)

# Задание 5. Напишите программу, которая удаляет пробел в начале и конце строки
print("")
print("Задание 5")

string_old = " Мама мыла мылом раму "
string_new = string_old.strip()
print("Оригинальная строка:", string_old)
print("Строка без начальных и конечных пробелов:", string_new)

# Задание 6. Создайте словарь, связав его с переменной school,
# и наполните его данными, # которые бы отражали количество
# учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
print("")
print("Задание 6")

school = {
    "1a": 20,
    "1б": 18,
    "1в": 23,
    "1г": 21,
    "2а": 20,
    "2б": 19,
    "2в": 24,
    "2г": 22,
    "3а": 25,
    "3б": 24,
}
print("Количество учащихся в школе в разрезе классов: ", school)

# Задание 7. Создайте список и извлеките из него списка второй элемент
print("")
print("Задание 7")

list_1 = ["стол", "стул", "кровать", "шкаф"]
print("Второй элемент списка ", list_1, " - ", list_1[1])

# Задание 8. Вывести входит ли строка1 в строку2 (пример: employ и employment)
print("")
print("Задание 8")

string_1 = "employ"
string_2 = "employment"
if string_2.find(string_1) != -1:
    print("Строка '", string_1, "' входит в строку '", string_2, "'")
else:
    print("Строка '", string_1, "' не входит в строку '", string_2, "'")

# Задание 9. Вывести нужные символы из строки "My name is Agent Smith"
print("")
print("Задание 9")

x = "My name is Agent Smith"
print(x[1])  # y
print(x[3:16:3])  # nesgt

# Задание 10. Есть массив чисел. Известно, что каждое число в этом массиве
# имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число.
print("")
print("Задание 10")

list_1 = [1, 5, 2, 9, 2, 9, 1]

for i in range(len(list_1)):
    if list_1.count(list_1[i]) == 1:
        print("Уникальное число списка: ", list_1[i])
