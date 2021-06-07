from ..helper.formatHelper import list2str
from ..note import Note
from ..model import Model


priority = 10


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


BACK = r"""{{FrontSide}}
<hr id=answer>
{{Back}}"""

CSS = r""".card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
ul {
display: inline-block;
text-align: left;
}
ol {
display: inline-block;
text-align: left;
}
"""

MODELNAME = "AnkiLink-Basic"
MODELID = 1145141921

_model = Model(
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
    def __init__(self, front, back, model=_model, _tags=("#Export",)):
        super().__init__(model, {"Front": front, "Back": back}, _tags)
