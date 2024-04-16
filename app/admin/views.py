from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from app.db import get_db
from app.db_backup import backup_database
from app.users.login_utils import login_required
from app.utils import form_errors, validate

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def dashboard():
    """ Route to render the admin dashboard, restricted to authenticated users"""
    return render_template('admin/dashboard.html')

@bp.route('/backup', methods=['POST', 'GET'])
@login_required
def backup():
    """ Route to backup the database """
    if request.method == 'POST':
        backup_database()
        # Logic to backup the database
        flash('Database backed up successfully', 'success')
        return redirect(url_for('admin.dashboard'))
    
    # Handles GET request
    else:
        return render_template('admin/backup.html')

@bp.route('/backup/restore', methods=['POST', 'GET'])
@login_required
def restore():
    """ Route to restore the database """
    if request.method == 'POST':
        # Logic to restore the database
        flash('Database restored successfully', 'success')
        return redirect(url_for('admin.dashboard'))
    
    # Handles GET request
    else:
        return render_template('admin/restore.html')


