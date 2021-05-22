import urllib.request
import json


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


def addNote(target, deck, options={"allowDuplicate": True}):
    invoke("addNote", note={
        "deckName": deck,
        "modelName": target.model.modelName,
        "fields": target.outputfields,
        "options": options,
        "tags": target.tags
    }
    )


def getModelNamesAndIds():
    return invoke("modelNamesAndIds")


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
