import re

PATTERN = re.compile("^.*\\.(mov|mkv|avi|mp4)$")


def check(file):
    return PATTERN.match(file)
