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
    return re.sub(
        fr"({'|'.join(fields)})=[^{separator}]*",
        lambda m: f"{m.group().split('=')[0]}={redaction}",
        message
    )
