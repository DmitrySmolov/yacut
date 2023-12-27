# Yacut

Yacut - это небольшое web-приложение для создания коротких URL-ссылок на различные web-страницы.

## Возможности приложения

- Создание короткой ссылки с указанным пользователем идентификатором
- Генерация случайной короткой ссылки в случае, если пользователь не указал свой вариант
- Переадресация пользователя с короткой ссылки на исходную web-страницу

## Технологии

[![Python][Python-badge]][Python-url]
[![Flask][Flask-badge]][Flask-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]
[![SQLite][SQLite-badge]][SQLite-url]

## Установка и использование

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корне проекта создайте файл переменных окружения `.env` со следующими переменными:
```
FLASK_APP=yacut
FLASK_ENV=<production для продакшена или development для отладки>
DATABASE_URI=<dialect+driver://username:password@host:port/database> # где dialect+driver - тип базы данных и драйвер(опционально), username:password - имя пользователя и пароль для подключения к БД, host - местоположение сервера БДб, port - её порт, database - её имя. По умолчанию это будет db.sqlite3 в директории yacut
SECRET_KEY=<ваш секретный ключ>
```
В терминале выполните следующие комманды:
```
flask db init
```

```
flask db migrate
```

В корневой папке в директории migrations/versions/ автоматически создастся файл начальной миграции, а в папке приложения yacut/ файл БД db.sqlite3 <br>

Приложение готово к запуску по следующей команде:
```
flask run
```
Приятного использования! :heart:

## Авторство

Дима Смолов

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)


<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Flask-url]: https://flask.palletsprojects.com/
[Flask-badge]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white

[SQLAlchemy-url]: https://www.sqlalchemy.org/
[SQLAlchemy-badge]: https://img.shields.io/badge/SQLAlchemy-CC2927?style=for-the-badge&logo=sqlalchemy&logoColor=white

[SQLite-url]: https://www.sqlite.org/index.html
[SQLite-badge]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
