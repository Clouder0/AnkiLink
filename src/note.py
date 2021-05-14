import helper

class Note:
    def __init__(self, _deckName="Export", _modelName="CBasic", _fields={}, _options={"allowDuplicate": True}, _tags=("#Export")):
        self.deckName = _deckName
        self.modelName = _modelName
        self.fields = _fields
        self.options = _options
        self.tags = _tags

class QANote(Note):
    def __init__(self, front, back, _deckName="Export", _modelName="CBasic",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Front": front, "Back": back}, _options, _tags)

class ClozeNote(Note):
    def __init__(self, text, _deckName="Export", _modelName="CCloze",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Text": text}, _options, _tags)

class ChoicesNote(Note):
    def __init__(self, question, options, answer, remark, _deckName="Export", _modelName="CChoices",  _options={"allowDuplicate": True}, _tags=("#Export",)):
        super().__init__(_deckName, _modelName, {"Question": question, "Options": options, "Answer": answer, "Remark": remark}, _options, _tags)

def addNote(target):
    return helper.invoke('addNote', note = {
            "deckName": target.deckName,
            "modelName": target.modelName,
            "fields": target.fields,
            "options": target.options,
            "tags": target.tags
        }
    )
