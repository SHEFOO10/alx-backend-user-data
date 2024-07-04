#!/usr/bin/env python3
""" 5. Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash password to make secure if data breached """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
