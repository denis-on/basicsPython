# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

import os

n_str = 0
n_char = 0
file_name = 'task01.txt'

def get_string_user():
    global n_str
    global n_char
    m_str = input(f"{n_str+1:03}->>>")
    n_str += 1
    # количество символов с учетом перевода строк под Win используеться CR LF
    # а это 2 байта а вот под лин будет только что мы укажем "\n" - 1 байт (LF)
    lb = 2 if os.name == "nt" else 1
    n_char += len(m_str) + (lb if len(m_str) > 0 and n_str>1 else 0)
    return m_str

print('введите строки для записи в файл, окончание ввода пустая строка')
with open(file_name, "w", encoding='utf-8') as f_obj:
    user_str = get_string_user()
    while user_str != "":
        if n_str>1: f_obj.writelines("\n")
        f_obj.writelines(user_str)
        user_str = get_string_user()
f_size = os.path.getsize(file_name)
print('в фаил записано {} символов, {} строк, размер файла на диске {} байт'.format(n_char, n_str-1, f_size))
