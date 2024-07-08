#!/usr/bin/env python3
""" Basic Auth """
from api.v1.auth.auth import Auth


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
