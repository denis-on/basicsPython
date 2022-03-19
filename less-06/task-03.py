# Реализовать базовый класс Worker (работник).
#
#    определить атрибуты: name, surname, position (должность), income (доход);
#    последний атрибут должен быть защищённым и ссылаться на словарь,
#    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#    создать класс Position (должность) на базе класса Worker;
#    в классе Position реализовать методы получения полного имени
#    сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#    проверить работу примера на реальных данных: создать экземпляры класса
#    Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surmane, position, income):
        self._name = name
        self._surname = surmane
        self._position = position
        self.__income = income

class Position(Worker):
    def __init__(self, name, surmane, position, income):
        super().__init__(name, surmane, position, income)

    def get_full_name(self):
        return self._name+" "+self._surname

    def get_total_income(self):
        return (self._Worker__income)["wage"] + (self._Worker__income)["bonus"]


user1=Position('имя1','фамилия1', 'должность1',{"wage": 24, "bonus": -3})
user2=Position('имя2','фамилия2', 'должность2',{"wage": 12, "bonus": 2})

print(user1.get_full_name())
print(user1.get_total_income())

print(user2.get_full_name())
print(user2.get_total_income())
