import os
from enum import Enum
import colorama

LogLevel = Enum("LogLevel", ["DEBUG", "WARNING", "ERROR"])

class Logger:
    def __init__(self):
        self.debug = os.getenv("DEBUG")

    def log(self, level: LogLevel, message: str):
        if not self.debug: return

