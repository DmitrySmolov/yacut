from datetime import datetime
from typing import Any

from settings import Constant
from yacut_app import db


class URLMap(db.Model):
    """Модель для хранения связей оригинальных и коротких URL-ссылок."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(Constant.ORIG_URL_MAX_LEN),
                         nullable=False)
    short = db.Column(db.String(Constant.SHORT_URL_LEN),
                      unique=True,
                      nullable=False)
    timestamp = db.Column(db.DateTime,
                          index=True,
                          default=datetime.utcnow)

    def to_dict(self: 'URLMap') -> dict[int, str, str, datetime]:
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self: 'URLMap', data: dict[Any]) -> None:
        for field in ('original', 'short'):
            if field in data:
                setattr(self, field, data[field])

    def __str__(self: 'URLMap') -> str:
        return (f'Ссылка(Кор:{self.short}, '
                f'Ориг: {self.original[Constant.ORIG_URL_REPR_LEN]})')
