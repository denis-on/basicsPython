# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит
# не менее b километров.
# Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
#
def inputIntNum(message):
    n=-1
    while True:
        try:
            n = int(input(message + ' '))
        except ValueError:
            print('Это не число, попробуйте снова.')
        else:
            if n < 0:
                print('Введено отрицательное значение!')
                continue
            break
    return n
def print_day_km(day,km):
    print(f'{day:02d} день: {km:.2f} km')

def result_day(start, end, percent):
    day = 1
    dist = start
#    print_day_km(day, dist)
    while dist < end:
        dist *= (1 + percent)
        day += 1
#        print_day_km(day, dist)
    return day


print('Введите данные по спорцмену')
start_dist = inputIntNum('Результат пробежки в первый день, км:')
end_dist = inputIntNum('Цель спортсменна, км:')
percent = inputIntNum('Увеличение дистанции в %')/100.0

print(f'Результат будет достигнут на {result_day(start_dist,end_dist,percent)} день')