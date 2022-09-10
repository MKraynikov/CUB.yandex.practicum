# Техническое задание

В данном документе будем определять функционал, который нам необходимо реализовать. 
Писать список и описание требуемых модулей. Распределять зоны ответственности - кто за что отвечает.

Актуальный список задач
* Модуль учета друзей
* Модуль хранения информации о друге
* Модуль получения данных о погоде
* Модуль расчета фитнес-трекера

## Описание модулей

### Базовые соглашения

В файле **main.py** храниться основная структура проекта
<!-- termynal -->

```
main.py
```

В каталоге **modules** хранятся все модули проекта
<!-- termynal -->

```
modules
```

В каталоге **database** хранятся все процедуры обращения к базе данных
<!-- termynal -->

```
database
```


### Описание модулей

Модуль учета друзей, список основных функций
```python
# создаем нового друга
def create_new_friend():
    friend = {}
    
    ...

    return friend
```

```python
# получаем данные друга
def get_friend_info(friend_id):
    friend_info = {}
    
    ...

    return friend_info
```

```python
# редактируем данные друга
def update_friend_info(friend_id, new_friend_info):
    new_friend_info = {}
    
    ...

    return new_friend_info
```

```python
def delete_friend_info(friend_id):
    
    ...

    return '<Данные друга "имя друга" успешно удалены>'
```

Модуль хранения информации о друге, список основных функций
```python
def store_friend_info(friend_id, friend_info):
    friend_info_object = {
        'var1' : '',
        'var2' : '',
        ...
        
        'var N+1': '',
    }
    ...

    return '<Информация о друге "имя друга" успешно сохранена>'

def store_friend_steps(friend_id, friend_steps):
    friend_steps_object = {
        'var1' : '',
        'var2' : '',
        ...
        
        'var N+1': '',
    }
    ...

    return '<Данные о шагах "имя друга" успешно сохранены>'

def store_friend_calories(friend_id, friend_calories):
    friend_calories_object = {
        'var1' : '',
        'var2' : '',
        ...
        
        'var N+1': '',
    }
    ...

    return '<Данные о калориях "имя друга" успешно сохранены>'
```

Модуль получения данных о погоде, список основных функций
```python
def get_friend_weather(friend_id):
    weather_in_city = {}

    return weather_in_city
```

Модуль расчета фитнес-трекера, список основных функций
```python
def get_friend_weather(friend_id):
    calculate_data = {
        'total_steps': 0,
        'total_calories': 0,
        'total_films': 0,
    }

    return calculate_data
```