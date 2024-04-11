from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def landing_page():
    """ Logic before  register and login """
    return render_template('landing.html')

@bp.route('/terms_of_service')
def terms_of_service():
    """ Route to display terms of service"""
    return render_template('terms_of_service.html')

@bp.route('/privacy_policy')
def privacy_policy():
    """ Route to display privacy policy """
    return render_template('privacy_policy.html')

@bp.route('/copyright')
def copyright():
    """ Route to display copyright information """
    return render_template('copyright.html')




    