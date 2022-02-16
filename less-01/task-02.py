# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк
#
import datetime
import time

while True:
    try:
        sec_input = int(input("напиши время в секундах "))
    except ValueError:
        print("Это не число, попробуйте снова.")
    else:
        break
#sec_input = 123455
print('перевожу в часы минуты.......')

print('Есть встроиные библиотечные функции, например timedelta из datetime: ', end="")
print(datetime.timedelta(seconds=sec_input))
print('или с указанием формат как в задании через strftime из time: ', end="")
print(time.strftime("%H:%M:%S",time.gmtime(sec_input)))

print('Но можно читой математикой получить результат')
day = sec_input // (24 * 3600)
sec = sec_input % (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print("Количество дней:   ", day)
print("Количество часов:  ", hour)
print("Количество минут:  ", min)
print("Количество секунд: ", sec)
print('-'*30)
print(f'Рузультат в формате требующийся в задаче: {hour:02d}:{min:02d}:{sec:02d}')
if day > 0:
    print(f'но в таком случаи потеряем еще дни, а их: {day}')
print('-'*30)