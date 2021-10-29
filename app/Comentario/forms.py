from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired
    
class CrearCommentForm(FlaskForm):
    doctorId = SelectField('Doctor', coerce=int)
    txt = TextAreaField('Comentario', validators=[DataRequired()])
    
    guardar = SubmitField('Guardar')
    
