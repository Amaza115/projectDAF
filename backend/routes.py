import flask 
import random
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# List of raccoon images
raccoon_images = [
    "https://example.com/raccoon1.jpg",
    "https://example.com/raccoon2.jpg",
    "https://example.com/raccoon3.jpg",
    "https://example.com/raccoon4.jpg"
]

@main.route('/')
def home():
    image_url = random.choice(raccoon_images)
    return render_template('index.html', image_url=image_url)