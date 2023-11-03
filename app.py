from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
app = Flask(__name__)
app.config['SECRET_KEY']='abc123'
app.config["SQLALCHEMY_DATABASE_URL"] = "postgresql:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.debug = True

toolbar=DebugToolbarExtension(app)