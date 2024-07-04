#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re
import logging
import sys


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
        return super().format(record)


def get_logger() -> logging.Logger:
    logger = logging.Logger('user_data', level=logging.INFO)
    streamHanlder = logging.StreamHandler(sys.stdout)
    streamHanlder.setFormatter(logging.Formatter(RedactingFormatter))
    logger.addHandler(streamHanlder)
    return logger


PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'ip')
