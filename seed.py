from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name='Kali', species='cat', photo_url='https://i.pinimg.com/736x/ab/c4/8b/abc48b4afe75a9c72f5cc162e6bf2be9.jpg', age='4', notes="cute and doesn't like other cats", available=True)
p2 = Pet(name='Bob', species='dog', photo_url='https://www.petlandflorida.com/wp-content/uploads/2019/09/Petland_Florida_Cavalier_King_Charles_Spaniel_puppy.jpg', age='5', notes="the most loveable creature alive", available=True)
p3 = Pet(name='Jingle', species='porcupine', photo_url='https://images.saymedia-content.com/.image/t_share/MTc0NDM2NjU2NDU4MjQ1NDgw/names-for-pet-hedgehogs-porcupines-and-tenrecs.jpg', age='2', notes="only pokes you sometimes", available=True)

pets = [p1, p2, p3]
db.session.add_all(pets)
db.session.commit()

