#!/usr/bin/env python3
""" Module for Authentication """


from uuid import uuid4

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register User """
        user_exists = None
        try:
            user_exists = self._db.find_user_by(email=email)
        except Exception:
            pass
        if user_exists:
            raise ValueError("User {} already exists".format(email))
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if email and password match a registered user

        Args:
            email (str): the email of the user
            password (str): the password of the user
        Returns:
            bool: True if if email and password match a registered user
            otherwise False
        """
        try:
            user = self._db.find_user_by(email=email)

            password_bytes = password.encode('utf-8')
            hashed_password = user.hashed_password

            if bcrypt.checkpw(password_bytes, hashed_password):
                return True
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """ generate password hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate UUID """
    return str(uuid4())
