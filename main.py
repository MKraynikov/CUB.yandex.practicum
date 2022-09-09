# CUB - company users base
# Training project,  yandex.practicum, group-18
# Python v.1.0 2022-09-09

from faker import Faker
from tabulate import tabulate
from random import randrange
import random
import json

fake = Faker('ru_RU')

#TODO Перенести заполняемые переменные в начало программы

def init_data_sets():
    #Генерируем список пользователей
    #TODO добавить параметр для выбора количества генерируемых пользователей
    fake_users = {}

    for i in range(10):
        fake_users[i] = {
            'id': i + 1,
            'name': fake.name(),
            'city': fake.city(),
            'address': fake.address(),
            'job': fake.job(),
            'email': fake.ascii_email(),
            'age': randrange(21, 75),
            'balance': random.uniform(0.0, 1000000)
        }

    return fake_users


def print_exist_users(users):
    # Выводим на экран список пользователей
    # TODO добавить пароверку наличия ранее сгенерированных списков
    table_headers = [
        'ID', 'ФИО', 'Возраст', 'Город проживания'
    ]
    table_data = []
    for i in users:
        new_table_data = [
            users[i]['id'],
            users[i]['name'],
            users[i]['age'],
            users[i]['city']
        ]
        table_data.append(new_table_data)

    print(tabulate(table_data, table_headers))


def print_exist_user(user):
    # Выводим на экран данные пользователя
    # TODO добавить пароверку наличия ранее сгенерированного пользователя
    table_headers = [
        'Параметр', 'Значение'
    ]

    table_data = []
    for k, v in user.items():
        user_info = [k, v]
        table_data.append(user_info)

    print(tabulate(table_data, table_headers))


def print_commands_list():
    # Список комамнд
    # TODO подумать как их расшиирять более гибко
    table_headers = [
        'Команда', 'Краткое описание', 'Функционал'
    ]

    table_data = [
        ['exit', 'Выход', 'Завершение работы программы'],
        ['mode', 'Режим работы', 'Смена режима работы с данными в программе'],
        ['users', 'Пользователи', 'Вывод списка сгенерированных пользователей'],
        ['show {user_id}', 'Показать пользователя', 'Загружает данные пользователя по его ID'],
        ['store', 'Сохранить пользователей', 'Сохраняет текущий сгенерированный список пользователей в JSON'],
        ['load', 'Загрузить пользователей', 'Загружает список пользователей из JSON файла'],
    ]

    print(tabulate(table_data, table_headers))


def terminal_commands():
    command = input('\nВведите команду: ')
    return command


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

        #TODO Если выбран JSON не работает поиск по ID
        if main_command == 'show':
            print(f'Загружаем данные пользователя: {input_command[1]}')
            try:
                print_exist_user(users_data[int(input_command[1])-1])
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


