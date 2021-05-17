import lib.ankiConnectHelper
class Note:
    def __init__(self, _deckName="Export", _modelName="CBasic", _fields={}, _options={"allowDuplicate": True}, _tags=("#Export")):
        self.deckName = _deckName
        self.modelName = _modelName
        self.fields = _fields
        self.options = _options
        self.tags = _tags

    def add(self):
        return lib.ankiConnectHelper.addNote(self)