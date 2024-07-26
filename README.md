# Проект «API для Yatube»

API для Yatube представляет собой проект социальной сети, в котором возможно обрабатывать запросы к постам, группам, комментариям.

## Что мы использовали в проекте:

Python, Django, DRF, JWT + Djoser

## Установка:

### Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/EvZhi/api_final_yatube.git```

```cd <ваша_папка>```

### Cоздать и активировать виртуальное окружение:

```python3 -m venv env```

```source env/bin/activate```

### Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

### Выполнить миграции:

```python3 manage.py migrate```

### Запустить проект:

```python3 manage.py runserver```

## Описание

### Здесь вы можете совершать определенные действия с обьектами:
|Endpoint                              	| Objec   | Methods	                | Description                                                                  |
|---------------------------------------|---------|-------------------------|------------------------------------------------------------------------------|
|/api/v1/posts/	                        | Post	  | GET, POST	            | Получаем список постов и создаем пост.|
|/api/v1/posts/{id}/	                | Post	  | GET, PUT, PATCH, DELETE	| Получаем, редактируем, заменяем, отдельный пост.
|/api/v1/posts/{post_id}/comments/	    | Comment |	GET, POST	            | Получаем список комментариев и создаем комментарий к конкретному посту
|/api/v1/posts/{post_id}/comments/{id}/	| Comment |	GET, PUT, PATCH, DELETE	| Получаем, редактируем, заменяем, отдельный комментарий и конкретному посту.
|/api/v1/groups/	                    | Group	  | GET	                    | Получаем список групп. Только чтоние
|/api/v1/groups/{id}/	                | Group	  | GET	                    | Получаем конкретную группу. Только чтоние
|/api/v1/follow/	                    | Follo   | GET, POST	            |Получаем все подписки пользователя сделавшего GET запрос. Подписываемся на другого пользователя. Подписыватся на себя безсмысленно
|/api/v1/jwt/create/	                | Token	  | POST	                |Получаем токен
|/api/v1/jwt/refresh/	                | Token	  | POST	                |Обновляем токен
|/api/v1/jwt/verify/	                | Token	  | POST	                |Проверяем токен

## Примеры ответа:

### GET запрос
/api/v1/posts/

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
POST запрос
/api/v1/posts/


{
  "text": "string",
  "image": "string",
  "group": 0
}
Пример ответа.


{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
Остальные примеры запросов и ответов можно посмотреть в файле \api_final_yatube\yatube_api\static\redoc.yaml
Спасибо что пользуетесь нашими сервисами!

8b664a98c17470cdc8217363e17a48deddb29612

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver

Описание
Здесь вы можете совершать определенные действия с обьектами:
Endpoint	Object	Methods	Description
/api/v1/posts/	Post	GET, POST	Получаем список постов и создаем пост.
/api/v1/posts/{id}/	Post	GET, PUT, PATCH, DELETE	Получаем, редактируем, заменяем, отдельный пост.
/api/v1/posts/{post_id}/comments/	Comment	GET, POST	Получаем список комментариев и создаем комментарий к конкретному посту
/api/v1/posts/{post_id}/comments/{id}/	Comment	GET, PUT, PATCH, DELETE	Получаем, редактируем, заменяем, отдельный комментарий и конкретному посту.
/api/v1/groups/	Group	GET	Получаем список групп. Только чтоние
/api/v1/groups/{id}/	Group	GET	Получаем конкретную группу. Только чтоние
/api/v1/follow/	Follow	GET, POST	Получаем все подписки пользователя сделавшего GET запрос. Подписываемся на другого пользователя. Подписыватся на себя безсмысленно
/api/v1/jwt/create/	Token	POST	Получаем токен
/api/v1/jwt/refresh/	Token	POST	Обновляем токен
/api/v1/jwt/verify/	Token	POST	Проверяем токен
Примеры ответа
GET запрос
/api/v1/posts/

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
POST запрос
/api/v1/posts/


{
  "text": "string",
  "image": "string",
  "group": 0
}
Пример ответа.


{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
Остальные примеры запросов и ответов можно посмотреть в файле \api_final_yatube\yatube_api\static\redoc.yaml
Спасибо что пользуетесь нашими сервисами!