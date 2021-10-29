from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators
from wtforms.form import Form
from wtforms.validators import DataRequired, Email, Length
    
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
    typeId = SelectField('Rol', coerce=int)
    
    is_active = SelectField('Estado', choices=[(1,'Activo'), (2,'Desactivado')], coerce=int)
    
    guardar = SubmitField('Guardar')
    
