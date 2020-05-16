import json
from flask_login import LoginManager, current_user, login_user, login_required,logout_user
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError
from models import db, User
from forms import LogIn



''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    login_manager.login_message = u"Please login to view this page"
    login_manager.login_view = "/Login"
    return User.query.get(user_id)


''' End Flask Login Functions '''
''' Begin boilerplate code '''


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  login_manager.init_app(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/user',methods=['GET'])
@login_required
def user():
  return render_template('personal_user.html')


@app.route('/search')
def search():
	return render_template('search.html')

@app.route('/app')
def indx():
	return render_template('index.html')
  
@app.route('/Login', methods=['POST','GET'])
def login():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
    data = request.form
    user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully. Go to My Account to see your grocery list.') 
      login_user(user) # login the user
      # redirect to main page if login successful
    else:
      flash('Invalid username or password') # send message to next page
      return redirect(url_for('index')) # redirect to login page if login unsuccessful
  return render_template('Login.html', form=form)

@app.route('/register',methods=['POST','GET'])
def register():
  return render_template('register.html')

@app.route('/signup', methods=['POST'])
def signup():
  userdata = request.get_json() # get userdata
  print(userdata)
  newuser = User(username=userdata['username'], email=userdata['email']) # create user object
  newuser.set_password(userdata['password']) # set password
  try:
    db.session.add(newuser)
    db.session.commit() # save user
  except IntegrityError: # attempted to insert a duplicate user
    db.session.rollback()
    return 'Username or email already exists' # error message
  return 'User created' # success

@app.route('/Logout')
def logout():
  logout_user()
  return redirect(url_for('index'))



app.run(host='0.0.0.0', port=8080,debug=False)