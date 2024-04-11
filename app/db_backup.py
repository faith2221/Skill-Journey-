import os
import shutil
import datetime
from pathlib import Path
from flask import current_app     

def backup_database():
        """ Backup the database."""
        source = current_app.config['DATABASE']
        backup_folder = Path(current_app.instance_path) / 'backup'
        os.makedirs(backup_folder, exist_ok=True)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        backup_name = f'db_backup_{timestamp}.sqlite3'
        destination = backup_folder / backup_name
        shutil.copy(source, destination)
        return 'Backup created successfully'