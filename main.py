# Banking Website
from flask import Flask, render_template, request, session, url_for, redirect

from flask.globals import request

from functions import Bank

app = Flask(__name__)
users = {}
print(users)
app.secret_key = 'hkjkjhfkjdh1357526%$^"£"'


@app.route('/')
def homepage():
  if 'user' in session:
    money = user.view_money()
    return render_template('homepage.html', money=money)
  else:
    return render_template('homepage.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
  global user
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
      session['user'] = username

      user = Bank(session['user'])

      print(user.show_details())

      print('Login Successful')
      return render_template('homepage.html')
    else:
      print('Username dosent exist or wrong password')
      return render_template('login.html')
      

  return render_template('login.html')

@app.route('/register', methods= ['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    if username in users:
      print('User already exists')
      return render_template('register.html')
    else:
      password = request.form['password']
      users[username] = password
      print('user created')
      print(users)
      return render_template('homepage.html')
  else:
    return render_template('register.html')


@app.route('/deposit', methods = ['GET', 'POST'])
def deposit():
  if request.method == 'POST':
    amount = request.form['deposit']
    user.deposit(amount)
    print(user.show_details())
    return render_template('deposit.html')
  else:
    return render_template('deposit.html')

@app.route('/withdraw', methods = ['GET', 'POST'])
def withdraw():
  if request.method == 'POST':
    amount = request.form['withdraw']
    user.withdraw(amount)
    print(user.show_details())
    return render_template('withdraw.html')
  else:
    return render_template('withdraw.html')

@app.route('/logout')
def logout():
  session.pop('user', None)
  return redirect(url_for('homepage'))
  


if __name__ == "__main__":
  app.run(debug=True)






