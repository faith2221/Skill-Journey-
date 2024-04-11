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

@bp.route('/users')
@login_required
def view_all_users():
    """ Route to view all users """
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('admin/view_all_users.html', users=users)

@bp.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    """ Logic to delete a user"""
    db = get_db()
    
    # Delete user
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()

    flash('User deleted successfully', 'success')
    return redirect(url_for('admin.view_all_users'))

@bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_user_post(post_id):
    """ Logic to delete a user post"""
    db = get_db()
    
    # Delete user posts
    db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    db.commit()

    flash('Post deleted successfully', 'success')   
    return redirect(url_for('admin.view_all_users'))

@bp.route('/comments/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_user_comment(comment_id):
    """ Logic to delete a user comment"""
    db = get_db()
   
    # Delete comment
    db.execute ('DELETE FROM comments WHERE id = ?', (comment_id,))
    db.commit()

    flash('Comment deleted successfully', 'success')
    return redirect(url_for('admin.view_all_users'))

@bp.route('/logs')
@login_required
def view_logs():
    """ Route to view logs """
    db = get_db()

    # Logic to retrieve and display logs
    logs = db.execute('SELECT * FROM logs').fetchall()
    return render_template('admin/view_logs.html', logs=logs)

@bp.route('/logs/<int:log_id>/delete', methods=['POST'])
@login_required
def delete_logs(log_id):
    """ Logic to delete a log"""
    db = get_db()
 
    # Delete log
    db.execute('DELETE FROM logs WHERE id = ?', (log_id,))
    db.commit()

    flash('Log deleted successfully', 'success')
    return redirect(url_for('admin.view_logs'))

@bp.route('/analytics')
@login_required
def analytics():
    """ Route to view analytics """
    db = get_db()
    
    # Logic to retrieve and display analytics
    analytics = db.execute('SELECT * FROM analytics').fetchall()

    return render_template('admin/analytics.html', analytics=analytics)

@bp.route('/analytics/<int:analytics_id>/delete', methods=['POST'])
@login_required
def delete_analytics(analytics_id):
    """ Logic to delete analytics"""
    db = get_db()
    
    # Delete analytics
    db.execute('DELETE FROM analytics WHERE id = ?', (analytics_id,))
    db.commit()
    
    flash('Analytics deleted successfully', 'success')
    return redirect(url_for('admin.analytics'))

@bp.route('/backup')
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

@bp.route('/backup/restore')
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


