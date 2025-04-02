# 0x02-Session_authentication

# Session Authentication

This project implements a session-based authentication system for a REST API using Flask, where user sessions are maintained using cookies.

## Project Overview

The session authentication system:
- Authenticates users via email/password
- Creates unique session IDs for authenticated users
- Uses cookies to maintain sessions
- Provides endpoints for login/logout functionality
- Allows retrieving current user information

## Features

- Cookie-based session management
- `/users/me` endpoint to get current authenticated user
- Login endpoint to create sessions
- Logout endpoint to destroy sessions
- Session ID generation and validation
- Secure session handling

## Files Structure

```
api/
├── v1/
│   ├── app.py                # Main Flask application
│   ├── auth/                 # Authentication classes
│   │   ├── auth.py           # Base auth class
│   │   ├── basic_auth.py     # Basic auth implementation
│   │   └── session_auth.py   # Session auth implementation
│   └── views/
│       ├── __init__.py       # Views initialization
│       ├── index.py          # Index view
│       ├── session_auth.py   # Session auth views
│       └── users.py          # User management views
models/
├── base.py                  # Base model class
└── user.py                  # User model
```

## Installation & Usage

1. Clone the repository
2. Ensure Python 3.7 is installed
3. Set required environment variables:
   ```bash
   export API_HOST=0.0.0.0
   export API_PORT=5000
   export AUTH_TYPE=session_auth
   export SESSION_NAME=_my_session_id
   ```

4. Run the application:
   ```bash
   python3 -m api.v1.app
   ```

## API Endpoints

### Session Endpoints
- `POST /api/v1/auth_session/login` 
  - Authenticates user with email/password
  - Creates session and sets session cookie
  - Required data: `email`, `password`
  
- `DELETE /api/v1/auth_session/logout`
  - Destroys current session
  - Requires valid session cookie

### User Endpoints
- `GET /api/v1/users/me`
  - Returns current authenticated user's details
  - Requires valid session cookie

## Examples

**Login:**
```bash
curl "http://0.0.0.0:5000/api/v1/auth_session/login" \
  -XPOST -d "email=test@example.com" -d "password=password"
```

**Get Current User:**
```bash
curl "http://0.0.0.0:5000/api/v1/users/me" \
  --cookie "_my_session_id=abc123"
```

**Logout:**
```bash
curl "http://0.0.0.0:5000/api/v1/auth_session/logout" \
  -XDELETE --cookie "_my_session_id=abc123"
```

## Requirements

- Python 3.7
- Flask
- pycodestyle (for linting)
- All code must be executable
- Proper documentation for all modules, classes and functions


## Tasks

#### 0. Et moi et moi et moi!
- Copy all work from 0x06 Basic Authentication project
- Add new endpoint `GET /users/me` to retrieve authenticated User object
- Update `@app.before_request` in `api/v1/app.py`:
  - Assign `auth.current_user(request)` to `request.current_user`
- Update `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
  - If `<user_id>` is "me", return current authenticated user
  - Otherwise keep normal behavior

#### 1. Empty session
- Create `SessionAuth` class that inherits from `Auth` in `api/v1/auth/session_auth.py`
- Update `api/v1/app.py` to use `SessionAuth` when `AUTH_TYPE=session_auth`

#### 2. Create a session
- Add `user_id_by_session_id` class attribute (dictionary)
- Implement `create_session(self, user_id: str = None)` method:
  - Generates Session ID using `uuid.uuid4()`
  - Stores user_id with session_id in dictionary
  - Returns Session ID

#### 3. User ID for Session ID
- Implement `user_id_for_session_id(self, session_id: str = None)` method:
  - Returns User ID based on Session ID
  - Uses dictionary lookup with `.get()`

#### 4. Session cookie
- Add `session_cookie(self, request=None)` method to `Auth` class:
  - Returns cookie value from request
  - Cookie name defined by `SESSION_NAME` environment variable

#### 5. Before request
- Update `@app.before_request` in `api/v1/app.py`:
  - Add `/api/v1/auth_session/login/` to excluded paths
  - If both `authorization_header` and `session_cookie` return None, abort(401)

#### 6. Use Session ID for identifying a User
- Implement `current_user(self, request=None)` in `SessionAuth`:
  - Gets User ID from session cookie
  - Returns User instance using `User.get()`

#### 7. New view for Session Authentication
- Create `POST /api/v1/auth_session/login` endpoint:
  - Handles email/password authentication
  - Creates session for valid credentials
  - Sets session cookie in response
  - Returns user JSON

#### 8. Logout
- Add `destroy_session(self, request=None)` to `SessionAuth`:
  - Deletes user session
- Create `DELETE /api/v1/auth_session/logout` endpoint:
  - Destroys session and logs user out

#### 9. Expiration? (Advanced)
- Create `SessionExpAuth` that inherits from `SessionAuth`:
  - Adds session expiration functionality
  - Uses `SESSION_DURATION` environment variable

#### 10. Sessions in database (Advanced)
- Create `UserSession` model to store sessions in DB
- Create `SessionDBAuth` that inherits from `SessionExpAuth`:
  - Stores sessions in database instead of memory
  - Implements DB-backed session operations

Each task builds on the previous one to create a complete session authentication system, starting from basic functionality and adding advanced features like expiration and database persistence.
