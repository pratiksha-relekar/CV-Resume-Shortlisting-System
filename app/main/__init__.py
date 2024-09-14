from flask import Blueprint  # Import the Blueprint class from the Flask module

# Create a Blueprint instance named 'main'
main = Blueprint('main', __name__, template_folder='templates')

from . import routes  # Import routes from the current package to register with the Blueprint
