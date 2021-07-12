from logging import debug
from typing import Text
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from wtforms.fields.simple import PasswordField
from wtforms.validators import Email
from forms import RegistrationForm, LoginForm
from datetime import datetime
 
app = Flask(__name__)

# configure secret key 
app.config['SECRET_KEY'] = '66166091d57a2fd226757403e0335d7f'
# configure SQLite3 database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# create a database instance 
db = SQLAlchemy(app)

# create database table classes 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False )
    password = db.Column(db.String(60), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='creator', lazy=True )
    comments = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False )
    dobirth = db.Column(db.Integer)
    doexpiery = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    profile_img = db.Column(db.String(20), nullable=False, default='default.jpg')
    orbituary = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='owner', lazy=True)

    def __repr__(self):
        return f"Post('{self.name}', '{self.dobirth}','{self.doexpiery}', '{self.location}', '{self.user_id}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    like = db.Column(db.Integer)
    Text = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.user_id}', '{self.post_id}','{self.Text}', '{self.datetime}')"

posts=[{
    'deceased':'Jhon dow',
    'dod':'February 21, 2021',
    'location':'Delhi/India',
    'image': 'static/dog.jfif'
},
{
    'deceased':'Maddem Mercury',
    'dod':'July 18, 2020',
    'location':'Arkensawl/USA',
    'image': 'static/person.jpg'
},
{
    'deceased':'Mr Dead Bird',
    'dod':'Feb 29, 2020',
    'location':'Okhla Bird Sanctuary/Delhi',
    'image': 'static/deadbird.jpg'
},
{
    'deceased':'Bilbo Baggins',
    'dod':'31 Dec, 2021',
    'location':'The Shire/Middle Earth',
    'image': 'static/sqperson.jfif'
},
{
    'deceased':'Damn its Van Dam',
    'dod':'04 July, 2021',
    'location':'the Ring of fire/Japan',
    'image': 'static/Computer.jpg'
    
},
{
    'deceased':'Jhon dow',
    'dod':'February 21, 2021',
    'location':'Delhi/India',
    'image': 'static/dog.jfif'
},
{
    'deceased':'Maddem Mercury',
    'dod':'July 18, 2020',
    'location':'Arkensawl/USA',
    'image': 'static/person.jpg'
},
{
    'deceased':'Mr Dead Bird',
    'dod':'Feb 29, 2020',
    'location':'Okhla Bird Sanctuary/Delhi',
    'image': 'static/deadbird.jpg'
},
{
    'deceased':'Bilbo Baggins',
    'dod':'31 Dec, 2021',
    'location':'The Shire/Middle Earth',
    'image': 'static/sqperson.jfif'
},
{
    'deceased':'Damn its Van Dam',
    'dod':'04 July, 2021',
    'location':'the Ring of fire/Japan',
    'image': 'static/bird2.jpg'
    
}
]
 
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"User with email address { form.email.data } is registered. kindly Sign In.", category="success")
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email == "gildedvisions@gmail.com" and password == "123":
            return redirect(url_for('home'))
        else:
            flash('login unsuccessfull. Please check email address and password', category="danger")
    return render_template('login.html', title="Sign In", form=form, email=email)
 
@app.route("/about")
def about():
    return render_template('about.html', title="about")
 
if __name__ == '__main__':
    app.run(debug=1)

