from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError




class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please enter your userame'),Length(min=4, max = 20)])
    email = StringField("Email Address", validators= [DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 6), EqualTo('confirm_password', message = 'password must match')])
    confirm_password = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


    # def validate_user(self, data):