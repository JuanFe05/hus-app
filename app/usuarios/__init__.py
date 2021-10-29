from flask import Blueprint

user_blueprints = Blueprint('user', __name__, template_folder='templates')

from . import routes