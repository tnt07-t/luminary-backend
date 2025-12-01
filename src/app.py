import json
from pickle import GET

from db import User, Constellation, Constellation_Attempt, Post, Session, db
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

@app.route("/api/users/<int:user_id>/total_hours/")
def get_user_total_hours(user_id):
    """
    Endpoint for getting total hours a user has worked (only completed sessions)
    """
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("User not found!", 404)

    total_hours = 0
    for session in user.sessions:
        if session.is_completed and session.hours:
            total_hours += session.hours

    return success_response({
        "user_id": user_id,
        "display_name": user.display_name,
        "total_hours": total_hours
    }, 200)


#------CONSTELLATION ROUTES-------------------------------------------------------------
@app.route("/api/constellations/", methods=["POST"])
def create_constellation():
    """
    Endpoint for creating a constellation
    """
    body = json.loads(request.data)
    name = body.get("name")
    weight = body.get("weight")

    if name is None or weight is None:
        return failure_response("Missing name or weight!", 400)

    new_constellation = Constellation(name=name, weight=weight)
    db.session.add(new_constellation)
    db.session.commit()
    return success_response(new_constellation.serialize(), 201)

@app.route("/api/constellations/")
def get_constellations():
    """
    Endpoint for getting all constellations
    """
    constellations = [c.serialize() for c in Constellation.query.all()]
    return success_response({"constellations": constellations}, 200)

@app.route("/api/constellations/<int:constellation_id>/")
def get_constellation_by_id(constellation_id):
    """
    Endpoint for getting constellation by id
    """
    constellation = Constellation.query.filter_by(id=constellation_id).first()
    if constellation is None:
        return failure_response("Constellation not found!", 404)
    return success_response(constellation.serialize(), 200)

@app.route("/api/constellations/<int:constellation_id>/", methods=["PUT"])
def update_constellation(constellation_id):
    """
    Endpoint for updating a constellation
    """
    constellation = Constellation.query.filter_by(id=constellation_id).first()
    if constellation is None:
        return failure_response("Constellation not found!", 404)

    body = json.loads(request.data)
    constellation.name = body.get("name", constellation.name)
    constellation.weight = body.get("weight", constellation.weight)
    db.session.commit()
    return success_response(constellation.serialize(), 200)

@app.route("/api/constellations/<int:constellation_id>/", methods=["DELETE"])
def delete_constellation(constellation_id):
    """
    Endpoint for deleting a constellation
    """
    constellation = Constellation.query.filter_by(id=constellation_id).first()
    if constellation is None:
        return failure_response("Constellation not found!", 404)
    db.session.delete(constellation)
    db.session.commit()
    return success_response({"message": "Constellation deleted successfully!"}, 200)


#------CONSTELLATION ATTEMPT ROUTES-----------------------------------------------------
@app.route("/api/users/<int:user_id>/constellation_attempts/", methods=["POST"])
def create_constellation_attempt(user_id):
    """
    Endpoint for creating a constellation attempt for a user
    """
    body = json.loads(request.data)
    constellation_id = body.get("constellation_id")

    if constellation_id is None:
        return failure_response("Missing required field: constellation_id", 400)

    # Validate user exists
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!", 404)

    # Validate constellation exists
    constellation = Constellation.query.filter_by(id=constellation_id).first()
    if constellation is None:
        return failure_response("Constellation not found!", 404)

    new_attempt = Constellation_Attempt(user_id=user_id, constellation_id=constellation_id)
    db.session.add(new_attempt)
    db.session.commit()
    return success_response(new_attempt.serialize(), 201)

@app.route("/api/constellation_attempts/")
def get_all_constellation_attempts():
    """
    Endpoint for getting all constellation attempts
    """
    attempts = [attempt.serialize() for attempt in Constellation_Attempt.query.all()]
    return success_response({"constellation_attempts": attempts}, 200)

@app.route("/api/constellation_attempts/<int:attempt_id>/")
def get_constellation_attempt_by_id(attempt_id):
    """
    Endpoint for getting a constellation attempt by id
    """
    attempt = Constellation_Attempt.query.filter_by(id=attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)
    return success_response(attempt.serialize(), 200)

@app.route("/api/users/<int:user_id>/constellation_attempts/")
def get_user_constellation_attempts(user_id):
    """
    Endpoint for getting all constellation attempts for a specific user
    """
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!", 404)
    attempts = [attempt.serialize() for attempt in user.constellation_attempts]
    return success_response({"constellation_attempts": attempts}, 200)

@app.route("/api/constellation_attempts/<int:attempt_id>/", methods = ["PUT"])
def increment_attempt(attempt_id):
    """
    Endpoint for incrementing the stars_completed of a constellation attempt
    """
    attempt = Constellation_Attempt.query.filter_by(id = attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)
    attempt.stars_completed += 1
    db.session.commit()
    return success_response(attempt.serialize(), 200)

@app.route("/api/constellation_attempts/<int:attempt_id>/complete", methods = ["PUT"])
def complete_attempt(attempt_id):
    """
    Endpoint for completing a constellation attempt
    """
    attempt = Constellation_Attempt.query.filter_by(id = attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)
    attempt.stars_completed = attempt.constellation.weight
    user = attempt.user
    if user.current_attempt_id == attempt_id:
        user.current_attempt_id = None 
    db.session.commit()
    return success_response({
        "attempt": attempt.serialize(),
        "user_updated": True,
        "message": "Constellation completed successfully!"
    }, 200)

@app.route("/api/constellation_attempts/<int:attempt_id>/", methods = ["DELETE"])
def delete_attempt(attempt_id):
    """
    Endpoint for deleting a constellation attempt
    """
    attempt = Constellation_Attempt.query.filter_by(id = attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)
    user = attempt.user
    if user.current_attempt_id == attempt_id:
        user.current_attempt_id = None 
    db.session.delete(attempt)
    db.session.commit()
    return success_response({"message": "Constellation Attempt deleted successfully!"}, 200)


#------SESSIONS ROUTES-----------------------------------------------------------------------
@app.route("/api/sessions/", methods = ["POST"])
def create_session():
    """
    Endpoint for creating a session
    """
    body = json.loads(request.data)
    user_id = body.get("user_id")
    constellation_attempt_id = body.get("constellation_attempt_id")
    hours = body.get("hours")

    if user_id is None or constellation_attempt_id is None or hours is None:
        return failure_response("Missing user_id, constellation_attempt_id, or hours!", 400)

    # Validate user exists
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!", 404)

    # Validate constellation attempt exists
    attempt = Constellation_Attempt.query.filter_by(id=constellation_attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)

    new_session = Session(
        user_id=user_id,
        constellation_attempt_id=constellation_attempt_id,
        hours=hours
    )
    db.session.add(new_session)
    db.session.commit()
    return success_response(new_session.serialize(), 201)

@app.route("/api/sessions/")
def get_sessions():
    """
    Endpoint for getting all sessions
    """
    sessions = [session.serialize() for session in Session.query.all()]
    return success_response({"sessions": sessions}, 200)

@app.route("/api/sessions/<int:session_id>/")
def get_session_by_id(session_id):
    session = Session.query.filter_by(id = session_id).first()
    if not session:
        return failure_response("session not found", 400)
    return success_response(session.serialize(), 200)

def get_sessions_by_user(user_id):
    """
    Endpoint for getting all sessions by user_id
    """
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("User not found!", 404)
    sessions = []
    for attempt in user.constellation_attempts:
        for session in attempt.sessions:
            sessions.append(session.serialize())
    return success_response({"sessions": sessions}, 200)

@app.route("/api/constellation_attempts/<int:attempt_id>/sessions/")
def get_sessions_by_attempt(attempt_id):
    """
    Endpoint for getting all sessions associated with a constellation attempt
    """
    attempt = Constellation_Attempt.query.filter_by(id = attempt_id).first()
    if attempt is None:
        return failure_response("Constellation Attempt not found!", 404)
    sessions = [session.serialize() for session in attempt.sessions]
    return success_response({"sessions": sessions}, 200)

@app.route("/api/sessions/<int:session_id>/complete", methods=["PUT"])
def complete_session(session_id):
    """
    Endpoint for completing a session
    """
    session = Session.query.filter_by(id=session_id).first()
    if session is None:
        return failure_response("Session not found!", 404)
    session.completed = True
    db.session.commit()
    return success_response(session.serialize(), 200)

@app.route("/api/sessions/<int:session_id>/cancel", methods=["PUT"])
def cancel_session(session_id):
    """
    Endpoint for canceling a session
    """
    session = Session.query.filter_by(id=session_id).first()
    if session is None:
        return failure_response("Session not found!", 404)
    session.is_completed = False
    db.session.commit()
    return success_response(session.serialize(), 200)

#------POST ROUTES-----------------------------------------------------------------------

@app.route("/api/posts/", methods = ["POST"])
def create_post():
    """
    Endpoint for creating a post
    """
    body = json.loads(request.data)
    user_id = body.get("user_id")
    constellation_id = body.get("constellation_id")
    post_type = body.get("post_type")
    if user_id is None or constellation_id is None or post_type is None:
        return failure_response("Missing required fields", 400)
    new_post = Post(user_id = user_id, constellation_id = constellation_id, post_type
                    = post_type)
    db.session.add(new_post)
    db.session.commit()
    return success_response(new_post.serialize(), 201)

@app.route("/api/posts/")
def get_posts():
    """
    Endpoint for getting all posts
    """
    posts = [post.serialize() for post in Post.query.all()]
    return success_response({"posts": posts}, 200)

@app.route("/api/posts/<int:post_id>/")
def get_post_by_id(post_id):
    """
    Endpoint for getting post by post_id
    """
    post = Post.query.filter_by(id = post_id).first()
    if post is None:
        return failure_response("Post not found!", 404)
    return success_response(post.serialize(), 200)

@app.route("/users/<int:user_id>/posts/")
def get_post_by_user(user_id):
    """
    Endpoint for getting post by user id
    """
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("User not found!", 404)
    posts = []
    for post in user.posts:
        posts.append(post.serialize())
    return success_response({"posts": posts}, 200)

@app.route("/constellations/<int:constellation_id>/posts/")
def get_post_by_constellation(constellation_id):
    """
    Endpoint for getting post by constellation id
    """
    constellation = Constellation.query.filter_by(id = constellation_id).first()
    if constellation is None:
        return failure_response("Constellation not found!", 404)
    posts = []
    for post in constellation.posts:
        posts.append(post.serialize())
    return success_response({"posts": posts}, 200)

@app.route("/api/posts/<int:post_id>/", methods = ["DELETE"])
def delete_post(post_id):
    """
    Endpoint for deleting a post
    """
    post = Post.query.filter_by(id = post_id).first()
    if post is None:
        return failure_response("Post not found!", 404)
    db.session.delete(post)
    db.session.commit()
    return success_response({"message": "Post deleted successfully!"}, 200)

@app.route("/api/feed/")
def get_feed():
    """
    Endpoint for getting the feed of all posts
    """
    posts = [post.serialize() for post in Post.query.order_by(Post.created_at.desc()).all()]
    return success_response({"posts": posts}, 200)

#------TESTING ROUTE - IGNORE -----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
