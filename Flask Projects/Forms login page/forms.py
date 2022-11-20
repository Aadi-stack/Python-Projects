
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    Username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    Password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',
                                     validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
