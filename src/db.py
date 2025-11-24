from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#Database Model Classes
class User():
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    display_name = db.Column(db.String, nullable = False)

    def serialize(self):
        """
        Serialize a User Object
        """