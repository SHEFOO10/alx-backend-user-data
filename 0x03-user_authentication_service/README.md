# 0x03-user_authentication_service

This repository contains a Flask-based user authentication service with SQLAlchemy as the ORM and bcrypt for password hashing. Below is an overview of each task implemented:
# User Authentication Service - Project Overview

## Project Structure

```
alx-backend-user-data/
└── 0x03-user_authentication_service/
    ├── app.py               # Flask application with all routes
    ├── auth.py              # Auth class with core authentication logic
    ├── db.py                # Database interaction class
    ├── user.py              # User model definition
    ├── main.py              # Integration test script
    └── README.md            # Project documentation
```

## Key Features

1. **User Management**
   - Secure user registration with email/password
   - Password hashing using bcrypt
   - Unique email validation

2. **Session Management**
   - Session creation with UUID tokens
   - Session validation middleware
   - Secure logout functionality

3. **Authentication Flow**
   - Login with email/password
   - Protected routes requiring valid sessions
   - Profile access control

4. **Password Recovery**
   - Reset token generation
   - Secure password update flow
   - Token invalidation after use

5. **Database Integration**
   - SQLAlchemy ORM for database operations
   - SQLite database (can be configured for other DBMS)
   - User model with all required fields

## Technical Stack

- **Backend Framework**: Flask
- **Database ORM**: SQLAlchemy
- **Password Hashing**: bcrypt
- **Session Management**: UUID tokens
- **Testing**: Python unittest via integration tests

## API Endpoints

| Endpoint           | Method | Description                          |
|--------------------|--------|--------------------------------------|
| /                  | GET    | Welcome message                      |
| /users             | POST   | Register new user                    |
| /sessions          | POST   | User login                           |
| /sessions          | DELETE | User logout                          |
| /profile           | GET    | Get user profile                     |
| /reset_password    | POST   | Request password reset token         |
| /reset_password    | PUT    | Update password with reset token     |

## Security Features

- All passwords are hashed with bcrypt before storage
- Session tokens are randomly generated UUIDs
- No sensitive data exposed in API responses
- Proper error handling for invalid requests
- CSRF protection via session tokens

## How to Use

1. **Setup**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python app.py
   ```

3. **Run tests**:
   ```bash
   python main.py
   ```

## Example Usage

1. Register a user:
   ```bash
   curl -XPOST localhost:5000/users -d 'email=test@example.com' -d 'password=secure123'
   ```

2. Login:
   ```bash
   curl -XPOST localhost:5000/sessions -d 'email=test@example.com' -d 'password=secure123' -v
   ```

3. Access profile:
   ```bash
   curl -XGET localhost:5000/profile -b "session_id=<your_session_id>"
   ```

4. Reset password:
   ```bash
   # Request token
   curl -XPOST localhost:5000/reset_password -d 'email=test@example.com'
   
   # Update password
   curl -XPUT localhost:5000/reset_password -d 'email=test@example.com' -d 'reset_token=<token>' -d 'new_password=newsecure123'
   ```

This service provides a complete authentication solution that can be integrated into larger applications or used as a reference implementation for Flask-based authentication systems.
## Task 0: User Model
- Created a SQLAlchemy model named `User` for a database table named `users`
- Attributes:
  - `id`: integer primary key
  - `email`: non-nullable string
  - `hashed_password`: non-nullable string
  - `session_id`: nullable string
  - `reset_token`: nullable string

## Task 1: Create User
- Implemented `add_user` method in DB class
- Takes email and hashed_password as arguments
- Saves user to database and returns User object

## Task 2: Find User
- Implemented `find_user_by` method in DB class
- Takes arbitrary keyword arguments to filter users
- Raises `NoResultFound` if no user found
- Raises `InvalidRequestError` for invalid query arguments

## Task 3: Update User
- Implemented `update_user` method in DB class
- Takes user_id and arbitrary keyword arguments for updates
- Raises ValueError if invalid user attribute is passed

## Task 4: Hash Password
- Implemented `_hash_password` method
- Takes password string, returns salted hash as bytes
- Uses bcrypt.hashpw for hashing

## Task 5: Register User
- Implemented `register_user` in Auth class
- Takes email and password, hashes password
- Raises ValueError if user already exists
- Returns created User object

## Task 6: Basic Flask App
- Created basic Flask app with single GET route "/"
- Returns JSON: `{"message": "Bienvenue"}`

## Task 7: Register User Endpoint
- Implemented POST /users route
- Registers new user with email and password
- Returns 400 if email already registered

## Task 8: Credentials Validation
- Implemented `valid_login` method in Auth class
- Checks email and password against database
- Returns True if valid, False otherwise

## Task 9: Generate UUIDs
- Implemented `_generate_uuid` helper function
- Returns string representation of new UUID

## Task 10: Get Session ID
- Implemented `create_session` method in Auth class
- Generates session ID for user and stores in database
- Returns session ID string

## Task 11: Login Endpoint
- Implemented POST /sessions route
- Validates login credentials
- Sets session_id cookie on successful login
- Returns 401 for invalid credentials

## Task 12: Find User by Session
- Implemented `get_user_from_session_id` method
- Returns User object for valid session ID
- Returns None for invalid/expired sessions

## Task 13: Destroy Session
- Implemented `destroy_session` method
- Updates user's session_id to None

## Task 14: Logout Endpoint
- Implemented DELETE /sessions route
- Destroys session based on session_id cookie
- Redirects to home page or returns 403

## Task 15: Profile Endpoint
- Implemented GET /profile route
- Returns user email for valid session
- Returns 403 for invalid session

## Task 16: Reset Password Token
- Implemented `get_reset_password_token` method
- Generates and stores reset token for user
- Raises ValueError for invalid email

## Task 17: Reset Token Endpoint
- Implemented POST /reset_password route
- Generates reset token for valid email
- Returns 403 for invalid email

## Task 18: Update Password
- Implemented `update_password` method
- Updates password using reset token
- Raises ValueError for invalid token

## Task 19: Update Password Endpoint
- Implemented PUT /reset_password route
- Updates password with email, token and new password
- Returns 403 for invalid token

## Task 20: End-to-end Integration Test
- Created test script that exercises all endpoints
- Tests registration, login, profile access, logout, and password reset
- Uses assertions to validate responses

The service provides a complete authentication flow with user registration, session management, and password reset functionality.
