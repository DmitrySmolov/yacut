import re
from typing import Optional, TYPE_CHECKING
from urllib.parse import urlparse

from wtforms import StringField
from wtforms.validators import ValidationError

from settings import Constant, Message
if TYPE_CHECKING:
    from yacut.forms import URLMapForm
from yacut.models import URLMap


class UniqueCustomId:
    """
    Валидатор проверки уникальности короткого URL-идентификатора в форме
     URLMapForm.
    """
    def __call__(
        self: 'UniqueCustomId',
        form: 'URLMapForm',
        field: StringField
    ) -> None:
        db_match = URLMap.query.filter_by(short=field.data).first()
        if db_match:
            message = f'Имя {field.data} уже занято!'
            raise ValidationError(message=message)


def is_valid_url(url: str) -> bool:
    """
    Функция для проверки значения поля 'url' в теле запроса к API на
     соответствие формату URL.
    """
    try:
        result = urlparse(url)
        return all((result.scheme, result.netloc))
    except ValueError:
        return False


def is_valid_custom_id(custom_id: str) -> bool:
    """
    Функция для проверки значения поля 'custom_id' в теле запроса к API на
     соответствие допустимому формату короткого ID.
    """
    return bool(re.match(Constant.SHORT_URL_FORMAT, custom_id))
