from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class NewPasswordForm(FlaskForm):
    code             = StringField('Código', validators=[InputRequired()])
    password         = PasswordField('Contraseña', validators=[InputRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[InputRequired(), EqualTo('password')])