from flask import redirect, render_template, request, url_for, session, abort
from app.db import connection
from app.models.user import User
from app.helpers.auth import authenticated
from app import db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)
<<<<<<< HEAD
    #if session['username'] == 'admin'    
=======
>>>>>>> 32a019d81740f94f415a068e19062eb45fc551c5
    users = db.session.query(User).all()
    return render_template("user/index.html", users=users)
    return render_template("home.html")


def new():
    if not authenticated(session):
        abort(401)
    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)
    db.session.add(User(request.form))
    db.session.commit()
    return redirect(url_for("user_index"))



def update(user_id):
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).filter_by(id= user_id).first()
    return render_template("user/update.html",user = user)



def update_new():
    if not authenticated(session):
        abort(401)
    data = request.form
    user = db.session.query(User).get(data['user_id'])
    if user.first_name != data['first_name']:
        user.first_name = data['first_name']
    if user.username != data['username']:
        user.username = data['username']
    if user.last_name != data['last_name']:
        user.last_name = data['last_name']
    if user.email != data['email']:
        user.email = data['email']
    db.session.commit()
    return redirect(url_for('user_index'))



def delete():
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).get(request.form['user_id'])
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_index'))
