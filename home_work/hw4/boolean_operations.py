# Задание 1. Присвойте двум переменным любые числовые значения.
a = 3
b = 4

# Задание 2. Составьте четыре сложных логических выражения с помощью
# оператора and, два из которых должны давать истину, а два других - ложь.
if 2 < a < 5 and 3 < b <= 4:  # True
    print(True)
else:
    print(False)

if 0 < a < b and a < b < 10:  # True
    print(True)
else:
    print(False)

if b < a < a + 1 and 10 < b < 11:  # False
    print(True)
else:
    print(False)

if 0 < a < 2 and 10 < b < a:  # False
    print(True)
else:
    print(False)

# Задание 3. Составьте четыре сложных логических выражения с помощью
# оператора or, два из которых должны давать истину, а два других - ложь.
if a < b or b <= 4:  # True
    print(True)
else:
    print(False)

if 0 < a < b or a < b < 10:  # True
    print(True)
else:
    print(False)

if not (a < b or b <= 4):  # False
    print(True)
else:
    print(False)

if b < a or 10 < b <= 20:  # False
    print(True)
else:
    print(False)

# Задание 4. Попробуйте использовать в сложных логических выражениях
# работу с переменными строкового типа.
string_1 = 'Строка первая'
string_2 = 'Строка вторая'

if 0 < len(string_1) < 20 and string_2.find('вторая'):  # True
    print(True)
else:
    print(False)

if string_1 == string_2 or string_1 in string_2:  # False
    print(True)
else:
    print(False)
