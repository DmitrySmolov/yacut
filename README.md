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
