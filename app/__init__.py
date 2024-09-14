from flask import Flask  # Import the Flask class from the flask module
from flask_bootstrap import Bootstrap  # Import the Bootstrap extension for Flask
from config import Config  # Import the Config class from a config module

# Function to create and configure the Flask application
def create_app():
    # Initialize the Flask app with custom static and template folders
    app = Flask(__name__, static_folder='main/static', template_folder='main/templates')
    
    # Load the configuration settings from the Config class
    app.config.from_object(Config)

    # Initialize the Bootstrap extension with the Flask app
    Bootstrap(app)

    # Import and register the main Blueprint with the Flask app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Return the configured Flask app
    return app
