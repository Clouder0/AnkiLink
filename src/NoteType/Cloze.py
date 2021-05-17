from note import Note
from lib.formatHelper import formatText

class ClozeNote(Note):
    def __init__(self, text, _deckName="Export", _modelName="CCloze",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Text": text}, _options, _tags)

def check(text):
    return "**" in text.splitlines()[0]

def get(text):
    sub = text.split("**")
    output = ""
    if len(sub) == 0: raise Exception("Invalid Cloze format, skipping.")
    # odd indexes are clozes
    for i in range(0,len(sub)):
        if(i % 2 == 1):
            output = output + '{{c' + str(((i + 1) // 2)) + '::' + sub[i] + '}}'
        else: output = output + sub[i]
    output = formatText(output)
    return ClozeNote(output)