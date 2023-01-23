from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    user_type = db.Column(
        db.Text,
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
        default="data:image/jpeg;base64,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"
    )

    bio = db.Column(
        db.Text,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    routes = db.relationship('Route', backref='user')
    comments = db.relationship('Comment', backref='user')
    posts = db.relationship('Post', backref='user')
    post_comments = db.relationship('PostComment', backref='user')
    likes = db.relationship('Like', backref='user')

    @classmethod
    def signup(cls, username, name, email, password, image_url, bio, user_type):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            name=name,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
            bio=bio,
            user_type=user_type,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`"""

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

class Route(db.Model):
    """Routes in the system."""

    __tablename__ = 'routes'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    section = db.Column(
        db.Text,
        nullable=False,
    )

    color = db.Column(
        db.Text,
        nullable=False,
    )

    grade = db.Column(
        db.Text,
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=False,
    )

    holds = db.Column(
        db.Text,
        nullable=False,
    )

    techniques = db.Column(
        db.Text,
        nullable=False,
    )

    setter_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    comments = db.relationship('Comment', backref='route')

    @classmethod
    def add_route(cls, name, section, color, grade, image_url, description, holds, techniques, setter_id):
        """Add route to the system."""

        route = Route(
            name=name,
            section=section, 
            color=color,
            grade=grade, 
            image_url=image_url, 
            description=description, 
            holds=holds, 
            techniques=techniques,
            setter_id=setter_id,
        )

        db.session.add(route)
        return route

class Comment(db.Model):
    """Comments in the system"""

    __tablename__ = 'comments'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey('routes.id'),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    description = db.Column(
        db.Text,
        nullable=False,
    )

    rating = db.Column(
        db.Text,
        nullable=False,
    )

    grade_rating = db.Column(
        db.Text,
        nullable=False,
    )

    @classmethod
    def add_comment(cls, route_id, user_id, description, rating, grade_rating):
        """Add comment to the system."""

        comment = Comment(
            route_id=route_id,
            user_id=user_id,
            description=description,
            rating=rating,
            grade_rating=grade_rating,
        )

        db.session.add(comment)
        return comment

class Follower(db.Model):
    """Followers following users in the system"""

    __tablename__ = 'followers'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    follower_user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    following_user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    @classmethod
    def follow_user(cls, follower_user_id, following_user_id):
        """Follow user"""

        follower = Follower(
            follower_user_id=follower_user_id,
            following_user_id=following_user_id,
        )

        db.session.add(follower)
        return follower

class Post(db.Model):
    """Posts by users in the system"""

    __tablename__ = 'posts'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    caption = db.Column(
        db.Text,
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
    )

    video_url = db.Column(
        db.Text,
    )

    likes = db.relationship('Like', backref='post')
    comments = db.relationship('PostComment', backref='post')

    @classmethod
    def add_post(cls, user_id, caption, description, image_url, video_url):
        """Add post to the system."""

        post = Post(
            user_id=user_id,
            caption=caption,
            description=description,
            image_url=image_url,
            video_url=video_url,
        )

        db.session.add(post)
        return post

class PostComment(db.Model):
    """Comment on posts in the system"""

    __tablename__ = 'post_comments'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id'),
    )

    description = db.Column(
        db.Text,
        nullable=False,
    )

    @classmethod
    def add_post_comment(cls, post_id, user_id, description):
        """Add comment to a post."""

        comment = PostComment(
            post_id=post_id,
            user_id=user_id,
            description=description,
        )

        db.session.add(comment)
        return comment

class Like(db.Model):
    """Likes on posts in the system"""

    __tablename__ = 'likes'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    like = db.Column(
        db.Boolean,
        default=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id'),
    )

    @classmethod
    def like_post(cls, like, user_id, post_id):
        """Add post to the system."""

        like = Like(
            user_id=user_id,
            like=like,
            post_id=post_id,
        )

        db.session.add(like)
        return like


def connect_db(app):

    db.app = app
    db.init_app(app)