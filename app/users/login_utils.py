import functools
from flask import session, redirect, url_for, g
from functools import wraps

def login_required(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('users.login'))
        return view(**kwargs)
    return wrapped