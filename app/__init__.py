"""This is main module, it contains config, initializes extensions."""
from flask import Flask
from extensions import db
from app.api.views import blueprint

from config import Config

__all__ = ['create_app']

def create_app(config=None, app_name=None):
    """This factory function create app object with parameters send to function."""

    app = Flask(__name__, static_folder='./static', template_folder='./templates')

    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)

    return app

def configure_app(app, config=None):
    """
    This function cinfigures app. Default config is from Config class.
    If you need, you can pass config by parameter.
    """

    app.config.from_object(Config)
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
      app.config.from_object(config)

def configure_extensions(app):
    """This function configures all extensions used in app."""

    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

def configure_blueprints(app):
    """This function is for register blueprints in app."""
    app.register_blueprint(blueprint)



