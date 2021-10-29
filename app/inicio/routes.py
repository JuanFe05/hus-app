from flask import render_template

from . import inicio_blueprints

@inicio_blueprints.route("/")
def inicio():
    return render_template('inicio.html')
