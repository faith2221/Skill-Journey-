from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from app.users.login_utils import login_required
from app.db import get_db
from datetime import datetime
from app.utils import form_errors, validate
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('skills', __name__, url_prefix='/skills')

@bp.route('/resources')
@login_required
def view_resources():
    """ Route to view resources """
    db = get_db()

    # Handle search query
    search_query = request.args.get('search_query', '').strip()
    if search_query:
        # Perform search query
        resources = db.execute("""SELECT r.id, r.title, r.url
                               FROM resources r
                               JOIN resource_links r1 ON r.id = r1.resource_id
                               WHERE r.title LIKE ?""", ('%' + search_query + '%',)).fetchall()
        
    else:
        # Retrieve all resources if no search query
        resources = db.execute("""SELECT r.id, r.title, r.url
                               FROM resources r
                               JOIN resource_links r1 ON r.id = r1.resource_id""").fetchall()
    
    return render_template('skills/view_resources.html', resources=resources)

@bp.route('/posts', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        # Extract form data
        title = request.form['title']
        content = request.form['content']
        url = request.form['url']
        
        # Add user_id to the post record for association with the user
        user_id = g.user['id']

        # Validate input
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('skills.create_post'))
        
        # Insert post record
        db = get_db()
        db.execute("""INSERT INTO posts (title, content, url, user_id, created_at)
                   VALUES (?,?, ?, ?, ?)""",
                   (title, content, url, user_id, datetime.utcnow()))
        
        # Commit the transaction
        db.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('skills.view_all_posts'))
    
    return render_template('skills/create_post.html')

@bp.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    """ Logic to edit a post"""
    db = get_db()
    post = db.execute("""SELECT * FROM posts WHERE id = ?""",
                      (post_id,)).fetchone()
    
    # Check if the user is authorized to edit the post
    if post['user_id'] != g.user['id']:
        flash('You are not authorized to edit this post!', 'error')
        return redirect(url_for('skills.view_all_posts'))
    
    # Handle POST request
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Validate Input
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('skills.edit_post', post_id=post_id))
        
        # Update the post record
        db.execute("""UPDATE posts SET title = ?, content = ? WHERE id = ?""",
                   (title, content, post_id))
        db.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('skills.view_all_posts'))

    return render_template('skills/edit_post.html', post=post)

@bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """ Logic to delete a post"""
    db = get_db()
    post = db.execute("""SELECT * FROM posts WHERE id = ?""",
                      (post_id,)).fetchone()
    
    # Check if the user is authorized to delete the post
    if post['user_id'] != g.user['id']:
        flash('You are not authorized to delete this post!', 'error')
        return redirect(url_for('skills.view_all_posts'))
    
    # Delete the post record
    db.execute("""DELETE FROM posts WHERE id = ?""", (post_id,))
    db.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('skills.view_all_posts'))

@bp.route('/posts')
@login_required
def view_all_posts():
    """ Logic for viewing posts """
    db = get_db()

    # Handle search query
    search_query = request.args.get('search_query', '').strip()
    if search_query:
        # Perform search query
        posts = db.execute("""SELECT p.id, p.title, p.content, p.url, p.created_at,
                           u.username FROM posts p JOIN users u ON p.user_id = u.id
                           WHERE p.title LIKE ? OR p.content LIKE ?
                           ORDER BY p.created_at DESC""",
                           ('%' + search_query + '%', '%' + search_query + '%')).fetchall()
        
    else:
        # Retrieve all posts if no search query
        posts = db.execute("""SELECT p.id, p.title, p.content, p.url, p.created_at,
                           u.username FROM posts p JOIN users u ON p.user_id = u.id
                           ORDER BY p.created_at DESC""").fetchall()
    
    # Assuming posts is a list of post dictionaries
    previous_post_ids = [None] + [post['id'] for post in posts[:-1]]
    next_post_ids = [post['id'] for post in posts[1:]] + [None]

    # Render the view
    return render_template('skills/view_all_posts.html', posts=posts,
                           previous_post_ids=previous_post_ids,
                           next_post_ids=next_post_ids)

@bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@login_required
def add_comment(post_id):
    """ Logic to add a comment to a post"""
    db = get_db()
    content = request.form['content']
    user_id = g.user['id']

    # Validate Input
    db.execute("""INSERT INTO comments (content, post_id, user_id, created_at)
               VALUES (?, ?, ?, ?)""", (content, user_id, post_id, datetime.utcnow()))
    db.commit()
    flash('Comment added successfully!', 'success')
    return redirect(url_for('skills.view_all_posts'))

@bp.route('/posts/<int:post_id>/comments/<int:comment_id>/edit',
           methods=['GET', 'POST'])
@login_required
def edit_comment(post_id, comment_id):
    """ Logic to edit a comment"""
    db = get_db()
    comment = db.execute("""SELECT * FROM comments WHERE id = ?""",
                         (comment_id,)).fetchone()
    
    # Check if the user is authorized to edit the comment
    if comment['user_id'] != g.user['id']:
        flash('You are not authorized to edit this comment!', 'error')
        return redirect(url_for('skills.view_all_posts'))
    
    # Handle POST request
    if request.method == 'POST':
        content = request.form['content']

        #Validate Input
        if not content:
            flash('Content is required!', 'error')
            return redirect(url_for('skills.edit_comment', 
                                    post_id=post_id, comment_id=comment_id))
        
        # Update the comment record
        db.execute("""UPDATE comments SET content = ? WHERE id = ?""",
                   (content, comment_id))
        db.commit()
        flash('Comment updated successfully!', 'success')
        return redirect(url_for('skills.view_all_posts'))
    
    return render_template('skills/edit_comment.html', comment=comment)

@bp.route('/posts/<int:post_id>/comments', methods=['GET', 'POST'])
@login_required
def view_all_comments(post_id):
    """ Logic to view comments"""
    db = get_db()

    # If its a POST request, it means the user submitted a search query
    if request.method == 'POST':
        search_query = request.form.get('search_query', '').strip()

        # Query the database to retrieve comments
        comments = db.execute("""SELECT c.id, c.content, c.created_at, u.username
                          FROM comments c JOIN users u ON c.user_id = u.id
                          WHERE c.post_id = ? AND (c.content LIKE ?)
                          ORDER BY c.created_at DESC""",
                          (post_id, '%' + search_query + '%')).fetchall()
    
        # Assuming comments is a list of comment dictionaries
        previous_comment_ids = [None] + [comment['id'] for comment in comments[:-1]]
        next_comment_ids = [comment['id'] for comment in comments[1:]] + [None]
    
        return render_template('skills/view_all_comments.html', comments=comments,
                               previous_comment_ids=previous_comment_ids,
                               next_comment_ids=next_comment_ids, search_query=search_query)
    
    else:
        # If its a GET request, it means the user wants to view all comments
        comments = db.execute("""SELECT c.id, c.content, c.created_at, u.username
                          FROM comments c JOIN users u ON c.user_id = u.id
                          WHERE c.post_id = ?
                          ORDER BY c.created_at DESC""", (post_id,)).fetchall()
    
        # Assuming comments is a list of comment dictionaries
        previous_comment_ids = [None] + [comment['id'] for comment in comments[:-1]]
        next_comment_ids = [comment['id'] for comment in comments[1:]] + [None]
    
        return render_template('skills/view_all_comments.html', comments=comments,
                               previous_comment_ids=previous_comment_ids,
                               next_comment_ids=next_comment_ids)

@bp.route('/search', methods=['POST'])
@login_required
def search():
    """ Route to handle comprehensive search queries """
    db = get_db()

    # Handle search query
    search_query = request.form.get('search_query', '').strip()
    if search_query:
        # Perform search query across posts, comments, and resources
        results = db.execute("""SELECT 'post' AS type, id, title, content, url, created_at,
                           NULL AS username FROM posts
                           WHERE title LIKE ? OR content LIKE ?
                           UNION
                           SELECT 'comment' AS type, c.id, c.content, NULL AS title, NULL AS url,
                           c.created_at, u.username FROM comments c
                           JOIN users u ON c.user_id = u.id                          
                           WHERE c.content LIKE ?
                           UNION
                           SELECT 'resource' AS type, r.id, r.title, NULL AS content, r1.url,
                           NULL AS created_at, NULL AS username FROM resources r
                           JOIN resource_links r1 ON r.id =r1.resource_id
                           WHERE r.title LIKE ?""",
                           ('%' + search_query + '%', '%' + search_query + '%',
                            '%' + search_query + '%', '%' + search_query + '%')).fetchall()
    else:
        # Redirect to home route if no search query
        return redirect(url_for('users.home'))
    
    return render_template('skills/search.html', results=results, search_query=search_query)

@bp.route('/posts/<int:post_id>/comments/<int:comment_id>/delete',
           methods=['POST'])
@login_required
def delete_comment(post_id, comment_id):
    """ Logic to delete a comment"""
    db = get_db()
    comment = db.execute("""SELECT * FROM comments WHERE id = ?""",
                         (comment_id,)).fetchone()
    
    # Check if the user is authorized to delete the comment
    if comment['user_id'] != g.user['id']:
        flash('You are not authorized to delete this comment!', 'error')
        return redirect(url_for('skills.view_all_posts'))
    
    # Delete the comment record
    db.execute("""DELETE FROM comments WHERE id = ?""", (comment_id,))
    db.commit()
    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('skills.view_all_posts'))