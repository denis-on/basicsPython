#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    try:
        one = input('введите число "n" от 0 до 9: ')
        num = int(str(one))
    except ValueError:
        print('Это не число, попробуйте снова.')
    else:
        if num > 9 or num < 0:  #в задании не оговариваеться сколько знаков
            print('неверно')    #ограничемся цифрами для наглядности и уберем отрицательные
            continue
        break

print('перевожу.......')
two = one+one
tree = one+one+one

print("n =",one," nn =",two," nnn =",tree)
print('Сумма чисел n + nn + nnn =',int(one)+int(two)+int(tree))