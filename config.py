from os import environ

class BaseConfig(object):
    """Base configuration."""

    DEBUG = None
    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"
    FILES_FOLDER= "app/static/uploads"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    ENV = "development"
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "root")
    DB_PASS = environ.get("DB_PASS", "")
    DB_NAME = environ.get("DB_NAME", "grupo37")
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:@localhost/grupo37'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV = "production"
    DEBUG = environ.get("DEBUG", False)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "grupo37")
    DB_PASS = environ.get("DB_PASS", "YTdhZmE5MDFkMmRj")
    DB_NAME = environ.get("DB_NAME", "grupo37")
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://grupo37:YTdhZmE5MDFkMmRj@localhost/grupo37'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
