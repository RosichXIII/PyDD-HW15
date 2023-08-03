import argparse
from matrix import Matrix
from conv_to_matrix import convert_to_matrix

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-m_1',  type = list, action='append', default = [['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2',  type = list, action='append', default = [['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']]  )
    parser.add_argument('-operation', type=str, default='+')

    args = parser.parse_args()

    m_1 = convert_to_matrix(args.m_1)
    m_2 = convert_to_matrix(args.m_2)

    if args.operation == '+':
        print(f'СЛОЖЕНИЕ: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif  args.operation == '*':
        print(f'УМНОЖЕНИЕ: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'РАВЕНСТВО: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Такая операция {args.operation} над матрицами не предусмотрена!')

    # Вызов из командной строки:
    # python matrix_cmd.py
    # python Homework/Seminar_15/Matrix_terminal.py -m_1='123 456 789' -m_2='123 456 789'
    # python Homework/Seminar_15/Matrix_terminal.py -m_1='987 654 321' -m_2='123 456 789' -operation='='
    # python Homework/Seminar_15/Matrix_terminal.py -m_1='123 456 789' -m_2='9876 5432' -operation='*'