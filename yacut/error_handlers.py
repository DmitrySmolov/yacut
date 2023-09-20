from http import HTTPStatus
from typing import Any, Optional

from flask import jsonify, render_template, Response

from yacut import app, db


class InvalidAPIUsage(Exception):
    """Класс ошибки при неверном обращении к API."""
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self: 'InvalidAPIUsage',
                 message: str,
                 status_code: Optional[Any] = None) -> None:
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self: 'InvalidAPIUsage') -> dict:
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: Any) -> Response:
    """Обработчик ошибок в API."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error: HTTPStatus.NOT_FOUND) -> str:
    """Обработчик ошибки 404 (страница не найдена)."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error: HTTPStatus.INTERNAL_SERVER_ERROR) -> str:
    """Обработчик ошибки 500 (внутренняя ошибка сервера)."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
