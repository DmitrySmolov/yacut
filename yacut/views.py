from http import HTTPStatus
from random import choice

from flask import abort, flash, redirect, render_template, Response, request

from settings import Constant, Message
from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap


def get_unique_short_id() -> str:
    """Функция для генерации случайного короткого URL."""
    while True:
        short_id = ''.join(
            (choice(Constant.SHORT_URL_CHARS)
             for _ in range(Constant.SHORT_URL_MAX_LEN))
        )
        db_match = URLMap.query.filter_by(short=short_id).first()
        if not db_match:
            return short_id


def get_full_short_url(short_id: str) -> str:
    """Функция для получения ссылки на короткий URL."""
    return request.host_url + short_id


@app.route(rule='/', methods=('GET', 'POST'))
def add_urlmap_view() -> str:
    """
    View-функция для отображения главной страницы с формой регистрации новых
     коротких URL.
    """
    form = URLMapForm()
    if (
        form.validate_on_submit() and
        form.custom_id.data and
        URLMap.query.filter_by(short=form.custom_id.data).first()
    ):
        message = f'Имя {form.custom_id.data} уже занято!'
        flash(message=message)
        return render_template('index.html', form=form)
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        new_short_url = get_full_short_url(short)
        message = (
            f'{Message.SHORT_URL_READY} <br> '
            f'<a href="{new_short_url}"> {new_short_url} </a>'
        )
        flash(message=message)
        form.original_link.data = form.custom_id.data = ''
    return render_template('index.html', form=form)


@app.route(rule='/<string:short>', methods=('GET',))
def redirect_to_original(short: str) -> Response:
    """
    View-функция для переадресации с известного короткого URL на оригинальный.
    """
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(location=url_map.original)
