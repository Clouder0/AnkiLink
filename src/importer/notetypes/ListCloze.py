from .Cloze import get as cget


priority = 10


def check(lines):
    return lines[0].startswith("- ")


def get(text, tags):
    return cget(text, tags)
