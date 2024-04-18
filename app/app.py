from app import create_app

# Create the flask application
app = create_app()

if __name__ == '__main__':
    # Run the flask application
    app.run(debug=True)