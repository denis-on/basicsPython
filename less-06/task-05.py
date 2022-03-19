# Реализовать класс Stationery (канцелярская принадлежность).
#
#    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#    в каждом классе реализовать переопределение метода draw.
#    Для каждого класса метод должен выводить уникальное сообщение;
#    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
      self.title = "Pen"

    def draw(self):
        print('Попишем ручкой')

class Pencil(Stationery):
    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        print('Чертить карандашом')

class Handle(Stationery):
    def __init__(self):
        self.title = "Handle"

    def draw(self):
        print('Рисуем Маркером')


pen=Pen()
print(pen.title)
pencil=Pencil()
print(pencil.title)
handle=Handle()
print(handle.title)

pen.draw()
pencil.draw()
handle.draw()
