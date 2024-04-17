import math
from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from app.users.login_utils import login_required
from app.db import get_db
from app.db_backup import backup_database
from datetime import datetime
from app.utils import form_errors, validate
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('skills', __name__, url_prefix='/skills')

@bp.route('/media')
@login_required
def view_media():
    """ Route to view media resources """
    db = get_db()

    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = 6

    # Search query 
    search_query = request.args.get('search_query', '').strip()
    search_filter = '%' + search_query + '%'

    # Retrieve total number of media links for pagination
    total_media = db.execute("""SELECT COUNT(*) FROM media WHERE title LIKE ?""",
                             (search_filter,)).fetchone()[0]
    
    # Calculate the total number of pages
    total_pages = math.ceil(total_media / per_page)

    # Retrieve media links for the current page
    offset = (page - 1) * per_page
    media_links = db.execute("""SELECT title, url
                             FROM media
                             WHERE  title LIKE ?
                             ORDER BY id DESC
                             LIMIT ? OFFSET ?""",
                             (search_filter, per_page, offset)).fetchall()
    
    return render_template('skills/view_media.html', media_links=media_links,
                           total_pages=total_pages, current_page=page)


@bp.route('/comments/add', methods=['GET', 'POST'])
@login_required
def add_comment():
    """ Logic to add a comment to a post"""
    if request.method == 'POST':
        content = request.form['content']

        if not content:
            flash('Content is required!')

        else:        
            user_id = g.user['id']

            # Validate Input
            with get_db() as db:
                db.execute("""INSERT INTO comments (content, user_id, created_at)
                       VALUES (?, ?, ?)""", (content, user_id, datetime.utcnow()))   
                db.commit()
            return redirect(url_for('skills.view_all_comments'))
    return render_template('skills/add_comment.html')

@bp.route('/comments', methods=['GET', 'POST'])
@login_required
def view_all_comments():
    """ Logic to view comments"""
    db = get_db()

    # If its a POST request, it means the user submitted a search query
    if request.method == 'POST':
        search_query = request.form.get('search_query', '').strip()

        # Query the database to retrieve comments
        comments = db.execute("""SELECT c.id, c.content, c.created_at, u.username
                          FROM comments c JOIN users u ON c.user_id = u.id
                          ORDER BY c.created_at DESC""",
                          ('%' + search_query + '%',)).fetchall()

        # Get IDs for pagination
        previous_comment_ids = [None] + [comment['id'] for comment in comments[:-1]]
        next_comment_ids = [comment['id'] for comment in comments[1:]] + [None]
    
        return render_template('skills/view_all_comments.html', comments=comments,
                               previous_comment_ids=previous_comment_ids,
                               next_comment_ids=next_comment_ids, search_query=search_query)
    
    else:
        # If its a GET request, it means the user wants to view all comments
        comments = db.execute("""SELECT c.id, c.content, c.created_at, u.username
                              FROM comments c JOIN users u ON c.user_id = u.id
                              ORDER BY c.created_at DESC""").fetchall()
                              
    
        # Assuming comments is a list of comment dictionaries
        previous_comment_ids = [None] + [comment['id'] for comment in comments[:-1]]
        next_comment_ids = [comment['id'] for comment in comments[1:]] + [None]
    
        return render_template('skills/view_all_comments.html', comments=comments,
                               previous_comment_ids=previous_comment_ids,
                               next_comment_ids=next_comment_ids)

@bp.route('/comments/cancel', methods=['POST'])
@login_required
def cancel_comment():
    """ Logic to cancel a comment ."""
    flash('Comment canceled!', 'info')
    return redirect(url_for('skills.view_all_comments'))
