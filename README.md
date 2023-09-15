# Продуктовый помощник Foodgram
```
Cайт https://foodgramstudy.zapto.org/
Документация https://foodgramstudy.zapto.org/api/docs/redoc.html
Админ:  
почта - qwer@qwer.qwer
пароль - admin
```

![badge](https://github.com/dmBra1n/foodgram-project-react/actions/workflows/main.yml/badge.svg)
## О проекте
Foodgram — онлайн-сервис позволяющий обмениваться рецептами любимых блюд.<br>
Проект состоит из бэкенд-приложения на Django и фронтенд-приложения на React.

Проект написан в рамках учебного курса "Python-разработчик" от Yandex.Practicum.<br>
Основные задачи были:
- реализовать backend на django
- развернуть frontend и backend на облачном сервере используя Docker
- настроить GitHub Actions

#### Технологии в проекте

![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/django-REST-ff1709?style=flat-square&logo=django&logoColor=white&color=f1c552&labelColor=%230c4b33)
![Django](https://img.shields.io/badge/django-%230c4b33.svg?style=flat-square&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat-square&logo=nginx&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=flat-square&logo=postgresql&logoColor=white)
![Actions GitHub](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat-square&logo=githubactions&logoColor=white)

## Реализован  функционал:
- Аутентификация реализована с помощью стандартного модуля DRF - Authtoken.
- У неаутентифицированных пользователей доступ к API только на уровне чтения.

### Гость (неавторизованный пользователь)

  - Создать аккаунт.
  - Просматривать рецепты на главной страницы.
  - Просматривать отдельные страницы рецептов.
  - Фильтровать рецепты по тегам.

### Авторизованный пользователь

- Вход в систему под своим логином и паролем.
- Выход из системы (разлогиниться).
- Смена своего пароля.
- Создавать/редактировать/удалять собственные рецепты.
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Возможность добавлять/удалять рецепты в свой список избранного. Просматривать свою страницу избранных рецептов.
- Возможность добавлять/удалять рецепты в свой список покупок. Просматривать список покупок.
- Возможность скачать список покупок в txt формате.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

### Администратор
- Изменять пароль любого пользователя.
- Создавать/блокировать/удалять аккаунты пользователей.
- Добавлять/удалять/редактировать теги.
- Редактировать/удалять любые рецепты.
- Добавлять/удалять/редактировать ингредиенты.



## Локальный запуск проекта
1. Склонировать репозиторий
2. В корне проекта создать и прописать файл _.env_
  
    ```env
    POSTGRES_USER=<имя_пользователя_БД>
    POSTGRES_PASSWORD=<пароль_БД>
    POSTGRES_DB=<имя_БД>
    DB_PORT=<порт_соединения_к_БД>
    DB_HOST=db
    
    SECRET_KEY=<django_secret_key>
    ```
3. В терминале, в корне проекта выполнить команду `docker compose up -d`
4. Выполнить миграции, собрать статику и загрузить ингридиенты в BD:
     ```
     docker exec backend python manage.py migrate
     docker compose exec backend python manage.py collectstatic
     docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
     docker compose exec backend python manage.py load_ingredients  
     ```
5. Документация к API будет доступна по адресу: http://localhost:8000/api/docs/redoc.html

## Автор
Вадим Миронов - [ссылка на GitHub](https://github.com/dmBra1n)
