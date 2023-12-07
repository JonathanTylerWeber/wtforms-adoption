from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = StringField('Picture', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    notes = StringField('Notes on pet', validators=[Optional()])
    available = BooleanField('Is this pet available?')