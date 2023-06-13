from pymongo import MongoClient
from flask import Flask, redirect, render_template, request, url_for, jsonify
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

# Forms Validation
from forms.register import RegistrationForm
from forms.login import LoginForm
from forms.forgetPassword import ForgetPasswordForm
from forms.newPassword import NewPasswordForm

# Models
from models.model_user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '0ZeX5A9qzA'

login_manager = LoginManager()
login_manager.init_app(app)

def ConexionMongo():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["bd_trivia"]
    return db

def inject_user():
    return dict(current_user=current_user)

app.context_processor(inject_user)

# MAIN PAGES
@app.route('/')
def home_controller():
    title = 'Inicio - Trivias UCV'
    return render_template(
        'home/homePage.html', 
        title = title
    )

@app.route('/play')
def play_controller():
    title = 'Jugar - Trivias UCV'
    return render_template(
        'play/playPage.html', 
        title = title
    )

@app.route('/game')
def quiz_controller():
    title = 'Jugar - Trivias UCV'
    return render_template(
        'play/gamePage.html',
        title = title
    )

@app.route('/rankings')
def rankings_controller():
    title = 'Rankings - Trivias UCV'
    return render_template(
        'rankings/rankingsPage.html', 
        title = title
    )

@app.route('/awards')
def awards_controller():
    title = 'Premios - Trivias UCV'
    return render_template(
        'awards/awardsPage.html', 
        title = title
    )

@app.route('/profile')
def profile_controller():
    title = 'Perfil - Trivias UCV'
    return render_template(
        'profile/profilePage.html', 
        title = title
    )

@app.route('/settings')
def settings_controller():
    title = 'Configuración - Trivias UCV'
    return render_template(
        'settings/settingsPage.html', 
        title = title
    )

@app.route('/help')
def help_controller():
    title = 'Ayuda - Trivias UCV'
    return render_template(
        'help/helpPage.html', 
        title = title
    )

# USERS
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# AUTH PAGES
@app.route('/auth/login', methods=['GET', 'POST'])
def login_controller():
    title           = 'Iniciar Sesión - Trivias UCV'
    principal_title = 'Bienvenid@'

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # alias = form.alias.data
        # password = form.password.data
        user = User.get(2)
        if user: 
            login_user(user)
            return redirect(url_for('home_controller')) 
    
    return render_template(
        'auth/loginPage.html', 
        title = title, 
        principal_title = principal_title, 
        form = form
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_controller'))

@app.route('/auth/register', methods=['GET', 'POST'])
def register_controller():
    title           = 'Registro - Trivias UCV'
    principal_title = 'Regístrate'

    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('login_controller'))
    
    return render_template(
        'auth/registerPage.html', 
        title = title, 
        principal_title = principal_title, 
        form = form
    )

@app.route('/auth/forget-password', methods=['GET', 'POST'])
def forget_password_controller():
    title           = 'Recuperar Contraseña - Trivias UCV'
    principal_title = 'Recuperar Contraseña'

    form = ForgetPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('new_password_controller'))
    
    return render_template(
        'auth/forgetPasswordPage.html', 
        title = title, 
        principal_title = principal_title, 
        form = form
    )

@app.route('/auth/new-password', methods=['GET', 'POST'])
def new_password_controller():
    title           = 'Recuperar Contraseña - Trivias UCV'
    principal_title = 'Bienvenid@ de Nuevo'

    form = NewPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('login_controller'))
    
    return render_template(
        'auth/newPasswordPage.html', 
        title = title, 
        principal_title = principal_title, 
        form = form
    )

@app.route('/usuarios')
def get_stored_usuarios():
    db = ConexionMongo()
    _usuarios = db.usuario_tb.find()
    usuarios = [{"id_user": usuario["id_user"], 
                 "name_user": usuario["name_user"], 
                 "alias": usuario["alias"], 
                 "email": usuario["email"], 
                 "fec_creacion": usuario["fec_creacion"], 
                 "fec_nacimiento": usuario["fec_nacimiento"], 
                 "facebook": usuario["facebook"], 
                 "twitter": usuario["twitter"], 
                 "tipo_usuario": usuario["tipo_usuario"], 
                 "posicion_ranking": usuario["posicion_ranking"], 
                 "imagen": usuario["imagen"], 
                 "puntaje": usuario["puntaje"], 
                 "ganador_sorteo": usuario["ganador_sorteo"]} for usuario in _usuarios]
    return jsonify({"usuarios": usuarios})

# MAIN
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')