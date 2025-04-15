# ALX Backend User Data - Authentication Services

## Overview

This repository contains a comprehensive collection of authentication services implemented as part of the ALX Backend specialization. It includes three major authentication implementations:

1. **Basic Authentication** - Simple token-based authentication
2. **Session Authentication** - Cookie-based session management
3. **User Authentication Service** - Full-featured authentication system with database integration

## Projects

### 1. [Basic Authentication](0x01-Basic_authentication/)
A simple REST API authentication system using Base64-encoded credentials.

**Key Features:**
- Base64 encoding/decoding of credentials
- Authorization header validation
- Protected routes with authentication requirements
- Proper error handling (401 Unauthorized, 403 Forbidden)

### 2. [Session Authentication](0x02-Session_authentication/)
A more advanced authentication system using session cookies.

**Key Features:**
- Cookie-based session management
- Session ID generation and validation
- Login/logout functionality
- `/users/me` endpoint for current user
- Session expiration (advanced)
- Database-backed sessions (advanced)

### 3. [User Authentication Service](0x03-user_authentication_service/)
A complete user authentication service with database integration.

**Key Features:**
- User registration with email/password
- Password hashing with bcrypt
- Session management
- Password reset functionality
- SQLAlchemy database integration
- Comprehensive API endpoints

## Technical Stack

- **Framework**: Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Security**: bcrypt for password hashing
- **Session Management**: UUID tokens
- **Testing**: Python unittest

## Getting Started

### Prerequisites
- Python 3.7+
- pip
- SQLite (for User Authentication Service)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SHEFOO10/alx-backend-user-data.git
   cd alx-backend-user-data
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Services

Each service can be run independently:

1. **Basic Authentication**:
   ```bash
   cd 0x01-Basic_authentication/
   python3 -m api.v1.app
   ```

2. **Session Authentication**:
   ```bash
   cd 0x02-Session_authentication/
   python3 -m api.v1.app
   ```

3. **User Authentication Service**:
   ```bash
   cd 0x03-user_authentication_service/
   python app.py
   ```

## API Documentation

Each service has its own API documentation in its respective directory:

- [Basic Authentication API](0x01-Basic_authentication/README.md)
- [Session Authentication API](0x02-Session_authentication/README.md)
- [User Authentication Service API](0x03-user_authentication_service/README.md)

## Testing

Integration tests are provided for the User Authentication Service:

```bash
cd 0x03-user_authentication_service/
python main.py
```

## Learning Objectives

Through these projects, you will learn:

1. Authentication concepts and implementation
2. Security best practices (password hashing, session management)
3. REST API design with Flask
4. Database integration with SQLAlchemy
5. Error handling and validation
6. Testing authentication flows
