from flask import Blueprint, render_template

bp = Blueprint('skills', __name__)

@bp.route('/')
def skills():
    render_template('index.html')
