from flask import Blueprint

rol_blueprints = Blueprint('rol', __name__, template_folder='templates')

from . import routes