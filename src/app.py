import json

from db import User, Constellation, Constellation_Attempt, Post, db
from flask import Flask, request

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

#initialize app
db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps(data), code


def failure_response(message, code=404):
    return json.dumps({"error": message}), code


#------USER ROUTES-----------------------------------------------------------------------
@app.route("/api/users/", methods = ["POST"])
def create_user():
    """
    Endpoint for creating a user
    """
    body = json.loads(request.data)
    display_name = body.get("display_name")
    if display_name is None:
        return failure_response("Display_name is missing", 400)
    new_user = User(display_name = display_name)
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/api/users/")
def get_users():
    """
    Endpoint for getting all users
    """
    users = [user.serialize() for user in User.query.all()]
    return success_response({"users": users}, 200)

@app.route("/api/users/<int:user_id>/")
def get_user_by_id(user_id):
    """
    Endpoint for getting user by user_id
    """
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("User not found!", 404)
    return success_response(user.serialize(), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
