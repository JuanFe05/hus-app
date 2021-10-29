from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app.autenticacion.models import DocumentType
from . import documentType_blueprints
from .forms import CrearDocumentTypeForm
# lista de DocumentTypes
ROWS_PER_PAGE = 15

@documentType_blueprints.route("/documentTypes", methods=['GET', 'POST'])
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    
    documentTypes = DocumentType.query.paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)

    if not documentTypes :
        documentTypes = []
    else :
        documentTypes = documentTypes.items
    return render_template('list_documentType.html', documentTypes=documentTypes)

@documentType_blueprints.route("/documentTypes/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:DocumentType = DocumentType.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('documentType.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('documentType.list'))

# lista de DocumentTypes
@documentType_blueprints.route("/documentTypes/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post:DocumentType = DocumentType.get_by_id(id)
    if post is not None :
        form = CrearDocumentTypeForm(formdata=request.form, obj=post)

        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_name(form.name.data)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('documentType.list'))
    else :
        return redirect(url_for('documentType.list'))
    return render_template('edit_documentType.html',form=form)


# lista de comentarios
@documentType_blueprints.route("/documentType", methods=['GET', 'POST'])
@login_required
def create():
    form = CrearDocumentTypeForm(request.form)
    if form.validate_on_submit():
        DocumentType(form.name.data).save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('documentType.list'))
    
    return render_template("create_documentType.html", form=form)
