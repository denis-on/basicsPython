# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):
    r = [first, second, third]
    r.remove(min(r))
    return sum(r)

print('сумма =',my_func(2, 2, 33))
