from flask import render_template, request, redirect, url_for
from flask_login import login_required
from datetime import datetime

from app.autenticacion.models import Appointment, Comment, Doctor, UserSimple
from . import comment_blueprints
from .forms import CrearCommentForm
# lista de Comments
ROWS_PER_PAGE = 15

@comment_blueprints.route("/comments/<int:id>", methods=['GET', 'POST'])
@login_required
def list(id):
    page = request.args.get('page', 1, type=int)
    
    comments = Comment.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)

    if not comments :
        comments = []
    else :
        comments = comments.items
    
    appointment = Appointment.get_by_id(id)
    if not appointment :
        return redirect(url_for('appointment.list'))
    return render_template('list_comment.html', comments=comments, appointment=appointment)

@comment_blueprints.route("/comments/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:Comment = Comment.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('appointment.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('comment.list', id= id))

# lista de Comments
@comment_blueprints.route("/comments/edit/<int:idComment>", methods=['GET', 'POST'])
@login_required
def edit(idComment):
    post:Comment = Comment.get_by_id(idComment)
    if post is not None :
        form = CrearCommentForm(formdata=request.form, obj=post)
        doctors = Doctor.get_by_type(2)
        doctors.insert(0, UserSimple("Seleccionar", "Doctor", 0))
        listDoctors=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in doctors]
        form.doctorId.choices = listDoctors
        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_txt(form.txt.data)
                post.set_doctorId(form.doctorId.data)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('comment.list', id= post.get_appointment().get_id()))
    else :
        return redirect(url_for('comment.list', id= idComment))
    return render_template('edit_comment.html',form=form)

# lista de comentarios
@comment_blueprints.route("/comment/<int:id>", methods=['GET', 'POST'])
@login_required
def create(id):
    form = CrearCommentForm(request.form)
    doctors = Doctor.get_by_type(2)
    doctors.insert(0, UserSimple("Seleccionar", "Doctor", 0))
    listDoctors=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in doctors]
    form.doctorId.choices = listDoctors
    if form.validate_on_submit():
        Comment(datetime.now(), form.doctorId.data, form.txt.data, id).save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('comment.list', id= id))
    
    return render_template("create_comment.html", form=form)
