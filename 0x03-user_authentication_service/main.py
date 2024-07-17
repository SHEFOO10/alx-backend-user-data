#!/usr/bin/env python3
"""
20. End-to-end integration test
"""
from requests import get, post, put, delete
import re
import json


def register_user(email: str, password: str) -> None:
    """ test register user """
    response = post('http://localhost:5000/users', {
        'email': email,
        'password': password
    })
    assert(response.json() == {"email": email, "message": "user created"})
    response = post('http://localhost:5000/users', {
        'email': email,
        'password': password
    })
    assert(response.json() == {"message": "email already registered"})


def log_in_wrong_password(email: str, password: str) -> None:
    """ log_in with a wrong password """
    response = post('http://localhost:5000/sessions', {
        "email": email,
        "password": password
    })
    assert(response.status_code == 401)


def profile_unlogged():
    """ get profile without sending session_id """
    headers = {
        'session_id': 'not exists'
    }
    response = get('http://localhost:5000/profile', headers=headers)
    assert(response.status_code == 403)


def log_in(email: str, password: str) -> str:
    """ test login operation """
    response = post('http://localhost:5000/sessions', {
        'email': email,
        'password': password
    })
    assert(response.json() == {'email': 'guillaume@holberton.io',
                               'message': 'logged in'})
    return response.cookies.get('session_id')


def profile_logged(session_id: str) -> None:
    """ test profile response with the given session_id """
    response = get('http://localhost:5000/profile', cookies={
        'session_id': session_id
    })
    assert(response.json() == {"email": EMAIL})


def log_out(session_id: str) -> None:
    """ test logout endpoint """
    response = delete('http://localhost:5000/sessions', cookies={
        "session_id": session_id
    })
    assert(response.history[0].status_code == 302)
    response = delete('http://localhost:5000/sessions', cookies={
        'session_id': 'nope'
    })
    assert(response.status_code == 403)


def reset_password_token(email: str) -> str:
    """ test request token endpoint """
    response = post('http://localhost:5000/reset_password', {
        'email': email
    })
    pattern = {
        'email': email,
        'reset_token': r"[a-z0-9\-]+"
    }
    validate_email = isinstance(re.match(pattern['email'],
                                         response.json()['email']), re.Match)
    validate_resetToken = isinstance(
        re.match(pattern['reset_token'],
                 response.json()['reset_token']),
        re.Match)
    assert(validate_email == validate_resetToken)
    return response.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update user password with the new password by the reset token """
    response = put('http://localhost:5000/reset_password', {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    })
    assert(response.json() == {"email": email, "message": "Password updated"})


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
