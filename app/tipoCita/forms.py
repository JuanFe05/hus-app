from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
    
class CrearAppointmentTypeForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    
    guardar = SubmitField('Guardar')
    
