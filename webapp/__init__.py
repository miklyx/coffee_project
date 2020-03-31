from flask import Flask, render_template

from webapp.forms import Input_roast, Input_File
from webapp.model import db, lots, measure_types, roasters, roastings, temperature

def create_app():

  app = Flask(__name__)
  app.config.from_pyfile('config.py')
  db.init_app(app)

  @app.route('/')          # main page
  def index(): 
    title = "Tiger"
  
  @app.route('/input_roast')
  def input_roast():
    title = "Input Roasting"
    input_form = Input_roast()
    return render_template('input.html', page_title=title, form = input_form)

  @app.route('/input_file')
  def input_file():
    title = "Input roasting file"
    input_form = Input_File()
    return render_template('input_file.html', page_title=title, form = input_form)
    
  return app 

