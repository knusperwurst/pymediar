import re

PATTERN = re.compile("^.*\\.(mov|mkv|avi|mp4)$")


def check(file):
    if PATTERN.match(file):
        print(file)
