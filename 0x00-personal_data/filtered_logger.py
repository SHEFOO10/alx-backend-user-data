#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initiate new RedactingFormatter Object """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ change the format of record """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
            )
        record.msg = re.sub(';', '; ', record.msg)
        return super().format(record)
