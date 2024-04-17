from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def landing_page():
    """ Logic before  register and login """
    return render_template('landing.html')

@bp.route('/about_section')
def about_section():
    """ Route to display the about section"""
    return render_template('about_section.html')





    