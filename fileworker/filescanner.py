import os
from fileworker import filechecker


class Scanner:
    filepaths = []

    def __init__(self, filepaths):
        self.filepaths = filepaths

    def scan(self):
        for path in self.filepaths:
            for _, dirs, files in os.walk(path):
                for file in files:
                    filechecker.check(file)
