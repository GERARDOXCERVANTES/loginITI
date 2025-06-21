from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from .models.ModelUser import ModelUser
from .models.entities.user import  User




app = Flask(__name__)
db = SQLAlchemy(app)

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
                return render_template('User.html')
        #print(request.form.get('username'))
        #print(request.form.get('password'))
            else:
                flash('opps.. ocurrio un error verifique cotrasena :)')
                return render_template('login.html')
        else:
            flash('opss... user no found :)')
            return render_template('login.html')  
    else:
        return render_template('login.html')
    
