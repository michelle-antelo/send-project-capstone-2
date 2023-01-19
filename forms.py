from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, validators, ValidationError, RadioField
from wtforms.validators import DataRequired, Email, Length

class UserAddForm(FlaskForm):
    """Form for adding users."""

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Profile Image URL')
    bio = TextAreaField('Share a little about yourself', validators=[Length(max=60)])
    user_type = RadioField('Are you a climber or a setter?', choices=['climber', 'setter'])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class UpdateUserForm(FlaskForm):
    """Form for updating users."""

    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    image_url = StringField('(Optional) Profile Image URL')
    bio = TextAreaField('Share a little about yourself')