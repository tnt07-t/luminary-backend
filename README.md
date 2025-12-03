# Luminary Backend

Backend API for a study application built with Python, Flask, and SQLAlchemy. This application helps users track their learning progress through constellations (study topics), attempts, sessions, and posts them after completing every constellation.


## Database Schema

- **Users**: Manage user profiles and current study attempts
- **Constellations**: Study topics with difficulty weights  
- **Constellation_Attempts**: User progress on specific constellations
- **Sessions**: Individual study sessions with time tracking
- **Posts**: Social posts with optional messages and study duration tracking

## Key Features

- **Automatic Minute Tracking**: User total minutes are automatically updated when sessions are completed, modified, or deleted
- **Session Management**: Track individual study sessions with completion status
- **Progress Tracking**: Monitor constellation completion with star-based progress
- **Social Feed**: Share achievements and progress with completion/progress posts


## API Overview

For detailed API documentation with complete request/response examples, see: **[API Specification](./API_SPECIFICATION.md)**

### Available Endpoints

#### User Management
- `POST /api/users/` - Create a new user
- `GET /api/users/` - Get all users  
- `GET /api/users/{user_id}/` - Get user by ID
- `GET /api/users/{user_id}/total_minutes/` - Get user's total study minutes

#### Constellation Management  
- `POST /api/constellations/` - Create a constellation
- `GET /api/constellations/` - Get all constellations
- `GET /api/constellations/{id}/` - Get constellation by ID
- `PUT /api/constellations/{id}/` - Update constellation
- `DELETE /api/constellations/{id}/` - Delete constellation

#### Study Progress Tracking
- `POST /api/users/{user_id}/constellation_attempts/` - Start constellation attempt
- `GET /api/constellation_attempts/` - Get all attempts
- `GET /api/constellation_attempts/{id}/` - Get attempt by ID  
- `GET /api/users/{user_id}/constellation_attempts/` - Get user's attempts
- `PUT /api/constellation_attempts/{id}/` - Increment progress (+1 star)
- `PUT /api/constellation_attempts/{id}/complete` - Mark attempt as completed
- `DELETE /api/constellation_attempts/{id}/` - Delete attempt

#### Session Logging
- `POST /api/sessions/` - Create study session
- `GET /api/sessions/` - Get all sessions
- `GET /api/sessions/{id}/` - Get session by ID
- `GET /api/constellation_attempts/{id}/sessions/` - Get sessions for attempt
- `PUT /api/sessions/{id}/complete` - Mark session as completed  
- `PUT /api/sessions/{id}/cancel` - Mark session as incomplete

#### Social Features
- `POST /api/posts/` - Create a post
- `GET /api/posts/` - Get all posts
- `GET /api/posts/{id}/` - Get post by ID
- `GET /users/{user_id}/posts/` - Get user's posts
- `GET /constellations/{id}/posts/` - Get constellation's posts
- `DELETE /api/posts/{id}/` - Delete post
- `GET /api/feed/` - Get chronological feed of all posts

#### Utility Features
- `POST /api/users/sync-minutes/` - Recalculate all users' total minutes




---
Created by Olric Zeng and Tran Tran