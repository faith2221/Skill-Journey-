import sqlite3
import click
from pathlib import Path
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_db():
    db = get_db()
    schema_paths = Path().glob('**/*.sql')
    schema_paths = sorted(schema_paths)
    for path_obj in schema_paths:
        with path_obj.open() as f:
            db.executescript(f.read())

@click.command('create-db')
@with_appcontext
def db_command():
    """Create the database."""
    create_db()
    click.echo('Created database')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(db_command)