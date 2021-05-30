import genanki
import hashlib


def getNote(mynote):
    return genanki.Note(model=getModel(mynote.model), fields=list(mynote.outputfields.values()), tags=mynote.tags)


def getModel(mymodel):
    return genanki.Model(
        model_id=mymodel.modelId,
        name="G" + mymodel.modelName,  # avoid duplicating
        fields=list([{"name": x} for x in mymodel.fields]),
        templates=[{"name": x["Name"], "qfmt":x["Front"], "afmt":x["Back"]}
                   for x in mymodel.templates],
        model_type=mymodel.isCloze,
        css=mymodel.css
    )


def getIdfromStr(text):
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10


def getDeck(deckname, notes):
    deck = genanki.Deck(getIdfromStr(deckname), deckname)
    for x in notes:
        deck.add_note(getNote(x))
    return deck


def exportDeck(deck, path):
    genanki.Package(deck).write_to_file(path)
