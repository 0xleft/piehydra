from .line_type import LineType

class Line:
    def __init__(self, type: LineType, full_content: str) -> None:
        self.type = type
        self.full_content = full_content


class FoundLine(Line):
    def __init__(self, target: str, username: str, password: str, full_content: str) -> None:
        super().__init__(LineType.FOUND, full_content)
        self.target = target
        self.username = username
        self.password = password

class AttemptLine(Line):
    def __init__(self, target: str, username: str, password: str, number: int, full_content: str) -> None:
        super().__init__(LineType.ATTEMPT, full_content)
        self.target = target
        self.username = username
        self.password = password
        self.number = number

class DataLine(Line):
    def __init__(self, data: str, full_content: str) -> None:
        super().__init__(LineType.DATA, full_content)
        self.data = data

class StatusLine(Line):
    def __init__(self, status: str, full_content: str) -> None:
        super().__init__(LineType.STATUS, full_content)
        self.status = status

class WarningLine(Line):
    def __init__(self, warning: str, full_content: str) -> None:
        super().__init__(LineType.WARNING, full_content)
        self.warning = warning

class VerboseLine(Line):
    def __init__(self, verbose: str, full_content: str) -> None:
        super().__init__(LineType.VERBOSE, full_content)
        self.verbose = verbose

class InfoLine(Line):
    def __init__(self, info: str, full_content: str) -> None:
        super().__init__(LineType.INFO, full_content)
        self.info = info

class UndefinedLine(Line):
    def __init__(self, line: str, full_content: str) -> None:
        super().__init__(LineType.UNDEFINED, full_content)
        self.line = line

class FinishedLine(Line):
    def __init__(self, full_content: str) -> None:
        super().__init__(LineType.FINISHED, full_content)