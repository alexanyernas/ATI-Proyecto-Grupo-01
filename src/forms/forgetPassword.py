from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import InputRequired, Email

class ForgetPasswordForm(FlaskForm):
    email = EmailField('Correo Electrónico', validators=[InputRequired(), Email()])