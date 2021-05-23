import urllib.request
import json


def checkOnline():
    try:
        getDeckNames()
    except Exception:
        return False
    return True


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(urllib.request.urlopen(
        urllib.request.Request("http://localhost:8765", requestJson)))
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


def addNote(target, deck, options={"allowDuplicate": True}, retry=True):
    try:
        return invoke("addNote", note={
            "deckName": deck,
            "modelName": target.model.modelName,
            "fields": target.outputfields,
            "options": options,
            "tags": target.tags
        }
        )
    except Exception as e:
        if len(e.args) == 0:
            return e
        if "model" in e.args[0] and target.model.modelName not in getModelNamesAndIds().keys():
            createModel(target.model)
        elif "deck was not found" in e.args[0] and deck not in getDeckNames():
            createDeck(deck)
        if retry:
            return addNote(target, deck, options, False)


def createDeck(deckName):
    return invoke("createDeck", deck=deckName)


def getModelNamesAndIds():
    return invoke("modelNamesAndIds")


def getDeckNames():
    return invoke("deckNames")


def createModel(model):
    return invoke("createModel",
                  modelName=model.modelName,
                  inOrderFields=model.fields,
                  css=model.css,
                  isCloze=model.isCloze,
                  cardTemplates=model.templates
                  )


def addNotes(notes, deck, options={"allowDuplicate": True}):
    for x in notes:
        addNote(x, deck, options)
