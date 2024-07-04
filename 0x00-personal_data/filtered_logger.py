#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        match = re.search(fr"{field}=([\w\d/]+);", message)
        if match:
            message = re.sub(match.group(1), redaction, message)
    return message
