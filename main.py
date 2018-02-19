from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://calendar-api-dev:QEhrQXQZCSNns9L2@localhost:8889/calendar-api-dev"
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

    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=False)
    location = db.relationship("Location", backref="location_events", foreign_keys=[location_id])

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

    events = db.relationship("Event", backref="location")

    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __repr__(self):
        return "<Location %r>" % self.name


# HANDLERS!

@app.route("/", methods=["POST", "GET"])
def index():
    
    title = "Event Calendar"

    events = Event.query.order_by(Event.date).all()

    return render_template("index.html", title=title, events=events)

app.run()
