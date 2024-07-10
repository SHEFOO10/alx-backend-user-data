#!/usr/bin/env python3
""" Session based Authentication """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create and Returns new session id """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = uuid4()
        SessionAuth.user_id_by_session_id.update({session_id: user_id})
        return session_id