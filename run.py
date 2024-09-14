from app import create_app  # Import the create_app function from the app module

app = create_app()  # Create an instance of the Flask application by calling create_app()

if __name__ == '__main__':  # Check if the script is being run directly (not imported)
    app.run(debug=True)  # Run the Flask application in debug mode
