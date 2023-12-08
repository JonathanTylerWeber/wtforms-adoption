from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])

    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="must be 'cat', 'dog', or 'porcupine'")])

    photo_url = StringField('Picture', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Please enter a number between 0 and 30.")])

    notes = StringField('Notes on pet', validators=[Optional()])
    
    available = BooleanField('Is this pet available?')