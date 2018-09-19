# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def open_file_and_find_keyword(file, input_string, local_list):
    with open(file, 'r') as current_file:
        for line in current_file:
            if input_string in line:
                print(file)
                local_list.append(file)
                break
    return local_list


def find_sql(list_of_files, input_string):
    local_list = []
    if len(list_of_files) == 0:
        for d, dirs, files in os.walk(os.path.join(current_dir, migrations)):  # Просматриваем каталог
            for file in files:  # идем по каждому файлу
                path = os.path.join(d, file)  # формирование полного пути файла
                if path.endswith('.sql'):
                    local_list = open_file_and_find_keyword(str(path), input_string, local_list)
    else:
        for file in list_of_files:
            local_list = open_file_and_find_keyword(file, input_string, local_list)

    print("Всего: ", len(local_list))
    return local_list


def start_func():
    local_list = []
    while True:
        key = input("Введите строку для поиска: ")
        local_list = find_sql(local_list, key)


if __name__ == '__main__':
    start_func()
