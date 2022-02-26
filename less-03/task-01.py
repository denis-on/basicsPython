# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def inputIntNum(message):
    n=0
    while True:
        try:
            n = float(input(message + ' '))
        except ValueError:
            print('Это не число или используйте "." для разделения разрядов, попробуйте снова.')
            continue
        else:
            break
    return n

def my_div(a,b):
    c=None
    try:
        c = a/b
    except ZeroDivisionError:
        print('Деление на ноль')
    return c

print('Введите 2 числа, опробуем диление a/b')
print(f"Результат деление a/b = { my_div(inputIntNum('Число а?'), inputIntNum('Число b?')) }")

