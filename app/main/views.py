from . import main
from flask import render_template, url_for

@main.route('/')

def index():
  return render_template('index.html')