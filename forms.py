from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Optional,URL, AnyOf

class AddPetForm(FlaskForm):
    """Form to add pet"""
    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField("Species", validators = [InputRequired(), AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo_url", validators = [URL(), Optional()])
    age = IntegerField("Age", validators = [Optional(), NumberRange(0, 30)])
    notes = StringField("Notes", validators = [Optional()])
