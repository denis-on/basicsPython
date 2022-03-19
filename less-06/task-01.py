# Создать класс TrafficLight (светофор).
#
#    определить у него один атрибут color (цвет) и метод running (запуск);
#    атрибут реализовать как приватный;
#    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#    проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    __color = {0: ['red', 7, '\033[91m'], 1: ['yellow', 2, '\33[6m\033[93m'], 2: ['green', 5, '\033[92m']}
    __dig = {'red': 0, 'yellow': 1, 'green': 2}
    __state = 0

    def __step(self, sleep_step=False):
        print(self.__color[self.__state][2] + self.__color[self.__state][0] + '\033[0m')
        if sleep_step:
            sleep(self.__color[self.__state][1])
        self.__state += 1
        if self.__state >= 3: self.__state = 0

    def running(self, state=None):
        if state is None:
            self.__step()
        else:
            st = self.__dig[state.lower()]
            while self.__state != st:
                self.__step(True)
            self.__step()

    def running_c(self, count):
        for _ in range(count*3+1):
            self.__step(True)



a = TrafficLight()

print('ручной режим типа next')
a.running()  # запустит 1 шаг за промежутками следим сами
sleep(1)
a.running()
sleep(1)
print('\nперевести в сотояние Красный(red) из текущего')
a.running('red')  # включит следующее состояние и будет преключаться до указаного
print('\nвыполним два полных круга от текущего')
a.running_c(2)  # выполнит полных 2 от текущего состояния
