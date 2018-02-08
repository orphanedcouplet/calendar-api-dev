from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:password@localhost:8889/databasename"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "jfkewal;2fdjkasdfmn,##J09#)(@_#(SHRugemoji4jq839fp0jefjkls;dkj034890-cvm+....3r3wwwrrrrrrrrrrr&#fjio(*"


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    events = db.relationship("Event", backref="user")

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return "<User %r>" % self.username


class Event(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.Location, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", backref="author_events", foreign_keys=[author_id])

    def __init__(self, title, description, location, author, date):
        self.title = title
        self.description = description
        self.location = location
        self.author = author
        # TODO look at Python DateTime docs, figure out how to set DateTime instances
        self.date = date
    
    def __repr__(self):
        return "<Event %r>" % self.title


class Location(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(500))

    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __repr__(self):
        return "<Location %r>" % self.name

def index():
    return True

app.run()
