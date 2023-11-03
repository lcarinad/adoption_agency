from flask import Flask, render_template, request, redirect, flash, session
from models import db, connect_db, Pet

app = Flask(__name__)
# app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='abc123'

app.app_context().push()
connect_db(app)

@app.route('/')
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)