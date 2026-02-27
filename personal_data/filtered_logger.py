#!/usr/bin/env python3
"""
Module for filtering sensitive data from log messages.
"""
import re
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import List, Tuple


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of strings representing all fields to obfuscate
        redaction: String representing by what the field will be obfuscated
        message: String representing the log line
        separator: Character separating all fields in the log line

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = f"({'|'.join(fields)})=([^{re.escape(separator)}]*)"
    return re.sub(pattern, f"\\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields: List of strings representing fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record with redacted fields.

        Args:
            record: The log record to format

        Returns:
            The formatted log message with redacted fields
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data.

    Returns:
        A configured logging.Logger object named "user_data"
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Connects to a secure database using credentials from environment variables.

    Returns:
        A MySQLConnection object connected to the database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    Main function that retrieves and displays all users from the database
    with PII fields filtered.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, email, phone, ssn, password, ip, "
                   "last_login, user_agent FROM users;")

    fields = ['name', 'email', 'phone', 'ssn', 'password',
              'ip', 'last_login', 'user_agent']

    for row in cursor:
        message = '; '.join(f"{fields[i]}={row[i]}"
                            for i in range(len(fields)))
        message += ';'
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
