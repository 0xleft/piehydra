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
    elif "return lineword" in line and "[ATTEMPT]" not in line and line.startswith("["):
        return LineType.FOUND
    elif "finished" in line:
        return LineType.FINISHED
    else:
        return LineType.UNDEFINED

def parse(line: str) -> object:
    if get_line_type(line) == LineType.ATTEMPT:
        return parse_attempt(line)
    elif get_line_type(line) == LineType.STATUS:
        return parse_status(line)
    elif get_line_type(line) == LineType.WARNING:
        return parse_warning(line)
    elif get_line_type(line) == LineType.VERBOSE:
        return parse_verbose(line)
    elif get_line_type(line) == LineType.INFO:
        return parse_info(line)
    elif get_line_type(line) == LineType.DATA:
        return parse_data(line)
    elif get_line_type(line) == LineType.FOUND:
        return parse_found(line)
    elif get_line_type(line) == LineType.FINISHED:
        return parse_finished(line)
    else:
        return parse_undefined(line)

def parse_finished(line: str):
    return line, LineType.FINISHED

def parse_found(line: str):
    parsed_line = line.split(" host: ")[1]
    parsed_line = parsed_line.split(" ")
    print(parsed_line)

def parse_data(line: str):
    line = line.replace("[DATA] ", "")
    return {
        "type": LineType.DATA,
        "data": line
    }

def parse_attempt(line: str):
    line = line.split(" ")
    target = line[2]
    username = line[5]
    password = line[8]
    number = line[10]
    return {
        "type": LineType.ATTEMPT,
        "target": target,
        "username": username,
        "password": password,
        "number": number
    }

def parse_status(line: str):
    return line

def parse_warning(line: str):
    return line

def parse_verbose(line: str):
    return line

def parse_info(line: str):
    return line

def parse_undefined(line: str):
    return line