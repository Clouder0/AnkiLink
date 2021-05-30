import datetime
from .notetype import *
from . import config


def HandleNote(text: str, noteList: list):
    lines = text.splitlines(keepends=False)
    if len(lines) == 0:
        return "Blank text, skipping.\n"
    try:
        ret = "Recognized as {}\n"
        rec = False
        # TODO dynamic importing for add-ons
        if Cloze.check(lines):
            ret = ret.format("Cloze")
            noteList.append(Cloze.get(text, tags=config.tags))
        elif Choices.check(lines):
            ret = ret.format("Cloze")
            noteList.append(Choices.get(text, tags=config.tags))
        elif ListCloze.check(lines):
            ret = ret.format("List Cloze")
            noteList.append(ListCloze.get(text, tags=config.tags))
        elif TableCloze.check(lines):
            ret = ret.format("Table Cloze")
            noteList.append(TableCloze.get(text, tags=config.tags))
        elif QA.check(lines):
            ret = ret.format("QA")
            noteList.append(QA.get(text, tags=config.tags))
        else:
            return "Unmatching any format.\n"
        return ret
    except Exception as e:
        return """Error! Exception:{}
details:
    class:{}
    cause:{}
    context:{}\n""".format(e, e.__class__, e.__cause__, e.__context__)


def HandlePost(text):
    notes = text.split("\n\n")
    f = open("log.txt", "a+", encoding="utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    noteList = []
    for note in notes:
        f.write(HandleNote(note, noteList))
    f.close()
    return noteList
