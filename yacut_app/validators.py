from typing import Optional

from wtforms import StringField
from wtforms.validators import ValidationError

from settings import Message
from yacut_app.forms import URLMapForm
from yacut_app.models import URLMap


class UniqueCustomId:
    """
    Валидатор проверки уникальности короткого URL-идентификатора в форме
     URLMapForm.
    """
    def __init__(
        self: 'UniqueCustomId',
        message: Optional[str] = None
    ) -> None:
        self.message = message or Message.SHORT_ID_ALREADY_USED

    def __call__(
        self: 'UniqueCustomId',
        form: URLMapForm,
        field: StringField
    ) -> None:
        db_match = URLMap.query.filter_by(short=field.data).first()
        if db_match:
            raise ValidationError(message=self.message)
