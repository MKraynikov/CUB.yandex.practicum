from tabulate import tabulate


def terminal_commands():
    command = input('\nВведите команду: ')
    return command


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
