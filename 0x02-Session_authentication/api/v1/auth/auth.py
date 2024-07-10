#!/usr/bin/env python3
""" Auth Class """
from flask import request
from typing import List, TypeVar
import re
User = TypeVar('User')


class Auth:
    """ manages the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if endpoint requires auth
            Returns: bool
        """
        if path is None or excluded_paths is None:
            return True
        for i in excluded_paths:
            if path == i or path.startswith(i):
                return False
            if i[-1] == '*' and path.startswith(i[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return value of the Authorization Header """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """ return the current authenticated user """
        return None
