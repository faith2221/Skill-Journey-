from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from app.users.views import login_required
from app.db import get_db
from datetime import datetime
from app.utils import form_errors, validate
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('skills', __name__, url_prefix='/skills')

@bp.route('/skills')
@login_required
def view_skills():
    """ Logic to view skills """
    db = get_db()
    skills = db.execute("SELECT * from skills").fetchall()
    return render_template('skills/skills.html', skills=skills)

@bp.route('/skills/add', methods=['GET', 'POST'])
@login_required
def add_skill():
    """ Logic that allows user to add skill to track progress"""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        if name and description:
            db = get_db()
            db.execute(" INSERT INTO skills (name, description) VALUES (?, ?)", (name, description))
            db.commit()
            flash('Skill added successfully!', 'success')
            return redirect(url_for('skills.view_skills'))
        else:
            flash('Both name and description are required', 'error')
    return render_template('skills/add_skill.html')

@bp.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_skill(id):
    db = get_db()
    skill = db.execute("""
    SELECT * FROM skills WHERE id = ?""", (id,)).fetchone()
    if skill is None:
        flash('Skill not found', 'error')
        return redirect(url_for('skills.view_skills'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        if name and description:
            db.execute ("""
            UPDATE skills SET name = ?, description = ? WHERE id = ?""", (name, description, id))
            db.commit()
            flash('Skill updated successfully!', 'success')
            return redirect(url_for('skills.view_skills'))
        else:
            flash ('Both name and description are required', 'error')
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
    return redirect(url_for('skills.view_skills'))