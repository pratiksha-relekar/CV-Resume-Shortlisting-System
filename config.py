import os  # Import the os module for interacting with the operating system

class Config:  # Define a configuration class named Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4e5b4d1f2c3d4a2b5e6f7a8b9c0d1e2f'  # Set the SECRET_KEY attribute, using an environment variable if available, otherwise defaulting to a hardcoded string
