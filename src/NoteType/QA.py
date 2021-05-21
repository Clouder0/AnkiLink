from note import Note
from lib.formatHelper import list2str

class QANote(Note):
    def __init__(self, front, back, _deckName="Export", _modelName="CBasic",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Front": front, "Back": back}, _options, _tags)

def check(lines):
    return len(lines) >= 2

def get(text, deckName, tags):
    if check(text) == False:
        raise Exception("Not QA format.")
    lines = text.splitlines()
    front = lines[0]
    back = list2str(lines[1:], '', '\n')
    if front == "": raise Exception("Blank front text, skipping.")
    if back == "": raise Exception("Blank back text, skipping.")
    return QANote(front, back, _deckName = deckName, _tags = tags)
