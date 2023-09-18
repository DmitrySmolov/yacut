from random import choice

from flask import flash, render_template

from settings import Constant, Message
from yacut_app import app, db
from yacut_app.forms import URLMapForm
from yacut_app.models import URLMap


def get_unique_short_id() -> str:
    while True:
        short_id = ''.join(
            (choice(Constant.SHORT_URL_CHARS)
             for _ in range(Constant.SHORT_URL_LEN))
        )
        db_match = URLMap.query.filter_by(short=short_id).first()
        if not db_match:
            return short_id


@app.route('/', methods=('GET', 'POST'))
def add_urlmap_view():
    form = URLMapForm()
    if (
        form.validate_on_submit() and
        form.custom_id.data and
        URLMap.query.filter_by(short=form.custom_id.data).first()
    ):
        flash(message=Message.SHORT_URL_NOT_UNIQUE)
        return render_template('html/templates/index.html', form=form)
    short = form.custom_id.data or get_unique_short_id()
    url_map = URLMap(
        original=form.original_link.data,
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    flash(message=Message.SHORT_URL_READY)
    return render_template('html/templates/index.html')
