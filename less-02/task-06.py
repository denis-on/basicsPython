# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

def my_str2int(str): # верним число если это возможно
    try:
        n_int=int(str)
    except ValueError:
        return str
    else:
        return n_int

def my_print_list(struct):
    print('[')
    for el in struct:
        print(el)
    print(']')
def my_print_dict(dict):
    print('{')
    for key in dict.keys():
            print(f"'{key}': {dict[key]},")
    print('}')

temp_struct = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

my_struct = []
my_dict={}

if False :   # Постывить True для отладки на temp_struct
    my_struct = temp_struct.copy()
    my_dict = {'название': [], 'цена': [], 'количество': [], 'eд': []}
else: # запросим у пользователя список полей (ключей) словаря
    i=1
    next = True
    str = input('Введите характеристиками товара через запятую:(def: название,цена,количество,единица измерения): \n')\
            or 'название,цена,количество,единица измерения'
    name_list = str.split(',')

    while next:
        str_dict = {}
        for itm in name_list:
            str_dict.update({itm : my_str2int(input(f'{itm}: '))})
            my_dict.update({itm : []})

        my_struct.append( (i,str_dict,) )
        next = False if input('Внести еще одну запись, (Y,n)' ).lower() == "n" else True
        i += 1

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.

print('\nЗаполненая структура:')
#print(my_struct)
my_print_list(my_struct)

for el_struct in my_struct:
    for key in el_struct[1].keys():
        if el_struct[1].get(key) not in my_dict[key]: # проверим повторяющиеся или можно было еще организовать через set
            my_dict[key].append(el_struct[1].get(key)) # но тут все равно перебор

print('\nАналитика:')
#print(my_dict)
my_print_dict(my_dict)


