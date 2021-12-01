from os import stat
from . import bp as app
from app import db
from flask import request, render_template, url_for, redirect, flash
from datetime import datetime
from app.blueprints.auth.models import User
from app.blueprints.api.models import Collection
from flask_login import login_user, logout_user, current_user


@app.route('/collections')
def collect():
    c = Collection.query.filter_by(user_id=current_user.get_id()).all():
    context = {
        'posts': Collection.query.order_by(Collection.date_created.desc()).all()
    }
    return render_template('collections.html', **context)

@app.route('/add_collection', methods=['POST'])
def add_collection():
    status = request.form.get('user_status')

    if status:
        c = Collection(name=status, user_id=current_user.get_id())
        db.session.add(c)
        db.session.commit()
        flash('You have successfully added a new superhero.', 'success')
    else:
        flash('You cannot post nothing', 'warning')
    return redirect(url_for('api.collect'))
