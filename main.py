# CUB - company users base
# Training project,  yandex.practicum, group-18
# Python v.1.0 2022-09-09

from modules.commands import *
from modules.friends import *


def operation():
    active = True
    while active:
        input_command = terminal_commands().split(' ', 1)
        main_command = input_command[0]

        if main_command == 'help':
            print_commands_list()
        if main_command == 'add':
            create_new_friend()
        if main_command == 'exit':
            exit()
        else:
            print(f'\n< Ожидание ввода следующей команды. Список команд: help >')


def run_process():
    print('Справочник моих друзей.')
    print('**********************************\n')
    operation()


run_process()
