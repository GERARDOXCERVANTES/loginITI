from flask import Flask,render_template,redirect,url_for,request,flash
from models.ModelUser import ModelUser
from models.entities.user import  User
from config.Config import DatabaseConnection, Conn
from flask_login import LoginManager,login_user,logout_user,login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
db_config = Conn()
db = DatabaseConnection(config=db_config)
login_manager = LoginManager(app)

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
                return render_template('User.html')
            else:
                flash('Estas credenciales no son validas')
                return render_template('login.html')  
        #print(request.form.get('username'))
        #print(request.form.get('password'))
            
        else:
            flash('Estas credenciales no son validas')
            return render_template('login.html')  
    else:
        return render_template('login.html')
    
