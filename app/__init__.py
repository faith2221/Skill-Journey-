import os
import datetime
from flask import Flask, send_from_directory
from pathlib import Path
from app.db_backup import backup_database

# Configure the app
def create_app():
    """ Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=str(Path(app.instance_path) / 'db.sqlite3'),
        SECRET_KEY='skill',
        ALLOWED_EXTENSIONS ={'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif'}
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

    from app.admin.views import bp as admin_bp
    app.register_blueprint(admin_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Initialize the database and backup
    from app import db
    db.init_app(app)
    
    return app