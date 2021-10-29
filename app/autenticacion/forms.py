from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators
from wtforms.validators import DataRequired, Email, Length

class InciarSesionForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    ingresar = SubmitField('Iniciar Sesión')
    
class CrearUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    lastName = StringField('Apellidos', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    re_password = PasswordField('Re-Ingrese Password', validators=[DataRequired()])
    documentTypeId = SelectField('Tipo Documento', coerce=int)
    documentNumber = StringField('Número de documento', validators=[DataRequired()])
    phoneNumber = StringField('Número de telefono', validators=[DataRequired()])
    birthDate = DateField('Fecha de nacimiento', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    gender = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    
    is_active = SelectField('Estado', choices=[(1,'Activo')], coerce=int)
    
    guardar = SubmitField('Guardar')
    
