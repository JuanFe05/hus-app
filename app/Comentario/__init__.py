from flask import Blueprint

comment_blueprints = Blueprint('comment', __name__, template_folder='templates')

from . import routes