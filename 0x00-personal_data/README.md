# ALX Personal Data Protection Project (0x00-personal_data)

## Overview

This project implements secure logging and data protection practices for handling Personally Identifiable Information (PII) in Python applications. It includes tools for obfuscating sensitive data in logs, secure database connections, and password hashing.

## Features

1. **Data Obfuscation**
   - Regex-based field redaction in log messages
   - Custom logging formatter for PII protection
   - Configurable sensitive field filtering

2. **Secure Database Integration**
   - Environment variable-based credentials
   - MySQL connector with protected access
   - Automatic PII filtering in query results

3. **Password Security**
   - bcrypt-based password hashing
   - Secure password validation
   - Salted hashes for protection against rainbow tables

## Project Structure

```
alx-backend-user-data/
└── 0x00-personal_data/
    ├── filtered_logger.py    # Log filtering and database utilities
    ├── encrypt_password.py   # Password hashing functions
    ├── user_data.csv         # Sample PII data
    └── main.py              # Example usage
```

## Technical Implementation

### 1. Data Obfuscation Tools

#### `filter_datum(fields, redaction, message, separator)`
- Obfuscates specified fields in log messages using regex
- Example:
  ```python
  filter_datum(["password", "ssn"], "***", "user=test;password=123;ssn=456", ";")
  # Returns: "user=test;password=***;ssn=***"
  ```

#### `RedactingFormatter`
- Custom logging formatter that automatically redacts PII
- Configurable fields to obfuscate
- Standardized log format with timestamp and severity

### 2. Database Utilities

#### `get_db()`
- Securely connects to MySQL database using environment variables
- Required environment variables:
  - `PERSONAL_DATA_DB_USERNAME`
  - `PERSONAL_DATA_DB_PASSWORD`
  - `PERSONAL_DATA_DB_HOST`
  - `PERSONAL_DATA_DB_NAME`

#### `main()`
- Example implementation that:
  1. Connects to database
  2. Retrieves user data
  3. Logs information with PII redaction

### 3. Password Security

#### `hash_password(password)`
- Generates salted bcrypt hash of passwords
- Returns bytes for secure storage

#### `is_valid(hashed_password, password)`
- Verifies if password matches the stored hash
- Uses bcrypt's timing-attack resistant comparison

## Usage Examples

### Log Filtering
```python
from filtered_logger import filter_datum

result = filter_datum(
    ["email", "ssn"],
    "***",
    "name=John;email=john@example.com;ssn=123-45-6789;password=secret",
    ";"
)
print(result)
```

### Secure Logging
```python
from filtered_logger import get_logger

logger = get_logger()
logger.info("name=Alice;email=alice@example.com;ssn=987-65-4321")
# Logs: [HOLBERTON] user_data INFO ... name=***;email=***;ssn=***;
```

### Password Hashing
```python
from encrypt_password import hash_password, is_valid

hashed = hash_password("SecurePass123")
print(is_valid(hashed, "SecurePass123"))  # True
print(is_valid(hashed, "WrongPass"))     # False
```

## PII Protection Standards

The project identifies and protects these common PII fields:
- Names
- Email addresses
- Phone numbers
- Social Security Numbers (SSN)
- Passwords
- IP addresses (partial protection)

## Setup Instructions

1. Install requirements:
   ```bash
   pip install mysql-connector-python bcrypt
   ```

2. Set environment variables:
   ```bash
   export PERSONAL_DATA_DB_USERNAME=your_username
   export PERSONAL_DATA_DB_PASSWORD=your_password
   export PERSONAL_DATA_DB_HOST=localhost
   export PERSONAL_DATA_DB_NAME=your_db
   ```

3. Run the logger:
   ```bash
   python filtered_logger.py
   ```

## Security Best Practices Implemented

1. Never store credentials in code
2. Always hash passwords with salt
3. Redact sensitive information in logs
4. Use environment variables for configuration
5. Implement proper error handling
6. Follow principle of least privilege for database access

## Why This Matters

This project demonstrates critical security practices for handling user data:
- Prevents sensitive data exposure in logs
- Protects against credential leaks
- Implements defense-in-depth for authentication systems
- Meets compliance requirements for PII protection

The techniques shown are applicable to production systems handling user data under regulations like GDPR, CCPA, and HIPAA.
