from lucky.database import user
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, length, EqualTo, Email


# Errorhandling
class DefaultForm(FlaskForm):
    def flash_form_errors(self):
        for field, errors in self.errors.items():
            for error in errors:
                flash("Error in field: %s - %s" % (getattr(self, field).label.text, error))


class RegisterForm(DefaultForm):
    username = StringField('Username', validators=[InputRequired(), length(1, 80)])
    email = StringField('Email', validators=[InputRequired(), length(1, 120), Email()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('password_confirm')])
    password_confirm = PasswordField('Repeat Password', validators=[InputRequired()])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        if user.query.filter_by(username=self.username.data).first() is not None:
            self.username.errors.append("Benutzername gibts es bereits.")
            return False

        if user.query.filter_by(email=self.email.data).first() is not None:
            self.email.errors.append("E-Mail-Adresse wird bereits verwendet")
            return False
        else:
            return True


class LoginForm(DefaultForm):
    username = StringField('Username', validators=[InputRequired(), length(1, 80)])
    password = PasswordField('Password', validators=[InputRequired()])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        nutzer = user.query.filter_by(username=self.username.data).first()
        if nutzer is None:
            self.username.errors.append("Not a valid username")
            return False

        if not nutzer.verify_password(self.password.data):
            self.password.errors.append("Not a valid password")
            return False

        self.user = nutzer
        return True