from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#Database Model Classes
class User(db):
    """
    User model
    One-to-many relationship with Constellations_attempts
    One-to-many relationship with Study_sessions
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    display_name = db.Column(db.String, nullable = False)


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
            "display_name" : self.display_name
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

    def init(self, **kwargs):
        """
        Initialize Constellation object
        """
        self.name = kwargs.get('name')
        self.weight = kwargs.get('weight')



class Constellation_Attempts(db.Model):
    """
    Constellation_Attempts model
    """
    __tablename__ = "constellation_attempts"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    constellation_id = db.Column(db.Integer, db.ForeignKey("constellations.id"), nullable = False)
    stars_completed = db.Column(db.Integer, nullable = False)
    

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

    def __init__(self, **kwargs):
        """
        Initialize Session object
        """
        self.user_id = kwargs.get('user_id')
        self.constellation_attempt_id = kwargs.get('constellation_attempt_id')
        self.is_completed = kwargs.get('is_completed', False)
        self.hours = kwargs.get('hours')

class Posts(db.Model):
    """
    Posts model
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