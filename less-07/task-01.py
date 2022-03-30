# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix():
    """Клас для работы с матрицами в ячейках которых целые числа"""
    def __init__(self,data):
        self.m = data

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.m])

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError('Для сложения необходимы равные по размеру матрицы')
            #return Matrix([[0]])  # без raise
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.m, other.m)))

    @property
    def size(self):
        return (len(self.m), len(self.m[0]))


my_list_1=[[1,0,0],[0,1,0],[0,0,1]] # еденичная матрица
my_list_2 = [[2,2,2],[1,1,1]]
m_1 = Matrix(my_list_1)
m_2 = Matrix(my_list_1)
sum_m = m_1 + m_2
sum_m_2 = Matrix(my_list_2)+Matrix(my_list_2) # сложение матриц не квадратных

print(m_1)
print(m_1.size)

print(sum_m)
print(sum_m.size)

print(sum_m_2)
print(sum_m_2.size)

try:
    sum_m_3 = Matrix(my_list_1) + Matrix(my_list_2)  # сложение матриц разного размера

except ValueError as exp:
    print(exp)
else:
    print(sum_m_3)
    print(sum_m_3.size)
