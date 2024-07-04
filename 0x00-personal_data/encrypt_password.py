#!/usr/bin/env python3
""" 5. Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash password to make secure if data breached """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: str, password: str) -> bool:
    """ validate that the provided password matches the hashed password. """
    return bcrypt.checkpw(password.encode(), hashed_password)
