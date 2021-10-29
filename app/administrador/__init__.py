from flask import Blueprint

administrador_blueprints = Blueprint('administrador', __name__, template_folder='templates')

from . import routes