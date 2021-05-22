from helper.formatHelper import list2str
from note import Note
from model import Model
import helper.ankiConnectHelper


def check(lines):
    return len(lines) >= 2


def get(text, tags):
    if not check(text):
        raise Exception("Not QA format.")
    lines = text.splitlines()
    front = lines[0]
    back = list2str(lines[1:], '', '\n')
    if front == "":
        raise Exception("Blank front text, skipping.")
    if back == "":
        raise Exception("Blank back text, skipping.")
    return QANote(front, back, _tags=tags)


BACK = """{{FrontSide}}

<hr id=answer>

{{Back}}"""

CSS = """.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
"""

MODELNAME = "DBasic"
MODELID = 1145141921

QAModel = Model(
    modelId=MODELID,
    modelName=MODELNAME,
    fields=["Front", "Back"],
    templates=[
        {
            'Name': 'Card 1',
            'Front': '{{Front}}',
            'Back': BACK
        }
    ],
    css=CSS
)


class QANote(Note):
    def __init__(self, front, back, model=QAModel, _tags=("#Export",)):
        super().__init__(model, {"Front": front, "Back": back}, _tags)


def init():
    if MODELNAME not in helper.ankiConnectHelper.getModelNamesAndIds().keys():
        helper.ankiConnectHelper.createModel(QAModel)
