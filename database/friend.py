import sqlite3

database = sqlite3.connect('database/students.db')


def store_new_friend(friend_info):
    cursor = database.cursor()

    try:
        query = """CREATE TABLE IF NOT EXISTS friends(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name CHAR(50) NOT NULL, 
                               city CHAR(50), 
                               description TEXT(500), 
                               steps INTEGER(10), 
                               calories REAL(20) )"""
        cursor.execute(query)

        columns = ', '.join(friend_info.keys())
        placeholders = ':' + ', :'.join(friend_info.keys())
        query = 'INSERT INTO friends (%s) VALUES (%s)' % (columns, placeholders)

        cursor.execute(query, friend_info)
        database.commit()

        new_friend_id = cursor.lastrowid
        print(f'Новый друг успешно добавлен в базу! Его ID: {new_friend_id}')
        return new_friend_id
    except:
        print('<Ошибка при добавлении друга в базу>')
        database.rollback()
