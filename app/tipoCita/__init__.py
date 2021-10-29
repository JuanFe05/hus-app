from flask import Blueprint

appointmentType_blueprints = Blueprint('appointmentType', __name__, template_folder='templates')

from . import routes