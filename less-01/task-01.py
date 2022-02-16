# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

one = 'раз'
two = 'два'
thre = 3
four = 4
five = 5.0

print(f'{one} {two} {thre} {four} {five} или так')
print('%s %s %03d %f %.2f' % (one,two,thre,four,five) )

ans = input("Привет! пообщаемся?(*/N) ") # проверяем только отрицательный ответ

while True:
    if ans.lower() == "n":
        print('Жаль :( ну пока')
        break
    print('Ура я "копм"')
    name = input("А как тебя зовут? ")

    while True: # можно и проверочку сделать как вариант
        try:
            num = int(input("Напиши целое число от 1 до 10: ")) # на целое не проверяем.
        except ValueError:
            print("Это не число, попробуйте снова.")
        else:
            break

    print('')
    even = 'не четное' if num % 2 else 'четное'
    print('Молодец {} ты ввел(а) число {} и оно {}'.format(name.title(),num,even))

    ans = input("Ещё разок?(*/N) ")
    print('-'*15)
    print('\n'*2)

