# CUB - company users base
# Training project,  yandex.practicum, group-18
# Python v.1.0 2022-09-09

import json
from modules.commands import *
from modules.users import *
from modules.data import *


# TODO Перенести заполняемые переменные в начало программы


def operation():
    global mode
    mode = True
    users_data = init_data_sets()

    while mode:
        print('Выберите режим работы:\n1. С сохраненными данными.\n2. Новая генерация.')
        command = int(input('Режим 1 или 2: '))
        if command == 1:
            with open('files/users.json') as users_base:
                users_data = json.load(users_base)

            print('Данные из файла загружены')
            mode = False
            break
        if command == 2:
            print('Данные для работы сгенерированы')
            mode = False
            break
        else:
            print('Допускается ввод числа 1 или 2.')

    active = True
    while active:
        input_command = terminal_commands().split(' ', 1)
        main_command = input_command[0]

        # TODO Если выбран JSON не работает поиск по ID
        if main_command == 'show':
            print(f'Загружаем данные пользователя: {input_command[1]}')
            try:
                print_exist_user(users_data[int(input_command[1]) - 1])
            except:
                print('Запрашиваемого пользователя нет в базе данных. Введите другой ID.')

        if main_command == 'store':
            with open('files/users.json', 'w') as users_base:
                json.dump(users_data, users_base)
                print('Данные успешно сохранены.')

        if main_command == 'load':
            with open('files/users.json') as users_base:
                data = json.load(users_base)
                print_exist_users(data)

        if main_command == 'help':
            print_commands_list()

        if main_command == 'users':
            print_exist_users(users_data)

        if main_command == 'mode':
            mode = True
            print('Запуск выбора режима работы.')

        if main_command == 'exit':
            exit()
        else:
            print(f'\n< Ожидание ввода следующей команды. Список команд: help >')


def run_process():
    print('База данных пользователей компании.')
    print('**********************************\n')
    operation()


run_process()
