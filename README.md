# :snake:Rest API на Python
Python REST API для управления пользователями.
## Содержание
- [Описание](#описание)
- [Пример работы программы](#примерработыпрограммы)
- [Технологии](#технологии)
- [Установка](#установка)
- [Автор](#автор)

## Описание
Проект реализован на Flask и представляет полноценный CRUD для работы с пользователями. Данные пользователей хранятся в базе данных PostgreSQL через SQLAlchemy, что обеспечивает удобное и безопасное взаимодействие с бд.
Все CRUD операции логируются (с указанием даны и времени) в отдельный файл. Данный API готов к интеграции с фронтендом или другими сервисами. Проверка работоспособности проводилась в Postman.

## Пример работы
- Получение списка всех пользователей
<img src="https://github.com/DmitryLkT/python_rest_api/blob/main/resources/static/images/get_all.jpg" 
     alt="getListUsers" width="600"/>

- Получение пользователя по id
  
  <img src="https://github.com/DmitryLkT/python_rest_api/blob/main/resources/static/images/get_one.jpg" 
     alt="getUsers" width="600"/>

- Добавление нового пользователя

     <img src="https://github.com/DmitryLkT/python_rest_api/blob/main/resources/static/images/post.jpg" 
     alt="postUsers" width="600"/>  

- Обновление существующего пользователя

  <img src="https://github.com/DmitryLkT/python_rest_api/blob/main/resources/static/images/put.jpg" 
     alt="putUsers" width="600"/>

- Удаление пользователя
 
    <img src="https://github.com/DmitryLkT/python_rest_api/blob/main/resources/static/images/delete.jpg" 
     alt="deleteUsers" width="600"/>

## Технологии
| Технология | Назначение |
| ----------- | ----------- |
| Python    | основной язык  |
| Flask  | фреймворк для создания сервера  |
| Flask-RESTful   | упрощает создание Rest API  |
| SQLAlchemy| ORM для работы с PostgreSQL |
| PostgreSQL     | основная база данных  |
| psycopg2   | драйвер для PostgreSQL  |
| Logging| логирование  |

## Установка
### Клонирование проекта 
```
git clone https://github.com/DmitryLkT/python_rest_api.git
cd python_rest_api
```
### Создание и активация вертуального окружения
```
python -m venv .venv
.\.venv\Scripts\activate
```
### Обновление pip
```
python -m pip install --upgrade pip
```
### Установка зависимостей
```
pip install -r requirements.txt
```
### Настройка базы PostgreSQL
```
CREATE TABLE users (
  id serial PRIMARY KEY,
  name varchar(20) NOT NULL,
  age int NOT NULL
)
```
### Настройка SQLAlchemy (data/userManager.py)
```
DATABASE_URL = "postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>"
```

### Запуск
```
python app.py
```
## Автор
Дмитрий Л.
- Почта: <Dmitry.plus1@yandex.ru>
- GitHub: [DmitryLkT](https://github.com/DmitryLkT)
