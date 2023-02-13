print('Задание 1.1')
name = "John Snow"
age = 29
print(name)

print('')
print('Задание 1.2')
print(type(3), ': 3')  # Numbers (Int) (числа)
print(type(3.2), ': 3.2')  # Numbers (Float) (числа)
print(type('Python'), ': Python')  # Strings (строки)
print(type([1, 2, 3]), ': [1, 2, 3]')  # Lists (списки)
print(type({'first': 1, 'second': 2}), ': {''first'': 1, ''second'': 2}')  # Dictionaries (словари)
print(type((1, 2, 3)), ': (1, 2, 3)')  # Tuples (кортежи)
print(type({'a', 'b', 'c', 'd'}), ': {''a'', ''b'', ''c'', ''d''}')  # Sets (множества)
print(type(bool(3)), ': bool(3)')  # Boolean (логический тип данных)

print('')
print('Задание 1.3')
print('17 / 2 * 3 + 2 =', 17 / 2 * 3 + 2)
print('2 + 17 / 2 * 3 =', 2 + 17 / 2 * 3)
print('19 % 4 + 15 / 2 * 3 =', 19 % 4 + 15 / 2 * 3)
print('(15 + 6) - 10 * 4 =', (15 + 6) - 10 * 4)
print('17 / 2 % 2 * 3 ** 3 =', 17 / 2 % 2 * 3 ** 3)

print('')
print('Задание 1.4')
age_1 = 49
age_2 = 50
age_3 = 23
summ_age = age_1 + age_2 + age_3
print('Суммарный возраст соседей:', summ_age)
average_age = summ_age // 3
print('Средний возраст соседей:', average_age)