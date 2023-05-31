from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    first_name       = StringField('Nombre', validators=[InputRequired()])
    last_name        = StringField('Apellido', validators=[InputRequired()])
    alias            = StringField('Alias', validators=[InputRequired()])
    phone            = StringField('Número de Teléfono')
    email            = StringField('Correo Electrónico', validators=[InputRequired(), Email()])
    password         = PasswordField('Contraseña', validators=[InputRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[InputRequired(), EqualTo('password')])