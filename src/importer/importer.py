import datetime
from . import config
from . import notetype_loader as loader
from .helper.formatHelper import list2str


def HandleNote(text: str, noteList: list) -> str:
    ERRORMSG = """Error! Exception:{}
details:
    class:{}
    cause:{}
    context:{}\n"""
    lines = text.splitlines(keepends=False)
    if len(lines) == 0:
        return "Blank text, skipping.\n"
    ret = "Recognized as {}\n"
    for now in loader.discovered_notetypes:
        try:
            if now.check(lines):
                ret = ret.format(now.__name__.split(".")[-1])
                noteList.append(now.get(text, tags=config.tags))
                yield ret
                return
        except Exception as e:
            yield ERRORMSG.format(e, e.__class__, e.__cause__, e.__context__)
    yield "Unmatching any format.\n"
    return


def HandlePost(text: str):
    notes = text.split("\n\n")
    f = open("log.txt", "a+", encoding="utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    noteList = []
    for note in notes:
        f.write(list2str(HandleNote(note, noteList)))
    f.close()
    return noteList
