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

# nice function lol java>python switch
def get_line_type(line: str):
    if "[DATA]" in line:
        return LineType.DATA
    elif "[ATTEMPT]" in line:
        return LineType.ATTEMPT
    elif "[STATUS]" in line:
        return LineType.STATUS
    elif "[WARNING]" in line:
        return LineType.WARNING
    elif "[VERBOSE]" in line:
        return LineType.VERBOSE
    elif "[INFO]" in line:
        return LineType.INFO
    elif "password" in line and "[ATTEMPT]" not in line and line.startswith("["):
        return LineType.FOUND
    elif "finished" in line:
        return LineType.FINISHED
    else:
        return LineType.UNDEFINED

def parse(line: str):
    return line