from logging import debug
from flask import Flask, render_template, url_for, flash
from werkzeug.utils import redirect
from forms import RegistrationForm, LoginForm
 
app = Flask(__name__)

# configure secret key 
app.config['SECRET_KEY'] = '66166091d57a2fd226757403e0335d7f'

posts=[{
    'deceased':'Jhon dow',
    'dod':'February 21, 2021',
    'location':'Delhi/India'
},
{
    'deceased':'Maddem Mercury',
    'dod':'July 18, 2020',
    'location':'Arkensawl/USA'
},
{
    'deceased':'Mr Dead Bird',
    'dod':'Feb 29, 2020',
    'location':'Okhla Bird Sanctuary/Delhi'
},
{
    'deceased':'Bilbo Baggins',
    'dod':'31 Dec, 2021',
    'location':'The Shire/Middle Earth'
},
{
    'deceased':'Damn its Van Dam',
    'dod':'04 July, 2021',
    'location':'the Ring of fire/Japan'
},
{
    'deceased':'Jhon dow',
    'dod':'February 21, 2021',
    'location':'Delhi/India'
},
{
    'deceased':'Maddem Mercury',
    'dod':'July 18, 2020',
    'location':'Arkensawl/USA'
},
{
    'deceased':'Mr Dead Bird',
    'dod':'Feb 29, 2020',
    'location':'Okhla Bird Sanctuary/Delhi'
},
{
    'deceased':'Bilbo Baggins',
    'dod':'31 Dec, 2021',
    'location':'The Shire/Middle Earth'
},
{
    'deceased':'Damn its Van Dam',
    'dod':'04 July, 2021',
    'location':'the Ring of fire/Japan'
}
]
 
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("email address {{ form.email }} is registered. kindly Sign In.", category="success")
        return redirect('login')
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('register.html', title="Sign In", form=form)
 
@app.route("/about")
def about():
    return render_template('about.html', title="about")
 
if __name__ == '__main__':
    app.run(debug=1)

