import helper.ankiConnectHelper
from note import Note
from model import Model


def check(lines: list):
    return "**" in lines[0]


def get(text: str, tags: list) -> Note:
    sub = text.split("**")
    output = ""
    if len(sub) == 0:
        raise Exception("Invalid Cloze format, skipping.")
    # odd indexes are clozes
    for i, x in enumerate(sub):
        if(i % 2 == 1):
            output = output + \
                "{{c" + str(((i + 1) // 2)) + "::" + x + "}}"
        else:
            output = output + x
    return ClozeNote(output, _tags=tags)


CSS = """.card {
  font-family: arial;
  font-size: 20px;
  text-align: left;
  color: black;
  background-color: white;
}

.cloze {
 font-weight: bold;
 color: blue;
}
.nightMode .cloze {
 color: lightblue;
}
"""

MODELNAME = "DCloze"
MODELID = 1145141920

ClozeModel = Model(
    modelId=MODELID,
    modelName=MODELNAME,
    isCloze=1,
    fields=["Text", "Back Extra"],
    templates=[
        {
            "Name": "Cloze",
            "Front": "{{cloze:Text}}",
            "Back": "{{cloze:Text}}",
        }
    ],
    css=CSS
)


class ClozeNote(Note):
    def __init__(self, text, model=ClozeModel, _tags=("#Export",)):
        super().__init__(model, {"Text": text, "Back Extra": ""}, _tags)


def init():
    if MODELNAME not in helper.ankiConnectHelper.getModelNamesAndIds().keys():
        helper.ankiConnectHelper.createModel(ClozeModel)
