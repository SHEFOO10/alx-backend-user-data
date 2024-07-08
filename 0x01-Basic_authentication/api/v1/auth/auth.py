#!/usr/bin/env python3
""" Auth Class """
from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """ manages the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if endpoint requires auth
            Returns: bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Return value of the Authorization Header """
        return None

    def current_user(self, request=None) -> User:
        """ return the current authenticated user """
        return None
