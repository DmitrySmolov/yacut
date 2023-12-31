from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from yacut.settings import Constant, Message
from yacut.validators import UniqueCustomId


class URLMapForm(FlaskForm):
    """Форма для создания новой записи объекта URLMap в БД."""
    original_link = URLField(
        label='Оригинальный адрес',
        validators=(
            DataRequired(message=Message.REQUIRED_FIELD),
            Length(min=Constant.ORIG_URL_MIN_LEN,
                   max=Constant.ORIG_URL_MAX_LEN,
                   message=Message.ORIG_URL_LEN),
            URL(message=Message.ORIG_URL_FORMAT)
        ),
        description='Введите оригинальный адрес URL, который хотите укоротить'
    )
    custom_id = StringField(
        label='Короткий идентификатор',
        validators=(
            Optional(),
            Length(min=Constant.SHORT_URL_MIN_LEN,
                   max=Constant.SHORT_URL_MAX_LEN,
                   message=Message.SHORT_URL_LEN),
            Regexp(regex=Constant.SHORT_URL_FORMAT,
                   message=Message.SHORT_URL_FORMAT),
            UniqueCustomId()
        ),
        description=('Укажите свой идентификатор из латинских букв и/или цифр'
                     f'длиной от {Constant.SHORT_URL_MIN_LEN} до '
                     f'{Constant.SHORT_URL_MAX_LEN} символов либо оставьте '
                     'поле пустым, чтобы сгенерировать случайный')
    )
    submit = SubmitField(label='Добавить')
