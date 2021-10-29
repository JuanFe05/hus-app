from flask import Blueprint

appointment_blueprints = Blueprint('appointment', __name__, template_folder='templates')

from . import routes