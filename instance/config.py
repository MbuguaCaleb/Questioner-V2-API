import os

class Config(object):
    """ Base Config class """

    DEBUG = False
    TESTING = False
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
   

class DevelopmentConfig(Config):
    """ Config class for Development environment """

    DEBUG = True
    DATABASE_NAME = os.getenv('DATABASE_NAME')


class TestingConfig(Config):
    """ Config class for Testing environment """

    TESTING = True
    DATABASE_NAME = os.getenv('TEST_DATABASE_NAME')


class ProductionConfig(Config):
    """ Config class for Production environment """

    DEBUG = False
    TESTING = False
    DATABASE_NAME = os.getenv('DATABASE_NAME')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

