import os
import string


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(key='DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv(key='SECRET_KEY', default='SECRET_KEY')
    STATIC_FOLDER = '../html/'
    TEMPLATE_FOLDER = '../html/templates'


class Constant(object):
    ORIG_URL_MIN_LEN = 3
    ORIG_URL_MAX_LEN = 2000
    ORIG_URL_REPR_LEN = 6
    SHORT_URL_MIN_LEN = 1
    SHORT_URL_MAX_LEN = 6
    # регулярное выражение для проверки формата короткого ID
    SHORT_URL_FORMAT = r'^[a-zA-Z0-9]{1,6}$'
    # набор допустимых символов для короткого ID
    SHORT_URL_CHARS = string.ascii_letters + string.digits
    # словарь для сопоставления имён полей в JSON API и модели в БД
    API_DESERIALIZE = {'url': 'original',
                       'custom_id': 'short'}


class Message(object):
    REQUIRED_FIELD = 'Обязательное поле'
    ORIG_URL_LEN = (f'Длина ссылки от {Constant.ORIG_URL_MIN_LEN} и '
                    f'до {Constant.ORIG_URL_MAX_LEN} символов')
    ORIG_URL_FORMAT = 'Ссылка должна быть в формате URL'
    SHORT_URL_NOT_UNIQUE = 'Такой идентификатор уже используется'
    SHORT_URL_LEN = (f'Длина должна быть от {Constant.SHORT_URL_MIN_LEN} '
                     f'и до {Constant.SHORT_URL_MAX_LEN} символов')
    SHORT_URL_FORMAT = 'Допустимы только латинские символы и цифры'
    SHORT_URL_READY = 'Ваша короткая ссылка готова:'
    API_REQUIRED_DATA = 'Отсутствует тело запроса'
    API_REQUIRED_FIELD = '\"url\" является обязательным полем!'
    API_BAD_CUSTOM_ID = 'Указано недопустимое имя для короткой ссылки'
    API_SHORT_ID_NOT_FOUND = 'Указанный id не найден'
