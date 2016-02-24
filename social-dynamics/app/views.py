from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template("homepage/index.html")

@app.route('/systems/system1')
def system1():
  return render_template("/systems/system1.html")

@app.route('/systems/system2')
def system2():
  return render_template("/systems/system2.html")

@app.route('/systems/system3')
def system3():
  return render_template("/systems/system3.html")

@app.route('/organizations/org1')
def org1():
  return render_template("/organizations/org1.html")

@app.route('/organizations/org2')
def org2():
  return render_template("/organizations/org2.html")

@app.route('/organizations/org3')
def org3():
  return render_template("/organizations/org3.html")

@app.route('/networks/')
def networks():
  return render_template("networks.html")

@app.route('/partners/')
def partners():
  return render_template("partners.html")