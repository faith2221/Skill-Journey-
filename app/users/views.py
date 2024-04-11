import os
import re
from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from flask import current_app
from app.db import get_db
from app.db_backup import backup_database
from app.utils import form_errors, validate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from app.users.login_utils import login_required

bp = Blueprint('users', __name__, url_prefix='/users')

# Path where profile pictures will be uploaded
UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif'}

def is_admin():
    """ Check if the user is an admin."""
    if g.user and g.user.get('is_admin'):
        return True
    return False

@bp.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}
    if request.method=='POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Password Validation
        if len(password) < 8:
            flash('Password must be at least 8 characters long!', 'error')
            return redirect(url_for('users.register'))
        
        if not (re.search("[a-z]", password) and
                re.search("[A-Z]", password) and
                re.search("[0-9]", password) and
                re.search("[!@#$%^&*()_+\\-=\\[\\]{};':\"\\/,.<>\\/?]", password)):
            flash('Password requires lowercase, uppercase, and special character!', 'error')
            return redirect(url_for('users.register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('users.register'))
        
        # Check if username or email already exists
        db = get_db()
        existing_user = db.execute("""SELECT id FROM users WHERE username = ? OR email = ?""",
                                   (username, email)).fetchone()
        if existing_user:
            flash('Username or email already exists', 'error')
            return redirect(url_for('users.register'))
        
        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user record
        db.execute("""INSERT INTO users (first_name, last_name, username, email, password_hash)
                   VALUES (?, ?, ?, ?, ?)""", (first_name, last_name, username, email,
                   hashed_password) )
        db.commit()

        # Get the newly created user's ID
        user_id = db.execute("""SELECT id FROM users WHERE username = ?""",
                             (username,)).fetchone()['id']

        # Insert profile record with initial data
        db.execute("""INSERT INTO profiles (user_id, bio) VALUES (?, ?)""", (user_id, ''))
        db.commit()

        # Redirect to login page after successful registration
        flash('Registration successful!', 'success')
        return redirect(url_for('users.login'))
    
    # Render registration form for GET requests
    return render_template('users/register.html', errors=errors)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.execute("""SELECT * FROM users WHERE username = ? OR email = ?""",
                          (username, username)).fetchone()
        if user is None or not check_password_hash(user['password_hash'], password):
            flash("Invalid username or password!", category='danger')
            return render_template('users/login.html')
        else:
            flash("Logged in successfully!", category='success')
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('users.home'))
    return render_template('users/login.html')

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def view_profile():
    """ View user profile """
    db = get_db()
    user_id = g.user['id']
    profile = db.execute("""SELECT * FROM profiles WHERE user_id = ?""",
                         (user_id,)).fetchone()
    if not profile:
        flash('Profile not found. Please create your profile!', 'warning')
        return redirect(url_for('users.edit_profile'))
    
    return render_template('users/view_profile.html', profile=profile)

@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """ Edit the profile """
    db = get_db()
    user_id = g.user['id']

    # Fetch the profile information
    profile= db.execute("""SELECT * FROM profiles WHERE user_id = ?""",
                        (user_id,)).fetchone()
    try:
        if request.method == 'POST':
            # Fetch existing user data
            existing_user = db.execute("""SELECT * FROM users WHERE id = ?""",
                                       (user_id,)).fetchone()
        
        # Get form data
        bio = request.form['bio']
        website_url = request.form['website_url']
        location = request.form ['location']

        # Handle profile picture upload
        if 'profile_picture' in request.files:
            profile_picture = request.files['profile_picture']
            if profile_picture.filename != '':
                filename = secure_filename(profile_picture.filename)
                profile_picture.save(os.path.join(current_app.config[UPLOAD_FOLDER], filename))
                profile_picture_url = url_for('static', filename='uploads/' + filename)

                # Update profile picture URL in the database
                db.execute("""UPDATE profiles
                           SET profile_picture_url = ? WHERE user_id = ?""",
                           (profile_picture_url, user_id))
            else:
                profile_picture_url = None
        else:
            profile_picture_url = None

        # Validate and update email if necessary
        email = request.form['email']
        existing_email = db.execute("""SELECT id FROM users WHERE email = ?""", (email,)).fetchone()
        if existing_email and existing_email['id'] != user_id:
            flash('Email already exists', 'error')
            return render_template('users/edit_profile.html', profile=profile)
                                    
        # Update profile data in the database
        db.execute("""UPDATE profiles
                   SET bio = ?, profile_picture_url = ?, website_url = ?,
                   location = ? WHERE user_id = ?""", (bio, profile_picture_url,
                   website_url, location, user_id))
        db.commit()

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('users.view_profile'))

    except Exception as e:
        flash('An error occurred while updating the profile!', 'error')
        current_app.logger.error(f"Error updating profile: {e}")

    return render_template('users/edit_profile.html', profile=profile)
       
@bp.route('/community')
@login_required
def community():
    """ Route to post and comment """
    return render_template('users/community.html')

@bp.route('/logout')
def logout():
    """ Route to log out a user"""
    session.clear()
    flash('Logged out successfully!', category='info')
    return redirect(url_for('users.login'))

@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def  user_settings():
    """ Route to edit user settings """
    if request.method == 'POST':
        # Get form data submitted by the user
        user_id = g.user['id']
        settings = {
            'theme_preference': request.form.get('theme_preference'),
            'push_notifications': request.form.get('push_notifications') == 'on',
            'email_notifications': request.form.get('email_notifications') == 'on',
            'language': request.form.get('language'),
            'text_size': request.form.get('text_size'),
            'text_color': request.form.get('text_color'),
            'background_color': request.form.get('background_color'),
            'color_contrast': request.form.get('color_contrast'),
            'social_media_connected': request.form.get('social_media_connected') == 'on',
            'dark_mode' : request.form.get('dark_mode') == 'on'
        }

        # Update user settings in the database
        db = get_db()
        for setting_name, setting_value in settings.items():
            db.execute("""INSERT INTO user_settings (user_id, setting_name, setting_value)
                       VALUES (?, ?, ?) ON CONFLICT(user_id, setting_name)
                       DO UPDATE SET setting_value = ?""",
                       (user_id, setting_name, setting_value, setting_value))
        db.commit()
        flash('User settings updated successfully!', 'success')

    # Fetch the current user settings from the database
    user_settings = db.execute("""SELECT setting_name, setting_value FROM user_settings
                                   WHERE user_id = ?""", (user_id,)).fetchall()
        
    # Renders the user settings page with the current user settings
    return render_template('users/user_settings.html', user_settings=user_settings)

@bp.route('/notifications')
@login_required
def notifications():
    """ Route to display notifications """
    db = get_db()
    user_id = g.user['id']
    notification_settings = db.execute("""SELECT setting_name, setting_value FROM user_settings
                                       WHERE user_id = ?""", (user_id,)).fetchall()
    
    # Extract user preferences for notification types
    preferences = {setting['setting_name']: setting['setting_value'] for setting in user_settings}

    #Initializes an empty list to store notifications
    notifications = []

    # Fetch notifications based on user preferences
    if preferences.get('email_notifications') == '1':   
            # Fetch email notifications based on user preferences
            email_notifications = db.execute("""SELECT * FROM notifications WHERE user_id = ?
                                             AND notification_type = 'email'""", (user_id,)).fetchall()
            notifications.extend(email_notifications)

    if preferences.get('push_notifications') == '1':
            # Fetch push notifications based on user preferences
            push_notifications = db.execute("""SELECT * FROM notifications WHERE user_id = ?
                                             AND notification_type = 'push'""", (user_id,)).fetchall()
            notifications.extend(push_notifications)

    return render_template('users/notifications.html', notifications=notifications)

@bp.route('/home')
@login_required
def home():
    """ Route to render the home page, restricted to authenticated users"""
    return render_template('users/home.html')
          
@bp.before_app_request
def load_auth_user():
    """ Load the currently authenticated user."""
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        user = db.execute("""SELECT * from users WHERE id = ?""", (user_id,)).fetchone()
        g.user = user