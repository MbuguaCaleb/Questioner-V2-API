""" Initiates blueprints for version 2 of the API """
from flask import Blueprint

version_2 = Blueprint('version_2', __name__, url_prefix='/api/v2')

