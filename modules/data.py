import random
from faker import Faker
from random import randrange

fake = Faker('ru_RU')


def init_data_sets():
    # Генерируем список пользователей
    # TODO добавить параметр для выбора количества генерируемых пользователей
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
