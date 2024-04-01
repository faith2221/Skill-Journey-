import sqlite3
import click
from pathlib import Path
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

def init_app(app):
    """ Register database functions with the Flask app."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(db_command)
    app.cli.add_command(create_admin_command)

def create_db():
    """Create the database tables."""
    db = get_db()
    schema_paths = list(Path().glob('**/*.sql'))
    schema_paths = sorted(schema_paths)
    for path_obj in schema_paths:
        with path_obj.open() as f:
            db.executescript(f.read())

def create_admin(first_name, last_name, email, password):
    """ Create an admin user."""
    db = get_db()
    db.execute("""INSERT INTO users (first_name, last_name, email, password,
    is_admin) VALUES (?, ?, ?, ?, ?)""", (first_name, last_name, email, password))
    db.commit()

@click.command('create-db')
@with_appcontext
def db_command():
    """Create the database."""
    create_db()
    click.echo('Created database')

@click.command('create_admin')
@with_appcontext
def create_admin_command():
    """ Create an admin user."""
    first_name = click.prompt('First Name', default='Edith')
    last_name = click.prompt('Last Name', default='Banda')
    email = click.prompt('Email', default='edithbanda014@gmail.com')
    password = click.prompt('Password', hide_input= True)
    create_admin(first_name, last_name, email, generate_password_hash(password))
    click.echo('Created admin user')

def get_db():
    """Connect to the application's configured database."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """ Close the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()