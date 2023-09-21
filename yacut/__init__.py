from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from yacut.settings import Config

app = Flask(import_name=__name__,
            static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

from yacut import api_views, error_handlers, models, views
