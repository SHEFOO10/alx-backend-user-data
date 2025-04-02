# 0x01-Basic_authentication

# Basic Authentication

This project implements a basic authentication system for a REST API using Flask, where users authenticate with email and password via Base64-encoded Authorization headers.

## Project Overview

The basic authentication system:
- Authenticates users via email/password credentials
- Validates Base64-encoded Authorization headers
- Protects API endpoints requiring authentication
- Implements proper error handling (401 Unauthorized, 403 Forbidden)

## Features

- Base64 encoding/decoding of credentials
- Authorization header validation
- User credential extraction
- Protected routes with authentication requirements
- Proper error responses for unauthorized access

## Files Structure

```
api/
├── v1/
│   ├── app.py                # Main Flask application
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth.py           # Base auth class
│   │   └── basic_auth.py     # Basic auth implementation
│   └── views/
│       ├── __init__.py
│       └── index.py          # View routes
models/
└── user.py                  # User model
```

## Installation & Usage

1. Clone the repository
2. Install requirements:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export API_HOST=0.0.0.0
   export API_PORT=5000
   export AUTH_TYPE=basic_auth
   ```
4. Run the application:
   ```bash
   python3 -m api.v1.app
   ```

## API Endpoints

### Public Endpoints
- `GET /api/v1/status` - API status
- `GET /api/v1/unauthorized` - Returns 401 error
- `GET /api/v1/forbidden` - Returns 403 error

### Protected Endpoints
- `GET /api/v1/users` - List all users (requires auth)
- Other user endpoints (CRUD operations)

## Examples

**Get API status:**
```bash
curl "http://0.0.0.0:5000/api/v1/status"
```

**Try unauthorized endpoint:**
```bash
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```

**Access protected endpoint with credentials:**
```bash
curl "http://0.0.0.0:5000/api/v1/users" \
  -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```

## Requirements

- Python 3.7
- Flask
- pycodestyle (for linting)
- All code must be executable
- Proper documentation for all modules, classes and functions

## Tasks

#### 0. Simple-basic-API
- Set up basic Flask API with User model
- Implement status endpoint

#### 1. Error handler: Unauthorized
- Add 401 error handler returning JSON
- Create `/api/v1/unauthorized` endpoint

#### 2. Error handler: Forbidden
- Add 403 error handler returning JSON
- Create `/api/v1/forbidden` endpoint

#### 3. Auth class
- Create base Auth class with:
  - `require_auth()`
  - `authorization_header()`
  - `current_user()`

#### 4. Define which routes don't need authentication
- Implement path exclusion logic in `require_auth()`

#### 5. Request validation!
- Add request filtering in `app.py`
- Validate Authorization header

#### 6. Basic auth
- Create BasicAuth class inheriting from Auth
- Configure auth type based on environment

#### 7. Basic - Base64 part
- Implement Base64 header extraction

#### 8. Basic - Base64 decode
- Implement Base64 decoding

#### 9. Basic - User credentials
- Extract user credentials from decoded string

#### 10. Basic - User object
- Retrieve User instance from credentials

#### 11. Basic - Overload current_user
- Complete authentication flow
- Protect endpoints with Basic Auth

#### 12. Basic - Allow password with ":" (Advanced)
- Handle passwords containing colons

#### 13. Require auth with stars (Advanced)
- Implement wildcard path matching for excluded paths

Each task builds on the previous one to create a complete basic authentication system, from setting up the API to implementing the full authentication flow.
