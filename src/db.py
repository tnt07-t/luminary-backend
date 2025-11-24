from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Database Model Classes
class User(db):
    """
    User model
    One-to-many relationship with Constellation_Attempts
    One-to-many relationship with Study_sessions
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    display_name = db.Column(db.String, nullable = False)
    #est. relationships
    constellation_attempts = db.relationship("Constellation_Attempts", back_populates = "user", cascade = "delete")
    sessions = db.relationship("Session", back_populates = "user",cascade = "delete")
    posts = db.relationship("Post", back_populates="user", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize Course object
        """
        self.display_name = kwargs.get("display_name")

    def serialize(self):
        """
        Serialize a User Object
        """
        return {
            "id" : self.id,
            "display_name" : self.display_name,
            "posts": [post.simple_serialize() for post in self.posts]
        }
    
    def simple_serialize(self):
        return {
            "id" : self.id,
            "display_name" : self.display_name
        }

class Constellation(db.Model):
    """
    Constellation model
    One-to-many relationship with Constellation_Attempts
    """
    __tablename__ = 'constellations'

    constellation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    #establish relationship
    user_attempts = db.relationship("Constellation_Attempts", back_populates="constellation")


    def init(self, **kwargs):
        """
        Initialize Constellation object
        """
        self.name = kwargs.get('name')
        self.weight = kwargs.get('weight')

    def serialize(self):
        """
        Serialize a Constellation Object
        """
        return {
            "constellation_id": self.constellation_id,
            "name": self.name,
            "weight": self.weight
        }



class Constellation_Attempt(db.Model):
    """
    Constellation_Attempt model
    """
    __tablename__ = "constellation_attempts"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    constellation_id = db.Column(db.Integer, db.ForeignKey("constellations.id"), nullable = False)
    stars_completed = db.Column(db.Integer, nullable = False)
    #est. relationships
    user = db.relationship("User", back_populates = "constellation_attempts")
    
    def __init__(self, **kwargs):
        """
        Initialize Constellation_Attempt object
        """
        user_id = kwargs.get("user_id")
        constellation_id = kwargs.get("constellation_id")
        stars_completed = 0

class Session(db.Model):
    """
    Session model
    """
    __tablename__ = 'sessions'

    session_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    constellation_attempt_id = db.Column(db.Integer, db.ForeignKey('constellation_attempts.attempt_id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    hours = db.Column(db.Integer, nullable=False)
    #est. relationship
    user = db.relationship("User", back_populates = "sessions")

    def __init__(self, **kwargs):
        """
        Initialize Session object
        """
        self.user_id = kwargs.get('user_id')
        self.constellation_attempt_id = kwargs.get('constellation_attempt_id')
        self.is_completed = kwargs.get('is_completed', False)
        self.hours = kwargs.get('hours')

class Post(db.Model):
    """
    Post model
    """
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    constellation_id = db.Column(db.Integer, db.ForeignKey('constellations.constellation_id'), nullable=False)
    post_type = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        """
        Initialize Posts object
        """
        self.user_id = kwargs.get('user_id')
        self.constellation_id = kwargs.get('constellation_id')
        self.post_type = kwargs.get('post_type')

    def serialize(self):
        """
        Serialize a Post Object
        """
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "constellation_id": self.constellation_id,
            "post_type": self.post_type
        }
    
    def simple_serialize(self):
        return {
            "post_id": self.post_id,
            "post_type": self.post_type
        }