import flask 
import random
from flask import Blueprint, render_template, url_for, current_app
import os

main = Blueprint('main', __name__)


@main.route('/')
def home():
    # Path to the images folder using current_app in a Blueprint
    images_folder = os.path.join(current_app.static_folder, 'images')
    
    # List all images in the directory
    images = os.listdir(images_folder)
    
    # Select a random image
    random_image = random.choice(images)
    
    # Build the URL for the selected image
    image_url = url_for('static', filename=f'images/{random_image}')
    
    return render_template('index.html', image_url=image_url)
