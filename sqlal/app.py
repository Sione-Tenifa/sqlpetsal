

from flask import Flask, request, redirect, render_template, flash, session
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    pets = Pet.query.all()

    return render_template('list.html', pets=pets)

@app.route("/<int:pet_id>")
def show_pet(pet_id):
    """show pet details"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('details.html', pet=pet)
