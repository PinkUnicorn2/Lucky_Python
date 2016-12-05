from flask import render_template, request, url_for, redirect, session, flash
from flask_login import current_user, login_user, logout_user, login_required
from lucky import app
from lucky.form import RegisterForm, LoginForm
from lucky.database import db, user, chat


@app.route('/')
def main():
    return(render_template('index.html',messages=chat.query.all(), user=user.query.all()))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', LoginForm=LoginForm(),messages=chat.query.all())


@app.route('/login', methods=['POST'])
def login_validate():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        login_user(login_form.user, remember=True)
        # Setzte direkt nach dem Einloggen in der Datenbank, logged_in auf 1,
        # um spaeter alle eingeloggten User anzeigen zu koennen
        # eigentliche Abfrage in base.html
        nutzer = user.query.filter_by(username=current_user.username).first()
        nutzer.logged_in = 1
        db.session.commit()
        return redirect(url_for('main'))
    else:
        login_form.flash_form_errors()
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    #Setzte logged_in auf 0, wenn Benutzer dabei ist, sich auszuloggen
    nutzer = user.query.filter_by(username=current_user.username).first()
    nutzer.logged_in = 0
    db.session.commit()
    logout_user()
    flash('Logout erfolgreich!')
    return redirect(url_for('login'))


@app.route('/showSignUp', methods=['GET'])
def register():
    return render_template('signup.html', RegisterForm=RegisterForm(),messages=chat.query.all())


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
        flash('Registrierung erfolgreich!')
        return redirect(url_for('main'))
    else:
        register_form.flash_form_errors()
        return redirect(url_for('register'))




@app.route('/cash_weg')
@login_required
def cash_weg():
    nutzer = user.query.filter_by(username=current_user.username).first()
    if nutzer.money<250:
        return 'verpiss dich'

    nutzer.money-=250;
    db.session.commit()
    return 'abgebucht'


@app.route('/cash_dazu')
def cash_dazu():
    nutzer = user.query.filter_by(username=current_user.username).first()
    if nutzer.money<250:
        return 'verpiss dich'

    nutzer.money+=5000;
    db.session.commit()
    return 'abgebucht'


@app.route('/games')
@login_required
def games():
    return render_template('games.html',messages=chat.query.all(),user=user.query.all())
