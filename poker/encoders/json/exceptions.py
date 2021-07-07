"""Exceptions for mismatched object and JSON encoder"""


class UnsupportedObjectToJSON(Exception):
    """JSON encoder is called on an unexpected type"""

    def __init__(self, msg):
        Exception.__init__()
        self.msg = msg
