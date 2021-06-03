import sys
import os
import pkgutil
import importlib
from importer.notetypes import Choices, Cloze, ListCloze, QA, TableCloze


discovered_notetypes = [Choices, Cloze, ListCloze, QA, TableCloze]
sys.path.append("." + os.sep + "notetypes" + os.sep)
sys.path.append("." + os.sep + "importer" + os.sep + "notetypes" + os.sep)
discovered_notetypes.extend(
    importlib.import_module(name) for finder, name, ispkg in pkgutil.iter_modules() if name.startswith("notetype_"))
discovered_notetypes.sort(key=lambda x: x.priority, reverse=True)
