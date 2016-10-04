from flask import render_template, request, url_for, redirect, session, flash
from functools import wraps
from flask_login import current_user, login_user, logout_user, login_required
from lucky import app
from lucky.form import RegisterForm, LoginForm
from lucky.database import db, user

#Login-Skript (nicht genutzt)
def login_required2(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def main():
    return(render_template('index.html'))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', LoginForm=LoginForm())


@app.route('/login', methods=['POST'])
def login_validate():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        login_user(login_form.user, remember=True)
        return redirect(url_for('main'))
    else:
        login_form.flash_form_errors()
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out!')
    return redirect(url_for('login'))

@app.route('/showSignUp', methods=['GET'])
def register():
    return render_template('signup.html', RegisterForm=RegisterForm())


@app.route('/showSignUp', methods=['POST'])
def register_validate():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        nutzer = user(
            username=register_form.username.data,
            password=register_form.password.data,
            email=register_form.email.data,
        )
        db.session.add(nutzer)
        db.session.commit()
        login_user(nutzer)
        flash('Succesful registered.<br/>You are now logged in!')
        return redirect(url_for('main'))
    else:
        register_form.flash_form_errors()
        return redirect(url_for('register'))

@app.route('/games')
@login_required
def games():
    return render_template('games.html')
