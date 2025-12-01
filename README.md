# Luminary Backend

Backend API for a study application built with Python, Flask, and SQLAlchemy. This application helps users track their learning progress through constellations (study topics), attempts, sessions, and posts them after completing every constellation.


## Database Schema

- **Users**: Manage user profiles and current study attempts
- **Constellations**: Study topics with difficulty weights
- **Constellation_Attempts**: User progress on specific constellations
- **Sessions**: Individual study sessions with time tracking
- **Posts**: Social posts linked to users and constellations


## API Documentation

### User Routes

#### Create User
- **POST** `/api/users/`
- **Body:**
```json
{
    "display_name": "string (required)"
}
```
- **Response:** User object with full serialization

#### Get All Users
- **GET** `/api/users/`
- **Response:** List of all users with full serialization

#### Get User by ID
- **GET** `/api/users/{user_id}/`
- **Response:** User object with full serialization

#### Get User Total Hours
- **GET** `/api/users/{user_id}/total_hours/`
- **Response:** User's total completed study hours

### Constellation Routes

#### Create Constellation
- **POST** `/api/constellations/`
- **Body:**
```json
{
    "name": "string (required)",
    "weight": "integer (required)"
}
```
- **Response:** Constellation object with full serialization

#### Get All Constellations
- **GET** `/api/constellations/`
- **Response:** List of all constellations with full serialization

#### Get Constellation by ID
- **GET** `/api/constellations/{constellation_id}/`
- **Response:** Constellation object with full serialization

#### Update Constellation
- **PUT** `/api/constellations/{constellation_id}/`
- **Body:**
```json
{
    "name": "string (optional)",
    "weight": "integer (optional)"
}
```
- **Response:** Updated constellation object

#### Delete Constellation
- **DELETE** `/api/constellations/{constellation_id}/`
- **Response:** Success message

### Constellation Attempt Routes

#### Create Constellation Attempt
- **POST** `/api/users/{user_id}/constellation_attempts/`
- **Body:**
```json
{
    "constellation_id": "integer (required)"
}
```
- **Response:** Constellation attempt object with full serialization

#### Get All Constellation Attempts
- **GET** `/api/constellation_attempts/`
- **Response:** List of all constellation attempts with full serialization

#### Get Constellation Attempt by ID
- **GET** `/api/constellation_attempts/{attempt_id}/`
- **Response:** Constellation attempt object with full serialization

#### Get User's Constellation Attempts
- **GET** `/api/users/{user_id}/constellation_attempts/`
- **Response:** List of user's constellation attempts

#### Increment Attempt Progress
- **PUT** `/api/constellation_attempts/{attempt_id}/`
- **Body:** None required
- **Response:** Updated constellation attempt (stars_completed += 1)

#### Complete Constellation Attempt
- **PUT** `/api/constellation_attempts/{attempt_id}/complete`
- **Body:** None required
- **Response:** Completed attempt with user update confirmation

#### Delete Constellation Attempt
- **DELETE** `/api/constellation_attempts/{attempt_id}/`
- **Response:** Success message

### Session Routes

#### Create Session
- **POST** `/api/sessions/`
- **Body:**
```json
{
    "user_id": "integer (required)",
    "constellation_attempt_id": "integer (required)",
    "minutes": "integer (required)"
}
```
- **Response:** Session object with full serialization

#### Get All Sessions
- **GET** `/api/sessions/`
- **Response:** List of all sessions with full serialization

#### Get Session by ID
- **GET** `/api/sessions/{session_id}/`
- **Response:** Session object with full serialization

#### Get Sessions by Constellation Attempt
- **GET** `/api/constellation_attempts/{attempt_id}/sessions/`
- **Response:** List of sessions for the constellation attempt

#### Complete Session
- **PUT** `/api/sessions/{session_id}/complete`
- **Body:** None required
- **Response:** Updated session (is_completed = true)

#### Cancel Session
- **PUT** `/api/sessions/{session_id}/cancel`
- **Body:** None required
- **Response:** Updated session (is_completed = false)

### Post Routes

#### Create Post
- **POST** `/api/posts/`
- **Body:**
```json
{
    "user_id": "integer (required)",
    "constellation_id": "integer (required)",
    "post_type": "string (required)"
}
```
- **Response:** Post object with full serialization

#### Get All Posts
- **GET** `/api/posts/`
- **Response:** List of all posts with full serialization

#### Get Post by ID
- **GET** `/api/posts/{post_id}/`
- **Response:** Post object with full serialization

#### Get Posts by User
- **GET** `/users/{user_id}/posts/`
- **Response:** List of user's posts

#### Get Posts by Constellation
- **GET** `/constellations/{constellation_id}/posts/`
- **Response:** List of posts for the constellation

#### Delete Post
- **DELETE** `/api/posts/{post_id}/`
- **Response:** Success message

#### Get Feed
- **GET** `/api/feed/`
- **Response:** All posts ordered by creation date (newest first)

## Response Format

All successful responses follow this format:
```json
{
    "data": "response_data",
    "status_code": 200
}
```

All error responses follow this format:
```json
{
    "error": "error_message",
    "status_code": 400 or 404
}
```

Created by Olric Zeng and Tran Tran