from flask import render_template, request
from flask_login import login_required
from app.autenticacion.models import User
from . import administrador_blueprints


@administrador_blueprints.route("/administrador", methods=['GET', 'POST'])
@login_required
def administrador_index():
    return render_template('administrador_index.html')

@administrador_blueprints.route("/doctor", methods=['GET', 'POST'])
@login_required
def doctor_index():
    return render_template('doctor_index.html')

@administrador_blueprints.route("/patient", methods=['GET', 'POST'])
@login_required
def patient_index():
    return render_template('patient_index.html')

# lista de comentarios
@administrador_blueprints.route("/comments", methods=['GET', 'POST'])
def comentarios_administrador():
    return render_template('comment_list.html')
