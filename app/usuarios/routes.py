from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.autenticacion.models import DocumentType, User, Admin, Patient, Doctor, Role
from . import user_blueprints
from .forms import CrearUsuarioForm
from datetime import datetime

# lista de usuarios
ROWS_PER_PAGE = 15

@user_blueprints.route("/usuarios", methods=['GET', 'POST'])
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    
    return render_template('list_user.html', users=users.items)

@user_blueprints.route("/usuarios/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:User = User.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('user.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('user.list'))

# lista de citas
@user_blueprints.route("/usuarios/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post:User = User.get_by_id(id)
    if post is not None :
        form = CrearUsuarioForm(formdata=request.form, obj=post)
        types = DocumentType.get_all()
        types.insert(0, DocumentType("Tipo de documento", 0))
        listTypes=[(i.get_id(), i.get_name()) for i in types]
        roles = Role.get_all()
        roles.insert(0, Role("Tipo de rol", 0))
        listRoles=[(i.get_id(), i.get_name()) for i in roles]
        form.documentTypeId.choices = listTypes
        form.typeId.choices = listRoles
        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_documentTypeId(form.documentTypeId.data)
                post.set_typeId(form.typeId.data)
                post.set_name(form.name.data)
                post.set_lastName(form.lastName.data)
                post.set_password(form.password.data)
                post.set_documentNumber(form.documentNumber.data)
                post.set_phoneNumber(form.phoneNumber.data)
                post.set_birthDate(form.birthDate.data)
                post.set_gender(form.gender.data)
                if form.is_active.data == 1 : 
                    post.set_is_active(True)
                else :
                    post.set_is_active(False)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('user.list'))
    else :
        return redirect(url_for('user.list'))
    return render_template('edit_user.html',form=form)

@user_blueprints.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    id = current_user.get_id()
    post:User = User.get_by_id(id)
    if post is not None :
        form = CrearUsuarioForm(formdata=request.form, obj=post)
        types = DocumentType.get_all()
        types.insert(0, DocumentType("Tipo de documento", 0))
        listTypes=[(i.get_id(), i.get_name()) for i in types]
        roles = Role.get_all()
        roles.insert(0, Role("Tipo de rol", 0))
        listRoles=[(i.get_id(), i.get_name()) for i in roles]
        form.documentTypeId.choices = listTypes
        form.typeId.choices = listRoles
        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_documentTypeId(form.documentTypeId.data)
                post.set_typeId(form.typeId.data)
                post.set_name(form.name.data)
                post.set_lastName(form.lastName.data)
                post.set_password(form.password.data)
                post.set_documentNumber(form.documentNumber.data)
                post.set_phoneNumber(form.phoneNumber.data)
                post.set_birthDate(form.birthDate.data)
                post.set_gender(form.gender.data)
                if form.is_active.data == 1 : 
                    post.set_is_active(True)
                else :
                    post.set_is_active(False)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('user.list'))
    else :
        return redirect(url_for('user.list'))
    return render_template('edit_user.html',form=form)

# lista de comentarios
@user_blueprints.route("/usuario", methods=['GET', 'POST'])
@login_required
def create():
    form = CrearUsuarioForm(formdata=request.form)
    types = DocumentType.get_all()
    types.insert(0, DocumentType("Tipo de documento", 0))
    listTypes=[(i.get_id(), i.get_name()) for i in types]
    roles = Role.get_all()
    roles.insert(0, Role("Tipo de rol", 0))
    listRoles=[(i.get_id(), i.get_name()) for i in roles]
    form.documentTypeId.choices = listTypes
    form.typeId.choices = listRoles
    print("1")
    if form.validate_on_submit():
        print("2")
        print(form.typeId.data)
        if form.typeId.data == "1" or form.typeId.data == 1 :
            print("3")
            user = Admin(form.name.data, form.lastName.data, form.password.data, form.documentTypeId.data, form.documentNumber.data, form.birthDate.data, form.phoneNumber.data, form.gender.data, datetime.now(), 1)
            user.save()
        elif form.typeId.data == "2" or form.typeId.data == 2 :
            user = Doctor(form.name.data, form.lastName.data, form.password.data, form.documentTypeId.data, form.documentNumber.data, form.birthDate.data, form.phoneNumber.data, form.gender.data, datetime.now(), "General")
            user.save()
        elif form.typeId.data == "3" or form.typeId.data == 3 :
            user = Patient(form.name.data, form.lastName.data, form.password.data, form.documentTypeId.data, form.documentNumber.data, form.birthDate.data, form.phoneNumber.data, form.gender.data, datetime.now())
            user.save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('user.list'))
    
    return render_template("create_user.html", form=form)
