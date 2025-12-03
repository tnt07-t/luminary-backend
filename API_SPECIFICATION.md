# API Specification

Complete API documentation with request/response examples for the Luminary Backend.

## User Routes

### Create User
**POST** `/api/users/`

**Request Body:**
```json
{
    "display_name": "John Doe"
}
```

**Response (201):**
```json
{
    "id": 1,
    "display_name": "John Doe",
    "current_attempt_id": null,
    "current_attempt": null,
    "constellation_attempts": [],
    "sessions": [],
    "posts": []
}
```

### Get All Users
**GET** `/api/users/`

**Response (200):**
```json
{
    "users": [
        {
            "id": 1,
            "display_name": "John Doe",
            "current_attempt_id": 2,
            "current_attempt": {
                "id": 2,
                "user_id": 1,
                "constellation_id": 1,
                "stars_completed": 3
            },
            "constellation_attempts": [
                {
                    "id": 2,
                    "user_id": 1,
                    "constellation_id": 1,
                    "stars_completed": 3
                }
            ],
            "sessions": [
                {
                    "id": 1,
                    "user_id": 1,
                    "constellation_attempt_id": 2,
                    "is_completed": true,
                    "minutes": 45
                }
            ],
            "posts": [
                {
                    "id": 1,
                    "post_type": "completion",
                    "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
                    "study_duration": 45,
                    "created_at": "2025-12-01T10:30:00"
                }
            ]
        }
    ]
}
```

### Get User by ID
**GET** `/api/users/1/`

**Response (200):**
```json
{
    "id": 1,
    "display_name": "John Doe",
    "current_attempt_id": 2,
    "current_attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 3
    },
    "constellation_attempts": [
        {
            "id": 2,
            "user_id": 1,
            "constellation_id": 1,
            "stars_completed": 3
        }
    ],
    "sessions": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_attempt_id": 2,
            "is_completed": true,
            "minutes": 45
        }
    ],
    "posts": []
}
```

### Get User Total Minutes
**GET** `/api/users/1/total_minutes/`

**Response (200):**
```json
{
    "user_id": 1,
    "display_name": "John Doe",
    "total_minutes": 180
}
```

### Get User Completed Constellations
**GET** `/api/users/1/completed_constellations/`

**Response (200):**
```json
{
    "user_id": 1,
    "display_name": "John Doe",
    "completed_constellations": [
        {
            "id": 1,
            "name": "Triangulum",
            "weight": 3,
            "user_attempts": [
                {
                    "id": 1,
                    "user_id": 1,
                    "constellation_id": 1,
                    "stars_completed": 3
                }
            ],
            "posts": [
                {
                    "id": 1,
                    "post_type": "completion",
                    "message": "Just completed Triangulum! Great start! 🌟",
                    "study_duration": 30,
                    "created_at": "2025-12-02T10:15:00"
                }
            ]
        },
        {
            "id": 2,
            "name": "Delphinus",
            "weight": 5,
            "user_attempts": [
                {
                    "id": 2,
                    "user_id": 1,
                    "constellation_id": 2,
                    "stars_completed": 5
                }
            ],
            "posts": [
                {
                    "id": 3,
                    "post_type": "completion",
                    "message": "Delphinus conquered! Moving up in difficulty! 🐬",
                    "study_duration": 75,
                    "created_at": "2025-12-02T14:30:00"
                }
            ]
        }
    ],
    "num_completed": 2
}
```

## Constellation Routes

### Create Constellation
**POST** `/api/constellations/`

**Request Body:**
```json
{
    "name": "Cassiopeia",
    "weight": 5
}
```

**Response (201):**
```json
{
    "id": 1,
    "name": "Cassiopeia",
    "weight": 5,
    "user_attempts": [],
    "posts": []
}
```

### Get All Constellations
**GET** `/api/constellations/`

**Response (200):**
```json
{
    "constellations": [
        {
            "id": 1,
            "name": "Cassiopeia",
            "weight": 5,
            "user_attempts": [
                {
                    "id": 2,
                    "user_id": 1,
                    "constellation_id": 1,
                    "stars_completed": 3
                }
            ],
            "posts": [
                {
                    "id": 1,
                    "post_type": "completion",
                    "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
                    "study_duration": 45,
                    "created_at": "2025-12-01T10:30:00"
                }
            ]
        }
    ]
}
```

### Get Constellation by ID
**GET** `/api/constellations/1/`

**Response (200):**
```json
{
    "id": 1,
    "name": "Cassiopeia",
    "weight": 5,
    "user_attempts": [
        {
            "id": 2,
            "user_id": 1,
            "constellation_id": 1,
            "stars_completed": 3
        }
    ],
    "posts": []
}
```

### Update Constellation
**PUT** `/api/constellations/1/`

**Request Body:**
```json
{
    "name": "Big Dipper",
    "weight": 7
}
```

**Response (200):**
```json
{
    "id": 1,
    "name": "Big Dipper",
    "weight": 7,
    "user_attempts": [],
    "posts": []
}
```

### Delete Constellation
**DELETE** `/api/constellations/1/`

**Response (200):**
```json
{
    "message": "Constellation deleted successfully!"
}
```

## Constellation Attempt Routes

### Create Constellation Attempt
**POST** `/api/users/1/constellation_attempts/`

**Request Body:**
```json
{
    "constellation_id": 1
}
```

**Response (201):**
```json
{
    "id": 2,
    "user_id": 1,
    "constellation_id": 1,
    "stars_completed": 0,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation": {
        "id": 1,
        "name": "Cassiopeia",
        "weight": 5
    },
    "sessions": []
}
```

### Get All Constellation Attempts
**GET** `/api/constellation_attempts/`

**Response (200):**
```json
{
    "constellation_attempts": [
        {
            "id": 2,
            "user_id": 1,
            "constellation_id": 1,
            "stars_completed": 3,
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            },
            "sessions": [
                {
                    "id": 1,
                    "user_id": 1,
                    "constellation_attempt_id": 2,
                    "is_completed": true,
                    "minutes": 45
                }
            ]
        }
    ]
}
```

### Get Constellation Attempt by ID
**GET** `/api/constellation_attempts/2/`

**Response (200):**
```json
{
    "id": 2,
    "user_id": 1,
    "constellation_id": 1,
    "stars_completed": 3,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation": {
        "id": 1,
        "name": "Cassiopeia",
        "weight": 5
    },
    "sessions": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_attempt_id": 2,
            "is_completed": true,
            "minutes": 45
        }
    ]
}
```

### Get User's Constellation Attempts
**GET** `/api/users/1/constellation_attempts/`

**Response (200):**
```json
{
    "constellation_attempts": [
        {
            "id": 2,
            "user_id": 1,
            "constellation_id": 1,
            "stars_completed": 3,
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            },
            "sessions": []
        }
    ]
}
```

### Increment Attempt Progress
**PUT** `/api/constellation_attempts/2/`

**Response (200):**
```json
{
    "id": 2,
    "user_id": 1,
    "constellation_id": 1,
    "stars_completed": 4,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation": {
        "id": 1,
        "name": "Cassiopeia",
        "weight": 5
    },
    "sessions": []
}
```

### Complete Constellation Attempt
**PUT** `/api/constellation_attempts/2/complete`

**Response (200):**
```json
{
    "attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 5,
        "user": {
            "id": 1,
            "display_name": "John Doe"
        },
        "constellation": {
            "id": 1,
            "name": "Cassiopeia",
            "weight": 5
        },
        "sessions": []
    },
    "user_updated": true,
    "message": "Constellation completed successfully!"
}
```

### Delete Constellation Attempt
**DELETE** `/api/constellation_attempts/2/`

**Response (200):**
```json
{
    "message": "Constellation Attempt deleted successfully!"
}
```

## Session Routes

### Create Session
**POST** `/api/sessions/`

**Request Body:**
```json
{
    "user_id": 1,
    "constellation_attempt_id": 2,
    "minutes": 45
}
```

**Response (201):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_attempt_id": 2,
    "is_completed": false,
    "minutes": 45,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation_attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 3
    }
}
```

### Get All Sessions
**GET** `/api/sessions/`

**Response (200):**
```json
{
    "sessions": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_attempt_id": 2,
            "is_completed": true,
            "minutes": 45,
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation_attempt": {
                "id": 2,
                "user_id": 1,
                "constellation_id": 1,
                "stars_completed": 3
            }
        }
    ]
}
```

### Get Session by ID
**GET** `/api/sessions/1/`

**Response (200):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_attempt_id": 2,
    "is_completed": true,
    "minutes": 45,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation_attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 3
    }
}
```

### Get Sessions by Constellation Attempt
**GET** `/api/constellation_attempts/2/sessions/`

**Response (200):**
```json
{
    "sessions": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_attempt_id": 2,
            "is_completed": true,
            "minutes": 45,
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation_attempt": {
                "id": 2,
                "user_id": 1,
                "constellation_id": 1,
                "stars_completed": 3
            }
        }
    ]
}
```

### Complete Session
**PUT** `/api/sessions/1/complete`

**Response (200):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_attempt_id": 2,
    "is_completed": true,
    "minutes": 45,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation_attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 3
    }
}
```

### Cancel Session
**PUT** `/api/sessions/1/cancel`

**Response (200):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_attempt_id": 2,
    "is_completed": false,
    "minutes": 45,
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation_attempt": {
        "id": 2,
        "user_id": 1,
        "constellation_id": 1,
        "stars_completed": 3
    }
}
```

## Post Routes

### Create Post
**POST** `/api/posts/`

**Request Body:**
```json
{
    "user_id": 1,
    "constellation_id": 1,
    "post_type": "completion",
    "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
    "study_duration": 45
}
```

**Note:** 
- `post_type` must be either:
  - `"completion"` - when a constellation is fully completed
  - `"progress"` - when a session/star is completed
- `message` (optional): Text message for the post
- `study_duration` (optional): Study time in minutes

**Response (201):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_id": 1,
    "post_type": "completion",
    "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
    "study_duration": 45,
    "created_at": "2025-12-01T10:30:00",
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation": {
        "id": 1,
        "name": "Cassiopeia",
        "weight": 5
    }
}
```

### Get All Posts
**GET** `/api/posts/`

**Response (200):**
```json
{
    "posts": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_id": 1,
            "post_type": "completion",
            "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
            "study_duration": 45,
            "created_at": "2025-12-01T10:30:00",
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            }
        }
    ]
}
```

### Get Post by ID
**GET** `/api/posts/1/`

**Response (200):**
```json
{
    "id": 1,
    "user_id": 1,
    "constellation_id": 1,
    "post_type": "completion",
    "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
    "study_duration": 45,
    "created_at": "2025-12-01T10:30:00",
    "user": {
        "id": 1,
        "display_name": "John Doe"
    },
    "constellation": {
        "id": 1,
        "name": "Cassiopeia",
        "weight": 5
    }
}
```

### Get Posts by User
**GET** `/users/1/posts/`

**Response (200):**
```json
{
    "posts": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_id": 1,
            "post_type": "completion",
            "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
            "study_duration": 45,
            "created_at": "2025-12-01T10:30:00",
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            }
        }
    ]
}
```

### Get Posts by Constellation
**GET** `/constellations/1/posts/`

**Response (200):**
```json
{
    "posts": [
        {
            "id": 1,
            "user_id": 1,
            "constellation_id": 1,
            "post_type": "completion",
            "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
            "study_duration": 45,
            "created_at": "2025-12-01T10:30:00",
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            }
        }
    ]
}
```

### Delete Post
**DELETE** `/api/posts/1/`

**Response (200):**
```json
{
    "message": "Post deleted successfully!"
}
```

### Get Feed
**GET** `/api/feed/`

**Response (200):**
```json
{
    "posts": [
        {
            "id": 2,
            "user_id": 1,
            "constellation_id": 1,
            "post_type": "progress",
            "message": "Made great progress on Cassiopeia today! 3 stars completed ⭐",
            "study_duration": 30,
            "created_at": "2025-12-01T14:22:00",
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            }
        },
        {
            "id": 1,
            "user_id": 1,
            "constellation_id": 1,
            "post_type": "completion",
            "message": "Just completed Cassiopeia! Amazing learning experience 🌟",
            "study_duration": 45,
            "created_at": "2025-12-01T10:30:00",
            "user": {
                "id": 1,
                "display_name": "John Doe"
            },
            "constellation": {
                "id": 1,
                "name": "Cassiopeia",
                "weight": 5
            }
        }
    ]
}
```

## Error Responses

All error responses follow this format:

**404 Not Found:**
```json
{
    "error": "User not found!"
}
```

**400 Bad Request:**
```json
{
    "error": "Missing required fields"
}
```

## Notes

- All timestamps are in ISO 8601 format
- All IDs are integers starting from 1
- Minutes are tracked as integers
- **Automatic Minute Calculation**: User `total_minutes` are automatically updated when sessions change (completed, modified, or deleted)
- Post types:
  - `"completion"` - when a constellation is fully completed
  - `"progress"` - when a session/star is completed
- Post fields:
  - `message` (optional): Custom text message for the post
  - `study_duration` (optional): Study time in minutes for this session
- Sessions default to `is_completed: false` when created
- Constellation attempts start with `stars_completed: 0`
- The `total_minutes` field in user responses reflects real-time calculations from completed sessions