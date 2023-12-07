from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    species = db.Column(db.String(20), nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Pet id = {self.id}, name = {self.name}, species = {self.species}, photo url = {self.photo_url}, age = {self.age}, notes = {self.notes}, available = {self.available}>"