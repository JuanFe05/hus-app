from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app.autenticacion.models import Appointment, AppointmentType, DocumentType, Appointment, UserSimple, User
from . import appointment_blueprints
from .forms import CrearCitaForm
from datetime import datetime

# lista de citas
ROWS_PER_PAGE = 15

@appointment_blueprints.route("/citas", methods=['GET', 'POST'])
@login_required
def list():
    page = request.args.get('page', 1, type=int)
    if current_user.get_type().get_id() == 1 :
        appointments = Appointment.get_all()
    elif current_user.get_type().get_id() == 2 :
        appointments = Appointment.get_by_doctor(current_user.get_id())
    elif current_user.get_type().get_id() == 3 :
        appointments = Appointment.get_by_patient(current_user.get_id())
    if not appointments :
        appointments = []
    return render_template('list_appointment.html', appointments=appointments)

@appointment_blueprints.route("/citas/delete/<int:id>", methods=['GET', 'POST'])
@login_required
def delete(id):
    post:Appointment = Appointment.get_by_id(id)
    if post is not None :
        post.delete()
    else :
        return redirect(url_for('appointment.list'))
    page = request.args.get('page', 1, type=int)
    return redirect(url_for('appointment.list'))

# lista de citas
@appointment_blueprints.route("/citas/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    post:Appointment = Appointment.get_by_id(id)
    if post is not None :
        form = CrearCitaForm(formdata=request.form, obj=post)

        doctors = UserSimple.get_by_type(2)
        doctors.insert(0, UserSimple("Seleccione", "Doctor", 0))
        patients = UserSimple.get_by_type(3)
        patients.insert(0, UserSimple("Seleccione", "Paciente", 0))
        appointmentTypes = AppointmentType.get_all()
        appointmentTypes.insert(0, AppointmentType("Seleccione Tipo de Cita", 0))
        listDoctors=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in doctors]
        listPatients=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in patients]
        listAppointmentTypes=[(i.get_id(), i.get_name()) for i in appointmentTypes]
        form.doctorId.choices = listDoctors
        form.patientId.choices = listPatients
        form.appointmentTypeId.choices = listAppointmentTypes
        if request.method == 'POST':
            if form.validate_on_submit():
                post.set_doctorId(form.doctorId.data)
                post.set_patientId(form.patientId.data)
                post.set_date(form.date.data)
                post.set_appointmentTypeId(form.appointmentTypeId.data)
                post.update()
                next = request.args.get('next', None)
                if next:
                    return redirect(next)
                return redirect(url_for('appointment.list'))
    else :
        return redirect(url_for('appointment.list'))
    return render_template('edit_appointment.html',form=form)


# lista de comentarios
@appointment_blueprints.route("/cita", methods=['GET', 'POST'])
@login_required
def create():
    form = CrearCitaForm(request.form)
    doctors = UserSimple.get_by_type(2)
    doctors.insert(0, UserSimple("Seleccione", "Doctor", 0))
    patients = UserSimple.get_by_type(3)
    patients.insert(0, UserSimple("Seleccione", "Paciente", 0))
    appointmentTypes = AppointmentType.get_all()
    appointmentTypes.insert(0, AppointmentType("Seleccione Tipo de Cita", 0))
    listDoctors=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in doctors]
    listPatients=[(i.get_id(), i.get_name() + ' ' + i.get_lastName()) for i in patients]
    listAppointmentTypes=[(i.get_id(), i.get_name()) for i in appointmentTypes]
    form.doctorId.choices = listDoctors
    form.patientId.choices = listPatients
    form.appointmentTypeId.choices = listAppointmentTypes
    if form.validate_on_submit():
        Appointment(form.doctorId.data, form.date.data, datetime.now(), form.patientId.data, form.appointmentTypeId.data).save()
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('appointment.list'))
    
    return render_template("create_appointment.html", form=form)
