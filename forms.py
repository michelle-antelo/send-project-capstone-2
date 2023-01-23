from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, validators, ValidationError, RadioField, SelectMultipleField
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

class AddRouteForm(FlaskForm):
    """Form for adding routes."""

    name = StringField('Route Name', validators=[DataRequired()])
    section = StringField('Wall Section', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    image_url = StringField('Route Image URL', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    holds = SelectMultipleField("Holds", choices=['jugs', 'crimps', 'slopers', 'pinches', 'pockets'],validators=[DataRequired()])
    techniques = SelectMultipleField("Techniques", choices=['heel hook', 'toe hook'],validators=[DataRequired()])


class AddCommmentForm(FlaskForm):
    """Form for adding comments to routes"""

    description = TextAreaField('Leave a Comment', validators=[DataRequired()])
    rating = RadioField("Rate this route!", choices=['1','2','3','4','5','6','7','8','9','10'], validators=[DataRequired()])
    grade_rating = TextAreaField("Route Grade Suggestion", validators=[DataRequired()])

class AddPostForm(FlaskForm):
    """Form for adding posts"""

    caption = TextAreaField('Title', validators=[DataRequired()])
    description = TextAreaField("Post", validators=[DataRequired()])
    image_url = StringField("Image URL")
    video_url = StringField("Video URL")

class AddPostCommentForm(FlaskForm):
    """Form for adding comments to user posts"""

    description = TextAreaField('Comment', validators=[DataRequired()])

