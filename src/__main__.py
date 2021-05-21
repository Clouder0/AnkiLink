import sys,datetime

#dirty hand tweak for proper importing...
sys.path.append(".")
sys.path.append("./src")
sys.path.append("..")

import config
from NoteType import *
from lib.ankiConnectHelper import addNote
 
def HandleNote(text):
    if type(text) != str: return "not string type!\n"
    lines = text.splitlines(keepends = False)
    if len(lines) == 0: return "Blank text, skipping.\n"
    try:
        ret = "Recognized as {}, invoke successfully with return code {}\n"
        #TODO dynamic importing for add-ons
        if Cloze.check(lines):
            return ret.format("Cloze", addNote(Cloze.get(text,
                   deckName=config.deck_name, tags=config.tags)))
        elif Choices.check(lines):
            return ret.format("Choices", addNote(Choices.get(text,
                   deckName=config.deck_name, tags=config.tags)))
        elif ListCloze.check(lines):
            return ret.format("List Cloze", addNote(ListCloze.get(text,
                   deckName=config.deck_name, tags=config.tags)))
        elif TableCloze.check(lines):
            return ret.format("Table Cloze", addNote(TableCloze.get(text,
                   deckName=config.deck_name, tags=config.tags)))
        elif QA.check(lines):
            return ret.format("QA", addNote(QA.get(text,
                   deckName=config.deck_name, tags=config.tags)))
        return "Unmatching any format.\n"
    except Exception as e:
        return """Error! Exception:{}
details: 
    class:{}
    cause:{}
    context:{}\n""".format(e, e.__class__,e.__cause__,e.__context__)

def HandlePost(text):
    if type(text) != str: raise Exception("A string is required!")
    notes = text.split("\n\n")
    f = open("log.txt", "a+", encoding="utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    for note in notes:
        f.write(HandleNote(note))
    f.close()

def main():
    #hack for proper importing
    if len(sys.argv) < 2: 
        print("Please provide a param: python AnkiImporter.py filename.md")
        sys.exit()
    path = sys.argv[1]
    print("path: " + path)
    f = open(path,"r",encoding = "utf-8")
    HandlePost(f.read())
    f.close()
    print("Done.")

if __name__ == "__main__":
    main()