import sys
import os
import datetime

# dirty hand tweak for proper importing...
sys.path.append(".")
sys.path.append("./src")
sys.path.append("..")

from NoteType import Cloze, Choices, ListCloze, TableCloze, QA
from helper.genankiHelper import getDeck, exportDeck
from helper.ankiConnectHelper import addNotes, checkOnline
from helper.formatHelper import getTitle, removeSuffix
import config


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


def main():
    print("Starting...")
    noteLists = []
    if config.output is False and not checkOnline():  # import into Anki
        print("ERROR: failed to connect with Anki Connect.")
        sys.exit()
    titles = []
    for file in config.file_list:
        print("file: " + file)
        f = open(file, "r", encoding="utf-8")
        content = f.read()
        titles.append(getTitle(content))
        noteList = HandlePost(content)
        f.close()
        noteLists += noteList
        print("Done.")
    if config.output is False:
        addNotes(noteLists, config.deck_name)
    else:
        if config.outputpath is None:
            config.outputpath = ""

            def getRaw(name: str) -> str:
                ret = os.path.basename(name)
                return ret[:ret.find(".")] if "." in ret else ret
            if len(config.file_list) > 1:
                for i, x in enumerate(config.file_list):
                    config.outputpath += (titles[i] if titles[i] is not None else getRaw(x)) + "_"
                config.outputpath = removeSuffix(config.outputpath, "_")
            else:
                config.outputpath = titles[0] if titles[0] is not None else getRaw(config.file_list[0])
            config.outputpath += ".apkg"
            print("No filename provided. Exporting to " + config.outputpath)
        exportDeck(getDeck(config.deck_name, noteLists), config.outputpath)
    print("All done.")


if __name__ == "__main__":
    main()
