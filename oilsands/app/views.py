from flask import render_template, flash, redirect, request
from app import app
from app.lib.mailer import SendGrid
from config import GMAIL

@app.route('/')
@app.route('/index')
def index():
  return render_template("homepage/index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/oilsands/')
def oilsands():
  return render_template("oilsands.html")

@app.route('/wind')
def wind1():
  return render_template("/wind/wind.html")

@app.route('/solar')
def solar1():
  return render_template("/solar/solar.html")

@app.route('/hybrid')
def hybrid():
  return render_template("hybrid.html")

@app.route('/paper/')
def paper():
  return render_template("paper.html")

@app.route('/contact/')
def contact():
  return render_template("contact.html")

@app.route('/contact/', methods=['POST','GET'])
def contact_msg():
  error = None
  if request.method == 'POST':
    name  = request.form['name']
    email = request.form['email']
    message  = request.form['message']

  if name == '':
    error = 'Full name required.'
    return render_template('contact.html', error=error)
  elif email == '':
    error = 'Email required.'
    return render_template('contact.html', error=error)
  elif message == '':
    error = 'Message required.'
    return render_template('contact.html', error=error)
  
  content = 'Name: ' + name + '\n\n'  + 'Email: ' + email + '\n\n' + 'Message: ' + message

  sg = SendGrid()
  sg.send(
    origin = GMAIL,
    destination = [GMAIL],
    subject = 'Oilsands Symbiotic Development (PERG) Message',
    content = content,
    )
  return render_template('contact.html', msg='Message Sent!')
