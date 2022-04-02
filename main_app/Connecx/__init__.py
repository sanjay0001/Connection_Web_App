from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Quora.db'
app.config['SECRET_KEY']='2418faa391fc381ac9f81b29'
db=SQLAlchemy(app)

from Connecx import routes
