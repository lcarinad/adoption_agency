from flask import Flask, render_template, request, redirect, flash, session
from models import db, connect_db, Pet
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""
    form = AddPetForm()
   
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        if not photo_url:
            photo_url = Pet.photo_url.default.arg
            
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"You added {name} the {species}!")
        return redirect("/add")
    
        
    else:    
        return render_template('pet_add_form.html', form = form)

@app.route("/<int:id>", methods=["GET", "POST"])
def show_pet(id):
    """Shows details about single pet"""
    pet = Pet.query.get_or_404(id)
    
    form = AddPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect(f'/{id}')
    return render_template("show_pet.html", pet = pet, form= form)