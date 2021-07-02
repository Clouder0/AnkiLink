import sys
import os
from AnkiIn.helper.genankiHelper import get_deck, export_deck
from AnkiIn.helper.ankiConnectHelper import add_notes, check_online
from AnkiIn.helper.formatHelper import get_title, remove_suffix
from AnkiIn import config
from AnkiIn.parser import markdown as markdown_parser
import config_parser


def execute_from_commandline():
    config_parser.parse()
    print("Starting...")
    noteLists = []
    if config.output is False and not check_online():  # import into Anki
        sys.exit()
    titles = []
    for file in config.file_list:
        print("file: " + file)
        f = open(file, "r", encoding="utf-8")
        content = f.read()
        titles.append(get_title(content))
        noteList = markdown_parser.handle_post(content)
        f.close()
        noteLists += noteList
        print("Done.")
    if config.output is False:
        add_notes(noteLists, config.deck_name)
    else:
        if config.outputpath is None:
            config.outputpath = ""

            def getRaw(name: str) -> str:
                ret = os.path.basename(name)
                return ret[:ret.find(".")] if "." in ret else ret
            if len(config.file_list) > 1:
                for i, x in enumerate(config.file_list):
                    config.outputpath += (titles[i] if titles[i] is not None else getRaw(x)) + "_"
                config.outputpath = remove_suffix(config.outputpath, "_")
            else:
                config.outputpath = titles[0] if titles[0] is not None else getRaw(config.file_list[0])
            config.outputpath += ".apkg"
            print("No filename provided. Exporting to " + config.outputpath)
        export_deck(get_deck(config.deck_name, noteLists), config.outputpath)
    print("All done.")


if __name__ == "__main__":
    execute_from_commandline()
