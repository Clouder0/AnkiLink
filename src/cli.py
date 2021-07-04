import sys
import os
from AnkiIn.helper.genankiHelper import export_notes
from AnkiIn.helper.ankiConnectHelper import add_notes, check_online
from AnkiIn.helper.formatHelper import get_title, remove_suffix
from AnkiIn import config
from AnkiIn.config import dict as conf
from AnkiIn.parser import markdown as markdown_parser
import config_parser
import config


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
    if not config.output:
        add_notes(noteLists)
    else:
        if config.output_path is None:
            config.output_path = ""

            def getRaw(name: str) -> str:
                ret = os.path.basename(name)
                return ret[:ret.find(".")] if "." in ret else ret

            if len(config.file_list) > 1:
                for i, x in enumerate(config.file_list):
                    config.output_path += (titles[i] if titles[i]
                                            is not None else getRaw(x)) + "_"
                config.output_path = remove_suffix(config.output_path, "_")
            else:
                config.output_path = titles[0] if titles[0] is not None else getRaw(
                    config.file_list[0])
            config.output_path += ".apkg"
            print("No filename provided. Exporting to " + config.output_path)
        export_notes(noteLists, config.output_path)
    print("All done.")


if __name__ == "__main__":
    execute_from_commandline()
