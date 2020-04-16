"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы
(строка на столбец).
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add () для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    def __init__(self, lists):
        self.data = lists
        self._width = len(self.data[0])
        self._height = len(self.data)
        self.name = str(self._width) + 'x' + str(self._height)

    def __str__(self):
        bottom = ''
        maxlen = len(str(max([l for lst in self.data for l in lst])))
        top = '\n' + u'\u250C' + u'\u2500' * maxlen + (u'\u252C' + u'\u2500' * maxlen) * (
                    self._width - 1) + u'\u2510' + '\n'
        for i, j in enumerate(self.data):
            item = map(lambda x: str(x) if len(str(x)) == maxlen else ' ' * (maxlen - len(str(x))) + str(x), j)
            bottom = bottom + u'\u2502' + u'\u2502'.join(item) + u'\u2502' + '\n'
            if i != len(self.data) - 1:
                bottom = bottom + u'\u251C' + u'\u2500' * maxlen + (u'\u253C' + u'\u2500' * maxlen) * (
                        self._width - 1) + u'\u2524' + '\n'
            else:
                bottom = bottom + u'\u2514' + u'\u2500' * maxlen + (u'\u2534' + u'\u2500' * maxlen) * (
                        self._width - 1) + u'\u2518' + '\n'
        return top + bottom

    def __add__(self, other):
        result = []
        rowres = []
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                res = val + other.data[i][j]
                rowres.append(res)
            result.append(rowres)
            rowres = []
        return Matrix(result)


# ЗАГРУЖАЕМ МАТРИЦЫ -- КЛАДЕМ ЛИСТЫ СТРОК В ЛИСТ МАТРИЦЫ
m_3_2 = [[31, 22], [37, 43], [51, 861]]
m_3_3 = [[3, 5, 32], [2, 4, 6], [-1, 643, -8]]
m_4_2 = [[3, 5, 8, 3], [8, 3, 7, 1]]

# СОЗДАЕМ ЭКЗЕМПЛЯРЫ КЛАССА MATRIX
m_3_2 = Matrix(m_3_2)
m_3_3 = Matrix(m_3_3)
m_4_2 = Matrix(m_4_2)

print('Смотрим загруженные матрицы в привычном (табличном) виде:')
print(m_3_2)
print(m_3_3)
print(m_4_2)
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# СЛОЖИМ 2 ОДНОРАЗМЕРНЫЕ РАНДОМНЫЕ МАТРИЦЫ
m_6_6_1 = Matrix([[random.randint(1, 999) for i in range(6)] for j in range(6)])
m_6_6_2 = Matrix([[random.randint(1, 99) for i in range(6)] for j in range(6)])
print(f'Складываем матрицы размерностью {m_6_6_1.name} и {m_6_6_1.name}:')
res = m_6_6_1 + m_6_6_2
print(m_6_6_1, '+', m_6_6_2, '=', res)
