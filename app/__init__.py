import os
from flask import Flask, send_from_directory
from pathlib import Path

# Configure the app
def create_app():
    """ Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=str(Path(app.instance_path) / 'db.sqlite3'),
        SECRET_KEY='dev',
        UPLOAD_FOLDER=Path(__file__).parent / 'uploads'
    )

    # Ensure the instance folder exists
    try:
        Path(app.instance_path).mkdir(exist_ok=True)
    except OSError:
        pass

    # Registering the Blueprints
    from app.users.views import bp as user_bp
    app.register_blueprint(user_bp)

    from app.skills.views import bp as skills_bp
    app.register_blueprint(skills_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app import db
    db.init_app(app)

    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    @app.route('/uploads/<filename>')
    def uploads(filename):
        """ Serve uploaded files."""
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    return app