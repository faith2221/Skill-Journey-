from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def landing_page():
    """ Logic before  register and login """
    return render_template('landing.html')