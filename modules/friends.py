from database.friend import *


def create_new_friend():
    friend = {
        'name': input('Введите имя друга: '),
        'city': input('Введите город друга: '),
        'description': input('Введите описание для друга: '),
        'steps': 0,
        'calories': 0,
    }

    store_new_friend(friend)


def get_friend_info(friend_id):
    friend_info = {}

    ...

    return friend_info


def update_friend_info(friend_id, new_friend_info):
    new_friend_info = {}

    ...

    return new_friend_info


def delete_friend_info(friend_id):
    ...

    return '<Данные друга "имя друга" успешно удалены>'