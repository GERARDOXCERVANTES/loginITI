from flask import Flask,render_template,redirect,url_for,request,flash
from models.ModelUser import ModelUser
from models.entities.user import  User
from config.Config import DatabaseConnection, Conn
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
db_config = Conn()
db = DatabaseConnection(config=db_config)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return ModelUser.by_id(db, user_id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(
            request.form.get('username'),
            request.form.get('password')
        )
        login_check = ModelUser.login(db,user)
        if login_check != None:
            if login_check.password:
                login_user(login_check)
                return redirect(url_for('home'))
            else:
                flash('Estas credenciales no son validas')
                return render_template('login.html')  
        else:
            flash('Estas credenciales no son validas')
            return render_template('login.html')  
    else:
        return render_template('login.html')
    
    
@app.route('/home')
@login_required
def home():
    
    return render_template('home.html')

def status_401(e):
    return redirect(url_for('login'))

def status_404(e):
    return "<h1>Page not found</h1>",404
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)