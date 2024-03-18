from flask import Flask, render_template, request
from models import db, User
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = b'123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
app.app_context().push()
db.create_all()


@app.get('/')
def index_get():
    return render_template('index.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest()
    user = User(name=name, last_name=last_name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return f'Added user {name}<br><br>OK'
