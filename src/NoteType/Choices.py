from note import Note
from lib.formatHelper import formatText,list2str

class ChoicesNote(Note):
    def __init__(self, question, options, answer, remark, _deckName="Export", _modelName="CChoices",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Question": question, "Options": options, "Answer": answer, "Remark": remark}, _options, _tags)

def check(text):
    lines = text.splitlines()
    return len(lines) >= 3 and lines[1][0] == 'A'

def get(text):
    lines = text.split("\n")
    question = formatText(lines[0])
    options = list()
    remark = ""
    i = 1
    while i < len(lines):
        if lines[i][0] != chr(65 + i - 1): break
        options.append(lines[i].strip())
        i += 1
    if len(options) <= 1: raise Exception("Error! Choices with only one option.")
    options = options[0] + list2str(options[1:])
    options = formatText(options)
    if i < len(lines): 
        answer = list2str([x for x in lines[i] if ord(x) >= 65 and ord(x) <= 90],'','')
        i += 1
    else: raise Exception("Error! Choices with no answer.")
    if i < len(lines): remark = formatText(list2str(lines[i:]))
    return ChoicesNote(question, options, answer, remark)