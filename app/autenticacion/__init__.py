from flask import Blueprint

autenticacion_blueprints = Blueprint('autenticacion', __name__, template_folder='templates')

from . import routes