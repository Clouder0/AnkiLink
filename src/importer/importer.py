import datetime
from . import config
from . import notetype_loader as loader


def HandleNote(text: str, noteList: list) -> str:
    lines = text.splitlines(keepends=False)
    if len(lines) == 0:
        return "Blank text, skipping.\n"
    try:
        ret = "Recognized as {}\n"
        for now in loader.discovered_notetypes:
            if now.check(lines):
                ret = ret.format(now.__name__.split(".")[-1])
                noteList.append(now.get(text, tags=config.tags))
                return ret
        return "Unmatching any format.\n"
    except Exception as e:
        return """Error! Exception:{}
details:
    class:{}
    cause:{}
    context:{}\n""".format(e, e.__class__, e.__cause__, e.__context__)


def HandlePost(text: str):
    notes = text.split("\n\n")
    f = open("log.txt", "a+", encoding="utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    noteList = []
    for note in notes:
        f.write(HandleNote(note, noteList))
    f.close()
    return noteList
