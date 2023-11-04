from models import Pet, db
from app import app
db.drop_all()
db.create_all()

Pet.query.delete()

fluffy = Pet(name='Fluffy', species='Dog', photo_url='https://media-be.chewy.com/wp-content/uploads/2019/10/24131108/chinweenie-pup.jpg',
             age=3, notes='Friendly and playful', available=False)
whiskers = Pet(name='Whiskers', species='Cat', photo_url='https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg',
               age=2, notes='Loves to cuddle', available=True)
bubbles = Pet(name='Hammy', species='Porcupine', photo_url='https://media.istockphoto.com/id/119869206/photo/four-toed-hedgehog-atelerix-albiventris-3-weeks-old-white-background.jpg?s=612x612&w=0&k=20&c=HegzlayFTAZ2gJ0dg85SxGxm3-21LxeIAjh17mALgAw=',
               age=None, notes=None, available=True)

db.session.add_all([fluffy, whiskers, bubbles])
db.session.commit()