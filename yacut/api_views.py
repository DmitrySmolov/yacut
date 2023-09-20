from http import HTTPStatus

from flask import jsonify, request, Response

from settings import Message
from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.validators import is_valid_custom_id, is_valid_url
from yacut.views import get_full_short_url, get_unique_short_id


@app.route(rule='/api/id/', methods=('POST',))
def create_id() -> Response:
    """View-функция для создания новой короткой ссылки."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(message=Message.API_REQUIRED_DATA)
    if 'url' not in data:
        raise InvalidAPIUsage(message=Message.API_REQUIRED_FIELD)
    if not is_valid_url(data['url']):
        raise InvalidAPIUsage(message=Message.ORIG_URL_FORMAT)
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    if not is_valid_custom_id(data['custom_id']):
        raise InvalidAPIUsage(message=Message.API_BAD_CUSTOM_ID)
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(message=f'Имя "{data["custom_id"]}" уже занято.')
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    response_data = url_map.to_dict()
    response_data['short_link'] = get_full_short_url(
        response_data['short_link']
    )
    return jsonify(response_data), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_id(short_id: str) -> Response:
    """View-функция для получения оригинальной ссылки по короткому ID."""
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage(message=Message.API_SHORT_ID_NOT_FOUND,
                              status_code=HTTPStatus.NOT_FOUND)
    response_data = url_map.to_dict()
    del response_data['short_link']
    return jsonify(response_data), HTTPStatus.OK
