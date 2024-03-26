from flask import request, render_template, Blueprint, session, url_for, redirect, flash
from app.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('users', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if username and email and password:
            hashed_password = generate_password_hash(password)
            query = """--sql
            INSERT INTO users (username, email, password) VALUES ('%s', '%s', '%s')""" %(username,
            email, password)
            db.execute(query)
            db.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('users.login'))
    return render_template('users/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('users/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('users.login'))