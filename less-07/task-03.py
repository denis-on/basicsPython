# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    __count = 0

    def __init__(self, count):
        if count <= 0:
            raise ValueError("error count <=0")
        self.__count = count

    def make_order(self, len_row):
        res = ["*" * len_row] * (self.__count // len_row)
        if self.__count % len_row:
            res.append("*" * (self.__count % len_row))
        return "\n".join(res)

    def __str__(self):
        return f'{self.__count}'

    def __add__(self, other):
        if not (isinstance(other, Cell)):
            raise ValueError("error other class")
        return Cell(self.__count + other.__count)

    def __sub__(self, other):
        if not (isinstance(other, Cell)):
            raise ValueError("error other class")
        res = self.__count - other.__count
        if res > 0:
            return Cell(self.__count - other.__count)
        else:
            raise ValueError("error defference <=0")

    def __mul__(self, other):
        if not (isinstance(other, Cell)):
            raise ValueError("error other class")
        return Cell(self.__count * other.__count)

    def __floordiv__(self, other):
        if not (isinstance(other, Cell)):
            raise ValueError("error other class")
        #так как Cell иницилизируеться только целым положительным кол-вом ячеек то деления на ноль не будет
        #однако при self.__count < other.__count будет иницилизироваться класс нулевым кол-вом ячеек
        if (self.__count < other.__count):
            raise ValueError("error integer division return zero")
        else:
            return Cell(self.__count // other.__count)



cell_1 = Cell(12)
cell_2 = Cell(8)
print(cell_1.make_order(5))
try:
    print(f"+ -> {cell_1 + cell_2}")
    print(f"- -> {cell_1 - cell_2}")
    print(f"* -> {cell_1 * cell_2}")
    print(f"/ -> {cell_1 // cell_2}")
except ValueError as exp:
    print(exp)