# Задание 1. Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного файла.
# Если чисел меньше 3 выводить ошибку
def output_from_file(file: str) -> str:
    '''
    Дан файл целых чисел, содержащий не менее четырех элементов.
    Вывести первый, второй, предпоследний и последний элементы данного файла.
    Если чисел меньше 3 выводить ошибку.
    :param file: Имя файла с целыми числами
    :return: Вывод первого, второго, предпоследнего и последнего элементов
    '''
    try:
        with open(file, 'r') as f:
            sting: str = f.readline()
            if len(sting) < 3:
                return 'Ошибка: в файле меньше 3-х чисел'
            else:
                return f'Вывод первого, второго, предпоследнего и ' \
                       f'последнего элементов файла "{file}": {sting[0]}, ' \
                       f'{sting[1]}, {sting[-2]}, {sting[-1]}'
    except FileNotFoundError:
        print('Файл не найден')


# Задание 2. Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные
# (в том же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить пустым.
def even_and_odd_numbers(file: str) -> str:
    '''
    Дан файл целых чисел. Создать два новых файла, первый из которых содержит
    четные числа из исходного файла, а второй — нечетные (в том же порядке).
    Если четные или нечетные числа в исходном файле отсутствуют, то
    соответствующий результирующий файл оставить пустым.
    :param file: Имя файла с целыми числами
    :return: Два файла с четными и нечетными числами
    '''
    even = []
    odd = []
    with open(file, 'r') as f:
        sting: str = f.readline()
        for i in range(len(sting)):
            if int(sting[i]) % 2 == 0:
                even.append(sting[i])
            else:
                odd.append(sting[i])

        with open('C:/Users/dmitr/PycharmProjects/'
                  'QAP12-onl/home_work/hw6/even.txt', 'w') as f1:
            if even:
                for i in even:
                    f1.write(i)

        with open('C:/Users/dmitr/PycharmProjects/'
                  'QAP12-onl/home_work/hw6/odd.txt', 'w') as f2:
            if odd:
                for i in odd:
                    f2.write(i)

        with open('C:/Users/dmitr/PycharmProjects/'
                  'QAP12-onl/home_work/hw6/even.txt', 'r') as f3:
            even = f3.readline()
        with open('C:/Users/dmitr/PycharmProjects/'
                  'QAP12-onl/home_work/hw6/odd.txt', 'r') as f4:
            odd = f4.readline()

    return f'Содержимое файла с четными числами: {even}\n' \
           f'Содержимое файла с нечетными числами: {odd}'


# Задание 3. Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты. Вещественные числа — это числа, у которых есть дробная часть
# (она может быть нулевой). Они могут быть положительными или отрицательными.
def squares_of_real_numbers(file: str) -> str:
    '''
    Дан файл вещественных чисел.
    Заменить в нем все элементы на их квадраты.
    :param file: Имя файла с вещественными числами
    :return: Файл, с заменными элементами на их квадраты
    '''
    with open(file, "r") as f:
        # f.readline().split(" ") - создаем список, разбивая файл по пробелу
        list_squares = [str(float(n) ** 2) for n in f.readline().split(" ")]

    with open(file, "w") as f:
        f.writelines(" ".join(list_squares))
        return f'Возведенные в квадрат вещественные числа: {list_squares}'


# Задание 4. Даны два файла произвольного типа. Поменять местами их содержимое.
# Файлы должны быть бинарного типа




