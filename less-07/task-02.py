# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
# костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
#

from abc import ABC, abstractmethod

class Clotnes(ABC):
    count_material = 0

    @abstractmethod
    def consum(self):
        pass

class Coat(Clotnes):
    def __init__(self, size):
        self.size = size
        Coat.count_material += self.consum  #  в родительский клас складывает все расходы ткани

    def __str__(self):
        return f'Пальто: размер {self.size}, требует ткани {self.consum:.2f}'

    @property
    def consum(self):
        return self.size / 6.5 + 0.5

class Costume(Clotnes):
    def __init__(self, height):
        self.height = height
        Costume.count_material += self.consum  #  в родительский клас складывает все расходы ткани

    def __str__(self):
        return f'Костюм: рост {self.height}, требует ткани {self.consum:.2f}'

    @property
    def consum(self):
        return 2*self.height + 0.3


coat_1 = Coat(36)
print(coat_1)
coat_2 = Coat(42)
print(coat_2)

costum_1 = Costume(140)
print(costum_1)
costum_2 = Costume(160)
print(costum_2)

print(f'Расход ткани на пальто составил {coat_1.count_material:.2f}')
print(f'Расход ткани на костюмы составил {costum_2.count_material:.2f}')
print(f'Общий расход ткани {coat_1.count_material+costum_2.count_material:.2f}')
