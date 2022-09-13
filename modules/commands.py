from tabulate import tabulate


def terminal_commands():
    command = input('\nВведите команду: ')
    return command


def print_commands_list():
    # Список команд
    table_headers = [
        'Команда', 'Краткое описание', 'Функционал'
    ]

    table_data = [
        ['exit', 'Выход', 'Завершение работы программы'],
        ['add', 'Добавить друга', 'Создание нового друга в базе'],
    ]

    print(tabulate(table_data, table_headers))
