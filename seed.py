from models import Pet, db
from app import app
db.drop_all()
db.create_all()

Pet.query.delete()

fluffy = Pet(name='Fluffy', species='Dog', photo_url='https://media-be.chewy.com/wp-content/uploads/2019/10/24131108/chinweenie-pup.jpg',
             age=3, notes='Friendly and playful', available=False)
whiskers = Pet(name='Whiskers', species='Cat', photo_url='https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg',
               age=2, notes='Loves to cuddle', available=True)
bubbles = Pet(name='Bubbles', species='Fish', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzp8bihi179-GmniXboTsMBGvLXbRFlTUUD_HJq8d7cN6B2Z4TpKGSvkzkSvo7-k8X1qM&usqp=CAU',
               age=1, notes='Beautiful colors', available=True)

db.session.add_all([fluffy, whiskers, bubbles])
db.session.commit()