# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func_v1(x,y):
    if y == 0 : return 1
    elif y > 0:
        return x**y
    else:
        y = -y
        return 1/x**y

def my_func_v2(x,y):
    degr=1
    if y == 0:
        return degr
    elif y > 0:
        while y>=1:
            degr *= x
            y = y-1
        return degr
    else:
        y = -y
        while y>=1:
            degr *= x
            y = y-1
        return 1/degr

def inputIntNum(message):
    n=0
    while True:
        try:
            n = int(input(message + ' '))
        except ValueError:
            print('Это не число, попробуйте снова.')
            continue
        else:
            break
    return n

print('Решение задачи X в степени Y')
x = inputIntNum('X=')
y = inputIntNum('Y=')

print('Возведение в степень с помощью оператора **', my_func_v1(x,y))
print('без оператора **, с использованием цикла', my_func_v2(x,y))