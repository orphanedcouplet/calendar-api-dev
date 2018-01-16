from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://databasename:databasepassword@localhost:8889/something"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Event(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(300), nullable=False)

def index():
    return True

app.run()
