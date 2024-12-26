# carsMVP

Это веб-приложение сделал я его на FastAPI, это простой RESTful API для управления автомобилями, комментариями и аутентификацией пользователей.

## Технологии

• **FastAPI:** Фреймворк для создания веб-API.

• **SQLAlchemy:** ORM для приложения

• **SQLite:** База данных.

• **Passlib:** Для хеширования паролей.

• **Python-jose:** Для работы с JWT.

• **Uvicorn:** ASGI-сервер для запуска FastAPI-приложения.

• **Docker:** Для контейнеризации приложения.

## Swagger UI

Для просмотра документации API и взаимодействия с ним используется Swagger UI. Он доступен по адресу: http://localhost:8000/docs

## Запуск

1. без Docker
   clone https://github.com/Wiquzix/carsMVP.git
   pip install -r requirements.txt
   python main.py
2. через Docker
   clone https://github.com/Wiquzix/carsMVP.git
   docker build -t fastapi-app .
   docker run -p 8000:8000 fastapi-app
   в обеих вариантах приложение будет доступно по адресу: http://localhost:8000

## Структура проекта

• main.py: Основной файл приложения FastAPI.

• models.py: Модели данных SQLAlchemy.

• schemas.py: Схемы данных для Pydantic.

• database.py: Конфигурация подключения к базе данных.

• routers.py: Определение маршрутов API.

• auth.py: Функции аутентификации и авторизации.

• crud.py: CRUD (Create, Read, Update, Delete) операции для работы с базой данных.

• requirements.txt: Список зависимостей проекта.

• Dockerfile: Файл для сборки Docker-образа.

## ендпоинты

# Cars

• GET /api/cars/: Получение списка автомобилей.

• GET /api/cars/{id}: Получение информации о конкретном автомобиле.

• POST /api/cars/: Создание нового автомобиля (требуется авторизация).

• PUT /api/cars/{id}: Обновление информации об автомобиле (требуется авторизация).

• DELETE /api/cars/{id}: Удаление автомобиля (требуется авторизация).

# Comments

• GET /api/cars/{car_id}/comments/: Получение комментариев к автомобилю.

• POST /api/cars/{car_id}/comments/: Добавление нового комментария к автомобилю (требуется авторизация).

# Authentication

• POST /api/token: Получение токена доступа (вход).

• POST /api/create_user/: Регистрация нового пользователя.

В правом верхнем углу есть кнопка Authorize туда можно сразу ввести данные пользователя что бы ко всем запросам прикреплялся header ('Authorization': 'Bearer {Token}') что бы отправлять запросы на ручки в которых требуется авторизация
