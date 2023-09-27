from .objects import *

# nice function lol java>python switch
def get_line_type(line: str):
    if "[DATA]" in line:
        return LineType.DATA
    elif "[ATTEMPT]" in line:
        return LineType.ATTEMPT
    elif "[WARNING]" in line:
        return LineType.WARNING
    elif "[VERBOSE]" in line:
        return LineType.VERBOSE
    elif "[INFO]" in line:
        return LineType.INFO
    elif "password" in line and "[ATTEMPT]" not in line and line.startswith("["):
        return LineType.FOUND
    elif "finished" in line or "completed" in line:
        return LineType.FINISHED
    elif "[STATUS]" in line:
        return LineType.STATUS
    else:
        return LineType.UNDEFINED

def parse(line: str) -> Line:
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
    return FinishedLine(line)

def parse_found(line: str):
    split_line = line.strip().split(" ")
    target = split_line[2]
    username = split_line[6]
    password = split_line[10]
    return FoundLine(target, username, password, line)

def parse_data(line: str):
    return DataLine(line.replace("[DATA] ", ""), line)

def parse_attempt(line: str):
    split_line = line.split(" ")
    target = split_line[2]
    username = split_line[5][1:-1]
    password = split_line[8][1:-1]
    number = split_line[10]
    return AttemptLine(target, username, password, number, line)

def parse_status(line: str):
    return StatusLine(line.replace("[STATUS] ", ""), line)

def parse_warning(line: str):
    return WarningLine(line.replace("[WARNING] ", ""), line)

def parse_verbose(line: str):
    return VerboseLine(line.replace("[VERBOSE] ", ""), line)

def parse_info(line: str):
    return InfoLine(line.replace("[INFO] ", ""), line)

def parse_undefined(line: str):
    return UndefinedLine(line, line)