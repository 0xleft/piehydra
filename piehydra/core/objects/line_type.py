from enum import Enum

class LineType(Enum):
    ATTEMPT = 0
    STATUS = 1
    WARNING = 2
    VERBOSE = 3
    INFO = 4
    DATA = 5
    FOUND = 6
    UNDEFINED = 7
    FINISHED = 8