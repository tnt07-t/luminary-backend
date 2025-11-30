from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Database Model Classes
class User(db.Model):
    """
    User model
    One-to-many relationship with Constellation_Attempt
    One-to-many relationship with Study_sessions
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    display_name = db.Column(db.String, nullable = False)
    current_attempt_id = db.Column(db.Integer, db.ForeignKey("constellation_attempts.id"), nullable=True)
    #est. relationships
    constellation_attempts = db.relationship("Constellation_Attempt", foreign_keys="Constellation_Attempt.user_id", back_populates = "user", cascade = "delete")
    current_attempt = db.relationship("Constellation_Attempt", foreign_keys=[current_attempt_id], uselist=False)
    sessions = db.relationship("Session", back_populates = "user",cascade = "delete")
    posts = db.relationship("Post", back_populates="user", cascade="delete")
    
    def __init__(self, **kwargs):
        """
        Initialize Course object
        """
        self.display_name = kwargs.get("display_name")

    def serialize(self):
        """
        Serialize a User Object with all relationships
        """
        return {
            "id": self.id,
            "display_name": self.display_name,
            "current_attempt_id": self.current_attempt_id,
            "current_attempt": self.current_attempt.simple_serialize() if self.current_attempt else None,
            "constellation_attempts": [attempt.simple_serialize() for attempt in self.constellation_attempts],
            "sessions": [session.simple_serialize() for session in self.sessions],
            "posts": [post.simple_serialize() for post in self.posts]
        }
    
    def simple_serialize(self):
        """
        Simple User serialization to prevent loops
        """
        return {
            "id": self.id,
            "display_name": self.display_name
        }

class Constellation(db.Model):
    """
    Constellation model
    One-to-many relationship with Constellation_Attempt
    """
    __tablename__ = 'constellations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    #establish relationship
    user_attempts = db.relationship("Constellation_Attempt", back_populates="constellation")
    posts = db.relationship("Post", back_populates="constellation")

    def __init__(self, **kwargs):
        """
        Initialize Constellation object
        """
        self.name = kwargs.get('name')
        self.weight = kwargs.get('weight')

    def serialize(self):
        """
        Serialize a Constellation Object with all relationships
        """
        return {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "user_attempts": [attempt.simple_serialize() for attempt in self.user_attempts],
            "posts": [post.simple_serialize() for post in self.posts]
        }

    def simple_serialize(self):
        """
        Simple Constellation serialization to prevent loops
        """
        return {
            "id": self.id,
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
    user = db.relationship("User", foreign_keys=[user_id], back_populates = "constellation_attempts")
    constellation = db.relationship("Constellation", back_populates="user_attempts")
    sessions = db.relationship("Session", back_populates="constellation_attempt", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize Constellation_Attempt object
        """
        self.user_id = kwargs.get("user_id")
        self.constellation_id = kwargs.get("constellation_id")
        self.stars_completed = 0

    def serialize(self):
        """
        Serialize a Constellation_Attempt Object with all relationships
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "constellation_id": self.constellation_id,
            "stars_completed": self.stars_completed,
            "user": self.user.simple_serialize() if self.user else None,
            "constellation": self.constellation.simple_serialize() if self.constellation else None,
            "sessions": [session.simple_serialize() for session in self.sessions]
        }

    def simple_serialize(self):
        """
        Simple Constellation_Attempt serialization to prevent loops
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "constellation_id": self.constellation_id,
            "stars_completed": self.stars_completed
        }
    

class Session(db.Model):
    """
    Session model
    """
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    constellation_attempt_id = db.Column(db.Integer, db.ForeignKey('constellation_attempts.id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    hours = db.Column(db.Integer, nullable=False)
    #est. relationship
    user = db.relationship("User", back_populates = "sessions")
    constellation_attempt = db.relationship("Constellation_Attempt", back_populates="sessions")

    def __init__(self, **kwargs):
        """
        Initialize Session object
        """
        self.user_id = kwargs.get('user_id')
        self.constellation_attempt_id = kwargs.get('constellation_attempt_id')
        self.is_completed = kwargs.get('is_completed', False)
        self.hours = kwargs.get('hours')
        
    def serialize(self):
        """
        Serialize a Session Object with all relationships
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "constellation_attempt_id": self.constellation_attempt_id,
            "is_completed": self.is_completed,
            "hours": self.hours,
            "user": self.user.simple_serialize() if self.user else None,
            "constellation_attempt": self.constellation_attempt.simple_serialize() if self.constellation_attempt else None
        }

    def simple_serialize(self):
        """
        Simple Session serialization to prevent loops
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "constellation_attempt_id": self.constellation_attempt_id,
            "is_completed": self.is_completed,
            "hours": self.hours
        }

class Post(db.Model):
    """
    Post model
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    constellation_id = db.Column(db.Integer, db.ForeignKey('constellations.id'), nullable=False)
    post_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #establish relationships
    user = db.relationship("User", back_populates="posts")
    constellation = db.relationship("Constellation", back_populates="posts")

    def __init__(self, **kwargs):
        """
        Initialize Posts object
        """
        self.user_id = kwargs.get('user_id')
        self.constellation_id = kwargs.get('constellation_id')
        self.post_type = kwargs.get('post_type')

    def serialize(self):
        """
        Serialize a Post Object with all relationships
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "constellation_id": self.constellation_id,
            "post_type": self.post_type,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "user": self.user.simple_serialize() if self.user else None,
            "constellation": self.constellation.simple_serialize() if self.constellation else None
        }
    
    def simple_serialize(self):
        """
        Simple Post serialization to prevent loops
        """
        return {
            "id": self.id,
            "post_type": self.post_type,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }