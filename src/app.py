# from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)

# app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
# app.config['BABEL_DEFAULT_LOCALE']          = 'es'
# app.config['LANGUAGES']                     = {
#     'es': 'Español',
#     'en': 'English'
# }

# def get_locale():
#     return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# babel = Babel(app, locale_selector = get_locale)

# MAIN PAGES
@app.route('/')
def home_controller():
    title = 'Inicio - Trivias UCV'
    return render_template('home/homePage.html', title = title)

@app.route('/play')
def play_controller():
    title = 'Jugar - Trivias UCV'
    return render_template('play/playPage.html', title = title)

@app.route('/rankings')
def rankings_controller():
    title = 'Rankings - Trivias UCV'
    return render_template('rankings/rankingsPage.html', title = title)

@app.route('/awards')
def awards_controller():
    title = 'Premios - Trivias UCV'
    return render_template('awards/awardsPage.html', title = title)

@app.route('/profile')
def profile_controller():
    title = 'Perfil - Trivias UCV'
    return render_template('profile/profilePage.html', title = title)

@app.route('/settings')
def settings_controller():
    title = 'Configuración - Trivias UCV'
    return render_template('settings/settingsPage.html', title = title)

@app.route('/help')
def help_controller():
    title = 'Ayuda - Trivias UCV'
    return render_template('help/helpPage.html', title = title)

# AUTH PAGES
@app.route('/auth/login')
def login_controller():
    title           = 'Iniciar Sesión - Trivias UCV'
    principal_title = 'Bienvenid@'
    return render_template('auth/loginPage.html', title = title, principal_title = principal_title)

@app.route('/auth/register')
def register_controller():
    title           = 'Registro - Trivias UCV'
    principal_title = 'Regístrate'
    return render_template('auth/registerPage.html', title = title, principal_title = principal_title)

@app.route('/auth/forget-password')
def forget_password_controller():
    title           = 'Recuperar Contraseña - Trivias UCV'
    principal_title = 'Recuperar Contraseña'
    return render_template('auth/forgetPasswordPage.html', title = title, principal_title = principal_title)

@app.route('/auth/new-password')
def new_password_controller():
    title           = 'Recuperar Contraseña - Trivias UCV'
    principal_title = 'Bienvenid@ de Nuevo'
    return render_template('auth/newPasswordPage.html', title = title, principal_title = principal_title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')