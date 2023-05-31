from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    alias            = StringField('Alias', validators=[InputRequired()])
    password         = PasswordField('Contraseña', validators=[InputRequired()])