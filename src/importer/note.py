from .helper.formatHelper import formatText


class Note:
    def __init__(self, model, fields={}, tags=[]):
        self.model = model
        self.fields = fields
        self.outputfields = self.fields.copy()
        for x in self.outputfields.keys():
            self.outputfields[x] = formatText(self.outputfields[x])
        self.tags = tags

    def __getitem__(self, key):
        if key not in self.fields:
            raise KeyError
        return self.fields[key]

    def __setitem__(self, key, value):
        self.fields[key] = value
        self.outputfields[key] = formatText(value)
