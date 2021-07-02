import sys
import argparse
from AnkiIn import config

version_name = "2.3.0"

help_info = {
    "filename": "Files to be converted. You can specify multi files.",
    "deckname": "Deck to put your notes on. (default \"Export\")",
    "tags": "Tags to append to your notes. (default [\"#Export\"])",
    "output": "The path to output the notes to a apkg file, directly to Anki if left blank."
}

parser = argparse.ArgumentParser(
    description="Anki Importer. A handy tool to import your plain text files into Anki.")
parser.add_argument("-v", "--version", action="version",
                    version="Anki Importer v{}".format(version_name))
parser.add_argument("filename", metavar="filename", nargs="+",
                    help=help_info["filename"])
parser.add_argument("-d", "--deckname", metavar="deckname", nargs="?", default=config.deck_name,
                    help=help_info["deckname"])
parser.add_argument("-t", "--tags", metavar="tags", nargs="*", default=config.tags,
                    help=help_info["tags"])
parser.add_argument("-o", "--output", nargs="?", metavar="output", help=help_info["output"])


def enable_log_file():
    config.log_config["handlers"]["log_file"] = {
        "level": "INFO",
        "formatter": "standard",
        "class": "logging.FileHandler",
        "filename": "log.txt",
        "mode": "a"
    }
    for x in config.log_config["loggers"].keys():
        config.log_config["loggers"][x]["handlers"].append("log_file")


def parse():
    args = parser.parse_args()
    global deck_name, tags, file_list, output, outputpath
    config.deck_name = args.deckname
    config.tags = args.tags
    config.file_list = args.filename
    config.output = "-o" in sys.argv or "--output" in sys.argv
    config.outputpath = args.output
    enable_log_file()
    config.complete_config()
