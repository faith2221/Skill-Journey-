from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from app.users.login_utils import login_required
from app.db import get_db
from datetime import datetime
from app.utils import form_errors, validate
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('skills', __name__, url_prefix='/skills')

@bp.route('/skills/add', methods=['GET', 'POST'])
@login_required
def add_skill():
    """ Logic that allows user to add skill to track progress"""
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        if skill_name:
            db = get_db()
            db.execute(" INSERT INTO skills (skill_name) VALUES (?)", (skill_name))
            db.commit()
            flash('Skill added successfully!', 'success')
            return redirect(url_for('users.view_resources'))
        else:
            flash('Skill name is required', 'error')
    return render_template('skills/add_skill.html')

@bp.route('/resources')
@login_required
def view_resources():
    db = get_db()
    resources = db.execute("SELECT * FROM resources").fetchall()
    return render_template('skills/view_resources.html', resources=resources)

@bp.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_skill(id):
    """ Logic to edit an existing skill"""
    db = get_db()
    skill = db.execute("""
    SELECT * FROM skills WHERE id = ?""", (id,)).fetchone()
    if not skill:
        flash('Skill not found', 'error')
        return redirect(url_for('users.home'))
    
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        if skill_name :
            db.execute ("""
            UPDATE skills SET skill_name = ? WHERE id = ?""", (skill_name, id))
            db.commit()
            flash('Skill updated successfully!', 'success')
            return redirect(url_for('skills.view_resources'))
        else:
            flash ('Skill name is required', 'error')
    return render_template('skills/edit_skill.html', skill=skill)

@bp.route('/skills/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_skill(id):
    """ Logic to delete an added skill """
    db = get_db()
    db.execute("""
    DELETE FROM skills WHERE id = ?""", (id,))
    db.commit()
    flash('Skill deleted successfully!', 'success')
    return redirect(url_for('users.home'))