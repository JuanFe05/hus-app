from flask import Blueprint

inicio_blueprints = Blueprint('inicio', __name__, template_folder='templates')

from . import routes
