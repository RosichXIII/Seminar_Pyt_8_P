# Задание 1.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
# который должен принимать данные (список списков) для формирования матрицы.
# [[], [], []]
# Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add()__ для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
# Пример:
# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3
# 4 5 6
# 7 8 9
# Сумма матриц:
# 2 4 6
# 8 10 12
# 14 16 18

class Matrix:

    def __init__(self, *numbers):
        self.new_matrix = list(numbers)
    
    def __str__(self):
        view_matrix = '\n'.join(map(str, self.new_matrix)).replace('[', '').replace(',', '').replace(']', '')
        return view_matrix
    
    def __add__(self, other):
        matrix_product = []
        for i in range(len(self.new_matrix)):
            matrix_product.append([])
            for j in range(len(self.new_matrix[i])):
                matrix_product[i].append(self.new_matrix[i][j] + other.new_matrix[i][j])
        view_matrix_product = '\n'.join(map(str, matrix_product)).replace('[', '').replace(',', '').replace(']', '')
        return view_matrix_product

matrix_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix_2 = Matrix([11, 12, 13], [14, 55, 16], [17, 18, 19])

print(f'Матрица №1:\n{matrix_1}\n')
print(f'Матрица №2:\n{matrix_2}\n')
print(f'Сумма матриц:\n{matrix_1 + matrix_2}')
