from .models import get_user
from flask import (render_template, redirect, url_for, request, current_app)
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from datetime import datetime

from app import login_manager
from . import autenticacion_blueprints
from .forms import InciarSesionForm, CrearUsuarioForm


from app.autenticacion.models import DocumentType, User, Admin, Patient, Doctor, Role
# crear_cuenta
@autenticacion_blueprints.route("/crear_cuenta", methods=['GET', 'POST'])
def crear_cuenta():

    if current_user.is_authenticated:
        page = None
        if current_user.get_type().get_id() == 1:
            page = 'administrador.administrador_index'
        elif current_user.get_type().get_id() == 2:
            page = 'administrador.doctor_index'
        elif current_user.get_type().get_id() == 3:
            page = 'administrador.patient_index'
        return redirect(url_for(page))

    form = CrearUsuarioForm(formdata=request.form)
    types = DocumentType.get_all()
    types.insert(0, DocumentType("Tipo de documento", 0))
    listTypes=[(i.get_id(), i.get_name()) for i in types]
    form.documentTypeId.choices = listTypes
    if form.validate_on_submit():
        user = Patient(form.name.data, form.lastName.data, form.password.data, form.documentTypeId.data, form.documentNumber.data, form.birthDate.data, form.phoneNumber.data, form.gender.data, datetime.now())
        user.save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('autenticacion.iniciar_sesion'))
    
    return render_template("crear_cuenta.html", form=form)


# iniciar_sesion
@autenticacion_blueprints.route("/iniciar_sesion", methods=['GET', 'POST'])
def iniciar_sesion():
    if current_user.is_authenticated:
        return redirect(url_for('inicio.inicio'))

    form = InciarSesionForm()
    if form.validate_on_submit():
        user:User = get_user(form.usuario.data)
        if user is not None and user.check_password(form.password.data):
            page = None
            if user.get_type().get_id() == 1:
                page = 'administrador.administrador_index'
            elif user.get_type().get_id() == 2:
                page = 'administrador.doctor_index'
            elif user.get_type().get_id() == 3:
                page = 'administrador.patient_index'
            
            login_user(user, remember=True)
            
            next_page = request.args.get('next')
            user.set_is_authenticated(True)
            
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for(page)
            print(page)
            return redirect(next_page)            
    return render_template('iniciar_sesion.html', form=form)


# logout
@autenticacion_blueprints.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('autenticacion.iniciar_sesion'))

# prueba para el login
@login_manager.user_loader
def load_user(user_id):
    user = User.get_by_id(user_id)
    return user
