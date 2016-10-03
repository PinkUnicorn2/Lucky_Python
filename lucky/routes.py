from flask import render_template, request, url_for, redirect, session, flash
from functools import wraps
from flask_login import current_user, login_user, logout_user, login_required
from lucky import app
from lucky.form import RegisterForm, LoginForm

#Login Erforderlich
def login_required2(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Sie sind nicht angemeldet.')
            return redirect(url_for('login'))
    return wrap

@login_required
@app.route('/')
def main():
    return(render_template('index.html'))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', LoginForm=LoginForm())


@app.route('/login', methods=['POST'])
def login_validate():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        login_user(login_form.benutzer, remember=True)
        return redirect(url_for('main'))
    else:
        login_form.flash_form_errors()
        return redirect(url_for('login'))

@login_required
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout erfolgreich!')
    return redirect(url_for('main'))

@login_required
@app.route('/games')
def games():
    return render_template('games.html')
