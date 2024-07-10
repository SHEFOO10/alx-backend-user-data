#!/usr/bin/env python3
""" Basic Auth """
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple
from models.user import User


class BasicAuth(Auth):
    """ Implement Basic Auth """
    def extract_base64_authorization_header(
          self,
          authorization_header: str
          ) -> str:
        """ Extract base64 from Authorization Header """
        if (
            authorization_header is None
            or type(authorization_header) is not str
            or not authorization_header.startswith("Basic ")
        ):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
         self,
         base64_authorization_header: str
         ) -> str:
        """Decode base64 part from the Authorization Header """
        if (
            base64_authorization_header is None
            or type(base64_authorization_header) is not str
        ):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except (Exception):
            return None

    def extract_user_credentials(
         self,
         decoded_base64_authorization_header: str
         ) -> Tuple[str, str]:
        """
        returns the user email and password from the Base64 decoded value.
        """
        if (
            decoded_base64_authorization_header is None
            or type(decoded_base64_authorization_header) is not str
            or not decoded_base64_authorization_header.count(':')
        ):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
          self,
          user_email: str,
          user_pwd: str
          ) -> User:
        """
        returns the User instance based on his email and password.
        """
        from models.base import DATA
        if (
            user_email is None or type(user_email) is not str
            or
            user_pwd is None or type(user_pwd) is not str
            or
            len(DATA) == 0
            or
            len(User.search({'email': user_email})) == 0
        ):
            return None
        user = User.search({
            'email': user_email
        })[0]
        return user if user.is_valid_password(user_pwd) else None

    def current_user(self, request=None) -> User:
        """ Get the current user """
        AUTHORIZATION = self.authorization_header(request)
        base64str = self.extract_base64_authorization_header(AUTHORIZATION)
        decodedBase64 = self.decode_base64_authorization_header(base64str)
        credentials = self.extract_user_credentials(decodedBase64)
        user = self.user_object_from_credentials(*credentials)
        return user
