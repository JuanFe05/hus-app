from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app.autenticacion.models import AppointmentType
from . import appointmentType_blueprints
from .forms import CrearAppointmentTypeForm
# lista de AppointmentTypes
ROWS_PER_PAGE = 15

@appointmentType_blueprints.route("/appointmentTypes", methods=['GET', 'POST'])
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    
    appointmentTypes = AppointmentType.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)

    if not appointmentTypes :
        appointmentTypes = []
    else :
        appointmentTypes = appointmentTypes.items
    return render_template('list_appointmentType.html', appointmentTypes=appointmentTypes)

@appointmentType_blueprints.route("/appointmentTypes/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:AppointmentType = AppointmentType.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('appointmentType.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('appointmentType.list'))

# lista de AppointmentTypes
@appointmentType_blueprints.route("/appointmentTypes/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post:AppointmentType = AppointmentType.get_by_id(id)
    if post is not None :
        form = CrearAppointmentTypeForm(formdata=request.form, obj=post)

        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_name(form.name.data)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('appointmentType.list'))
    else :
        return redirect(url_for('appointmentType.list'))
    return render_template('edit_appointmentType.html',form=form)


# lista de comentarios
@appointmentType_blueprints.route("/appointmentType", methods=['GET', 'POST'])
@login_required
def create():
    form = CrearAppointmentTypeForm(request.form)
    if form.validate_on_submit():
        AppointmentType(form.name.data).save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('appointmentType.list'))
    
    return render_template("create_appointmentType.html", form=form)
