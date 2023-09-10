# Продуктовый помощник Foodgram
## О проекте
Foodgram — онлайн-сервис позволяющий обмениваться рецептами любимых блюд.<br>
Проект состоит из backend-приложения на Django и frontend-приложения на React.

Сервис позволяет:
- зарегистрироваться и авторизоваться пользователю
- опубликовать рецепт блюда
- добавить понравившиеся рецепты в список «Избранное»
- добавить рецепт в корзину(список покупок продуктов)
- скачать список покупок продуктов

Проект написан в рамках учебного курса "Python-разработчик" от Yandex.Practicum.
Основные задачи были:
- реализовать backend на django
- развернуть frontend и backend на облачном сервере используя Docker  

Технологии в проекте <br>
:small_orange_diamond: Python<br>
:small_orange_diamond: Django<br>
:small_orange_diamond: Django REST Framework<br>
:small_orange_diamond: PostgreSQL<br>
:small_orange_diamond: Nginx<br>
:small_orange_diamond: Gunicorn<br>
:small_orange_diamond: Docker<br>

## Локальный запуск проекта
1. Склонировать репозиторий
2. В корне проекта создать и прописать файл _.env_
  
    ```
    POSTGRES_USER=<имя_пользователя_БД>
    POSTGRES_PASSWORD=<пароль_БД>
    POSTGRES_DB=<имя_БД>
    DB_PORT=<порт_соединения_к_БД>
    DB_HOST=db
    
    SECRET_KEY=<django_secret_key>
    ```
3. В теменале, в корне проекта выполнить команду `docker compose up -d`
4. Вполнить миграции, собрать статику и загрузить ингридиенты в BD:
     ```
     docker exec backend python manage.py migrate
     docker compose exec backend python manage.py collectstatic
     docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
     docker compose exec backend python manage.py load_ingredients  
     ```

## Автор
Вадим Миронов - [ссылка на GitHub](https://github.com/dmBra1n)
