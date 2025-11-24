from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#Database Model Classes
class User():
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


class Constellation_Attempts(self):
    """
    Constellation_Attempts model
    """
    __tablename__ = "constellation_attempts"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    constellation_id = db.Column(db.Integer, db.ForeignKey("constellations.id"), nullable = False)
    stars_completed = db.Column(db.Integer, nullable = False)
    
