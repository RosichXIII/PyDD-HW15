# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
from random import randint

logging.basicConfig(filename='Matrix.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:
    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Сложение матриц разной размерности невыполнимо:  [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')
        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])
            logger.info(f' Сложение:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr


    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(f'Умножение матриц разной размерности невыполнимо: [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            logger.info(f' Умножение:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            print("")
            # raise ValFormatError
            return
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            logger.info(f' Равенство:  {self._matr} = {other._matr} ')
            return True

    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':

    m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    m_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    m_3 = [[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]]
    m_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    print ("Cложение матриц:")
    print(Matrix(m_1) + Matrix(m_2))
    print(Matrix(m_3) + Matrix(m_1))

    print("Cравнение матриц:")
    print(Matrix(m_1) == Matrix(m_1))

    print("Умножение матриц:")
    print(Matrix(m_1) * Matrix(m_3))
    print(Matrix(m_1) * Matrix(m_4))