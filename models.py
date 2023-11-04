from flask_sqlalchemy import SQLAlchemy  

db=SQLAlchemy()

def connect_db(app):
    db.app=app
    db.init_app(app)
    
class Pet(db.Model):
    """Pets for adoption"""
    __tablename__='pets'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, default="https://static.wikia.nocookie.net/spongebobgalaxy/images/c/cd/Gary_the_Snail.png/revision/latest/scale-to-width-down/180?cb=20171105152328")
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    def __repr__ (self):
        return f"<Pet: {self.name}, Available: {self.available}>"