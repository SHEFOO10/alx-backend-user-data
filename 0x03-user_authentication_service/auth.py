#!/usr/bin/env python3
""" Module for Authentication """


from uuid import uuid4
from typing import Union

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

    def create_session(self, email: str) -> Union[str, None]:
        """ Create session for the given user """
        try:
            user = self._db.find_user_by(email=email)

            sessionId = _generate_uuid()
            self._db.update_user(user.id, session_id=sessionId)
            return sessionId
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ get the user associated with the given session id """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destory User current session """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Generate reset token for the user """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update user password with the given token """
        if not reset_token or not password:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                            bcrypt.gensalt())
            self._db.update_user(user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError()


def _hash_password(password: str) -> bytes:
    """ generate password hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate UUID """
    return str(uuid4())
