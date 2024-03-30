from flask import request, render_template, Blueprint, session, url_for, redirect, flash, g
from flask import jsonify
from app.users.login_utils import login_required
from app.db import get_db
from datetime import datetime
from app.utils import form_errors, validate
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('skills', __name__, url_prefix='/skills')

@bp.route('/')
@login_required
def view_skills():
    """ Logic to view skills """
    db = get_db()
    skills = db.execute("SELECT * from skills").fetchall()

    categorized_skills = {
        "Programming": [],
        "Creative": [],
        "Lifestyle": [],
        "Career": [],
    }

    for skill in skills:
        skill_name = skill['skill_name']
        if  "Programming" in skill_name:
            categorized_skills["Programming"].append(skill_name)
        elif "Creative" in skill_name:
            categorized_skills["Creative"].append(skill_name)
        elif "Lifestyle" in skill_name:
            categorized_skills["Lifestyle"].append(skill_name)
        elif "Career" in skill_name:
            categorized_skills["Career"].append(skill_name)
        
    return render_template('skills/skills.html', categorized_skills=categorized_skills)

@bp.route('/skills/add', methods=['GET', 'POST'])
@login_required
def add_skill():
    """ Logic that allows user to add skill to track progress"""
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        if name:
            db = get_db()
            db.execute(" INSERT INTO skills (skill_name) VALUES (?, ?)", (skill_name))
            db.commit()
            flash('Skill added successfully!', 'success')
            return redirect(url_for('users.home'))
        else:
            flash('Skill name is required', 'error')
    return render_template('skills/add_skill.html')

@bp.route('/skills/select', methods=['POST'])
@login_required
def select_skill():
    """ Logic for the current user to select a skill."""
    if request.method == 'POST':
        # Assuming the skill ID is sent along with the form submission
        skill_id = request.form.get('skill_id')
        if skill_id:
            db = get_db()
            # Insert the skill ID into the user_selected_skills table
            db.execute("INSERT INTO user_selected_skills (user_id, skill_id) VALUES (?, ?)",
                       (session.get('user_id'), skill_id))
            db.commit()
            # Redirect user to the home page
            return redirect(url_for('users.home'))
        else:
            # If skill ID is not provided, return an error message
            return jsonify({'error': 'Skill ID not provided'})
       
@bp.route('/skills/unselect', methods=['POST'])
@login_required
def unselect_skill():
    """ Logic to remove skill from the current user's profile."""
    if request.method == 'POST':
        # Assuming the skill ID is sent along with the form submission
        skill_id = request.form.get('skill_id')
        if skill_id:
            db = get_db()
            # Delete the skill ID from the user_selected_skills table
            db.execute("DELETE FROM user_selected_skills WHERE user_id = ? and skill_id = ?",
                       (session.get('user_id'), skill_id))
            db.commit()
            # Redirect the user to the home page after successful  removal
            return redirect(url_for('users.home'))
        else:
            # If skill ID is not provided, return an error message
            return jsonify({'error': 'Skill ID is required'}), 400
       
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