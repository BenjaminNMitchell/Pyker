"""Exceptions for mismatched object and JSON encoder"""


class UnsupportedObjectToJSON(Exception, object):
    """JSON encoder is called on an unexpected type"""

    def __init__(self, msg):
        self.msg = msg
