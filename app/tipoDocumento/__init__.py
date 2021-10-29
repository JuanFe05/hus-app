from flask import Blueprint

documentType_blueprints = Blueprint('documentType', __name__, template_folder='templates')

from . import routes