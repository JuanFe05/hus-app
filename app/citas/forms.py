from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators
from wtforms.form import Form
from wtforms.validators import DataRequired, Email, Length
    
class CrearCitaForm(FlaskForm):
    date = DateField('Fecha de cita', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    doctorId = SelectField('Doctor', coerce=int, validators=[DataRequired()])
    patientId = SelectField('Paciente', coerce=int, validators=[DataRequired()])
    appointmentTypeId = SelectField('Tipo de cita', coerce=int, validators=[DataRequired()])
    
    guardar = SubmitField('Guardar')
    
