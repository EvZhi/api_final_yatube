## Проект «API для Yatube»

API для Yatube представляет собой проект социальной сети, в котором возможно обрабатывать запросы к постам, группам, комментариям.

## Что мы использовали в проекте:

Python, Django, DRF, JWT + Djoser

## Установка:

Клонировать репозиторий и перейти в него в командной строке:
 `git clone `

cd yatube_api
Cоздать и активировать виртуальное окружение: 

python3 -m venv venv
Если у вас Linux/macOS
source venv/bin/activate
Если у вас windows
source venv/scripts/activate
python3 -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver
This is an image По умолчанию для неавторизованных пользователей проект доступен только для чтения.

GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
За исключением эндпоинта follow, доступен только авторизованных пользователей.

api/v1/follow/ - получение подписок текущего пользователя
api/v1/follow/{id}/ - получение одной подписки
Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.

POST /api/v1/posts/ - создание публикации
в body { "text": "string", "image": "string", "group": 0 }

PUT /api/v1/posts/{id}/ - обновление публикации
в body { "text": "string", "image": "string", "group": 0 }

PATCH /api/v1/posts/{id}/ - частичное обновление публикации
в body { "text": "string", "image": "string", "group": 0 }

DEL /api/v1/posts/{id}/ - удаление публикации
Добавить группу в проект нужно через админ панель Django:
admin/ - после авторизации, переходим в раздел Groups и создаем группы
Доступ авторизованным пользователем доступен по JWT-токену

POST /api/v1/jwt/create/ - получение токена

{
"username": "string",
"password": "string"
}

POST /api/v1/jwt/refresh/ - обнорвление токена
POST /api/v1/jwt/verify/ - проверка токена
Также в проекте реализована пагинация(LimitOffsetPagination).