import sys
import os
from importer.helper.genankiHelper import getDeck, exportDeck
from importer.helper.ankiConnectHelper import addNotes, checkOnline
from importer.helper.formatHelper import getTitle, removeSuffix
from importer import *


def execute_from_commandline():
    print("Starting...")
    noteLists = []
    if config.output is False and not checkOnline():  # import into Anki
        print("ERROR: failed to connect with Anki Connect.")
        sys.exit()
    titles = []
    for file in config.file_list:
        print("file: " + file)
        f = open(file, "r", encoding="utf-8")
        content = f.read()
        titles.append(getTitle(content))
        noteList = importer.HandlePost(content)
        f.close()
        noteLists += noteList
        print("Done.")
    if config.output is False:
        addNotes(noteLists, config.deck_name)
    else:
        if config.outputpath is None:
            config.outputpath = ""

            def getRaw(name: str) -> str:
                ret = os.path.basename(name)
                return ret[:ret.find(".")] if "." in ret else ret
            if len(config.file_list) > 1:
                for i, x in enumerate(config.file_list):
                    config.outputpath += (titles[i] if titles[i] is not None else getRaw(x)) + "_"
                config.outputpath = removeSuffix(config.outputpath, "_")
            else:
                config.outputpath = titles[0] if titles[0] is not None else getRaw(config.file_list[0])
            config.outputpath += ".apkg"
            print("No filename provided. Exporting to " + config.outputpath)
        exportDeck(getDeck(config.deck_name, noteLists), config.outputpath)
    print("All done.")


if __name__ == "__main__":
    execute_from_commandline()
