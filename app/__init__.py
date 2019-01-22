import os
from flask import Flask, jsonify
from instance.config import app_config
from app.api.v2.views.user_views import v1 as users_blueprint_v2
from db_conn import create_tables

 
def create_app(config_name):
    """ Function to initialize Flask app """
    config_name = os.environ.get('FLASK_CONFIG', 'development')
    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    create_tables()

    app.register_blueprint(users_blueprint_v2)

    return app




    