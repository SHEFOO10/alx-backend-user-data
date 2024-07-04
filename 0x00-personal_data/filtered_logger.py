#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re
import logging
import os
import mysql.connector


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


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """ Create a new logger """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    streamHanlder = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    streamHanlder.setFormatter(formatter)
    logger.addHandler(streamHanlder)
    logger.propagate = False
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns Connector to the database """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.environ.get("PERSONAL_DATA_DB_NAME")
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=dbname
        )
    return connection
