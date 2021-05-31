from .Cloze import get as cget


priority = 15


def check(lines):
    if len(lines) < 3:
        return False
    return "|" in lines[0] and "|" in lines[1] and "-" in lines[1] and "|" in lines[2]


def get(text, tags):
    return cget(text, tags)
