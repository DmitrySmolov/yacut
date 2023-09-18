import os
import string


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(key='DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv(key='SECRET_KEY', default='SECRET_KEY')


class Constant(object):
    ORIG_URL_MIN_LEN = 3
    ORIG_URL_MAX_LEN = 2000
    ORIG_URL_REPR_LEN = 6
    SHORT_URL_LEN = 6
    SHORT_URL_FORMAT = r'^[a-zA-Z0-9]+$'
    SHORT_URL_CHARS = string.ascii_letters + string.digits


class Message(object):
    REQUIRED_FIELD = 'Обязательное поле'
    ORIG_URL_LEN = (f'Длина ссылки от {Constant.ORIG_URL_MIN_LEN} и '
                    f'до {Constant.ORIG_URL_MAX_LEN} символов')
    ORIG_URL_FORMAT = 'Ссылка должна быть в формате URL'
    SHORT_URL_NOT_UNIQUE = 'Такой идентификатор уже используется'
    SHORT_URL_LEN = f'Длина {Constant.SHORT_URL_LEN} символов'
    SHORT_URL_FORMAT = 'Допустимы только латинские символы и цифры'
    SHORT_URL_READY = 'Ваша короткая ссылка готова:\n'
