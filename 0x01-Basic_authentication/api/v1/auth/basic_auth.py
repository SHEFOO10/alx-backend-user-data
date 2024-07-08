#!/usr/bin/env python3
""" Basic Auth """
from api.v1.auth.auth import Auth
from base64 import b64decode


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
