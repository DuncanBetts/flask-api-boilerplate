import os


class BaseConfig(object):

    # define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "secret"
    CSRF_SESSION_KEY = "secret"

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True

    DOMAIN = 'http://localhost:5000'

    # check this why?
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):

    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    DB_LOGIN = 'devel_user'
    DB_PASSWORD = 'password'
    DB_NAME = 'newsroom_test'
    DB_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True

    DB_LOGIN = 'login'
    DB_PASSWORD = 'password'
    DB_NAME = 'database'
    DB_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
#    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_LOGIN + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME


class ProductionConfig(BaseConfig):
    pass


# get from env variable ?
class Config(DevelopmentConfig):
    pass
