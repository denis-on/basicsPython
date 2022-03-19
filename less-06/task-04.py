#Реализуйте базовый класс Car.
#
#    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
#    повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
#    свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
#к атрибутам, выведите результат. Вызовите методы и покажите результат.
from random import randint


class Car:
    numAvto = 0

    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_stop = True

    def getNewSpeed(self):
        self.speed = 0 if self.is_stop else randint(20,100)
        return self.speed

    def go(self):
        self.is_stop = False
        self.getNewSpeed()
        print(f'{self.name}: Начало движения')

    def stop(self):
        self.is_stop = True
        self.speed = 0
        print(f'{self.name}: Конец движения. Остановка')

    def turn(self, direction):
        print(f'{self.name}: Изменение направления на {direction}')

    def show_speed(self):
        print(f'{self.name}: текущая скорость {self.getNewSpeed()}')

class TownCar(Car):
    def __init__(self, color):
        TownCar.numAvto += 1
        super().__init__(color, "TownCar_"+str(TownCar.numAvto), False)

    def show_speed(self):
        print(f'{self.name}: текущая скорость {self.getNewSpeed()}')
        if self.speed > 60:
            print('Внимание'+''+'привышение скорости')

class SportCar(Car):
    def __init__(self, color):
        SportCar.numAvto += 1
        super().__init__(color, "SportCar_"+str(SportCar.numAvto), False)

class WorkCar(Car):
    def __init__(self, color):
        WorkCar.numAvto += 1
        super().__init__(color, "WorkCar_"+str(WorkCar.numAvto), False)

    def show_speed(self):
        print(f'{self.name}: текущая скорость {self.getNewSpeed()}')
        if self.speed > 40:
            print('\033[91m' + 'Внимание '+'\033[0m'+'привышение скорости')

class PoliceCar(Car):
    def __init__(self, color):
        PoliceCar.numAvto += 1
        super().__init__(color, "PoliceCar_"+str(PoliceCar.numAvto), True)




car_1 = PoliceCar('red')
car_2 = PoliceCar('green')
car_t = TownCar('yellow')
car_s = SportCar('while')
car_w = WorkCar('grey')

print(car_1.name,'цвет',car_1.color)
print(car_2.name,'цвет',car_2.color)
print(car_t.name,'цвет',car_t.color)
print(car_s.name,'цвет',car_s.color)
print(car_w.name,'цвет',car_w.color)

car_t.go()
car_s.go()
car_1.go()
car_w.go()
car_2.go()

# погоняем
print('\nпогоняем')
for _ in range(5):
    car_t.show_speed()
    car_s.show_speed()
    car_1.show_speed()
    car_w.show_speed()
    car_2.show_speed()
    print('')

car_t.stop()
car_s.stop()
car_1.stop()
car_w.stop()
car_2.stop()
car_t.show_speed()
car_s.show_speed()
car_1.show_speed()
car_w.show_speed()
car_2.show_speed()

