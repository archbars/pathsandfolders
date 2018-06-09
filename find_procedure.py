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


def find_sql(list_of_files, input_string):
    local_list = []
    if len(list_of_files) == 0:

        for d, dirs, files in os.walk(os.path.join(current_dir,migrations):  # Просматриваем каталог
            for file in files:  # идем по каждому файлу
                path = os.path.join(d, file)  # формирование полного пути файла
                if file.find('.sql') != -1:
                    current_file = open(str(path), 'r')
                    for line in current_file:
                        if line.find(input_string) != -1:
                            print(path)
                            local_list.append(path)
                            break  # после нахождения выходим из цикла по файлу
    else:
        for i in range(len(list_of_files)):
            current_file=open(list_of_files[i],'r')
            for line in current_file:
                if line.find(input_string) != -1:
                    print(list_of_files[i])
                    local_list.append(list_of_files[i])
                    break
    print("Всего: ", len(local_list))
    return local_list


def start_func():
    i = 1  # для организации бесконечного цикла
    local_list = []
    while i == 1:
        key = input("Введите строку для поиска: ")
        local_list = find_sql(local_list,key)


if __name__ == '__main__':
    start_func()
    pass
