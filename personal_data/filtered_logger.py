#!/usr/bin/env python3
"""
A function called filter_datum that returns the log message obfuscated:
"""
import re
from typing import List
import logging
from os import getenv
import mysql.connector


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
