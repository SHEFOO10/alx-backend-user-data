#!/usr/bin/env python3
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        import bcrypt
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """ Register User """
        user_exists = None
        try:
            user_exists = self._db.find_user_by(email=email)
        except Exception:
            pass
        if user_exists:
            raise ValueError("User {} already exists".format(email))
        hashed_password = Auth._hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user
