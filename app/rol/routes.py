from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app.autenticacion.models import Role
from . import rol_blueprints
from .forms import CrearRolForm

# lista de roles
ROWS_PER_PAGE = 15

@rol_blueprints.route("/roles", methods=['GET', 'POST'])
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    
    rols = Role.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)

    if not rols :
        rols = []
    else :
        rols = rols.items
    return render_template('list_rol.html', rols=rols)

@rol_blueprints.route("/roles/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:Role = Role.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('rol.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('rol.list'))

# lista de roles
@rol_blueprints.route("/roles/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post:Role = Role.get_by_id(id)
    if post is not None :
        form = CrearRolForm(formdata=request.form, obj=post)

        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_name(form.name.data)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('rol.list'))
    else :
        return redirect(url_for('rol.list'))
    return render_template('edit_rol.html',form=form)


# lista de comentarios
@rol_blueprints.route("/rol", methods=['GET', 'POST'])
@login_required
def create():
    form = CrearRolForm(request.form)
    if form.validate_on_submit():
        Role(form.name.data).save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('rol.list'))
    
    return render_template("create_rol.html", form=form)
