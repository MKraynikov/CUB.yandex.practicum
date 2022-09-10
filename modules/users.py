from tabulate import tabulate


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