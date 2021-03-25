from flask import Flask, render_template, redirect, url_for, request
from apis.weatherapi import get_temp
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
  data = {
          'title'  : 'Home',
          'date'   : datetime.now().strftime("%m-%d-%Y"),
          'time'   : datetime.now().strftime("%I:%M %p"),
          #'weather': requests.get('http://192.168.1.25/API?user=testuser'),
          'temp': str(get_temp()) + " F"
          }
  return render_template('home.html', **data)

@app.route('/greetme/<name>')
def greet(name):
   return 'welcome %s' % name

@app.route('/greetme', methods = ['POST', 'GET'])
def greetme():
  if request.method == 'POST':
    user = request.form['name']
    return redirect(url_for('greet', name = user))
  else:
    return render_template('greet.html')

@app.route('/API', methods = ['GET'])
def API():
  user = request.args.get('user')
  if user:
    return "User: " + str(user)
  else:
    return "API here, no user specified"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
