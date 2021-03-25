from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
  now = datetime.now()
  timeString = now.strftime("%m-%d-%Y %I:%M %p")
  data = {
          'title' : 'Home',
          'time'  : timeString
          }
  return render_template('home.html', **data)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success', name = user))
   else:
      return render_template('login.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
