from datetime import datetime
from typing import Optional

from yacut import db
from yacut.settings import Constant


class URLMap(db.Model):
    """Модель для хранения связей оригинальных и коротких URL-ссылок."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(Constant.ORIG_URL_MAX_LEN),
                         nullable=False)
    short = db.Column(db.String(Constant.SHORT_URL_MAX_LEN),
                      unique=True,
                      nullable=False)
    timestamp = db.Column(db.DateTime,
                          index=True,
                          default=datetime.utcnow)

    def to_dict(self: 'URLMap') -> dict[str, str]:
        return dict(
            url=self.original,
            short_link=self.short
        )

    def from_dict(self: 'URLMap', data: dict[str, Optional[str]]) -> None:
        for field in Constant.API_DESERIALIZE:
            if field in data:
                setattr(self, Constant.API_DESERIALIZE[field], data[field])

    def __str__(self: 'URLMap') -> str:
        return (f'Ссылка(Кор:{self.short}, '
                f'Ориг: {self.original[Constant.ORIG_URL_REPR_LEN]})')
