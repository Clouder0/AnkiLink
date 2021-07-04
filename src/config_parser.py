import argparse
import os.path
from AnkiIn.config import dict as conf
from AnkiIn import config as AnkiIn_config
import config
import toml

version_name = "2.3.1"

help_info = {
    "filename": "Files to be converted. You can specify multi files.",
    "deckname": "Deck to put your notes on. (default \"Export\")",
    "tags": "Tags to append to your notes. (default [\"#Export\"])",
    "output": "The path to output the notes to a apkg file, infer the filename if left blank.",
    "debug": "Enable this to be in debug mode.",
    "config": "The path of the config file"
}

parser = argparse.ArgumentParser(
    description="Anki Importer. A handy tool to import your plain text files into Anki.")
parser.add_argument("-v", "--version", action="version",
                    version="Anki Importer v{}".format(version_name))
parser.add_argument("filename", metavar="filename", nargs="+",
                    help=help_info["filename"])
parser.add_argument("-d", "--deckname", metavar="deckname", nargs="+", default=conf["deck_name"],
                    help=help_info["deckname"])
parser.add_argument("-c", "--config", metavar="config", nargs="+", default=config.config_path,
                    help=help_info["config"])
parser.add_argument("-t", "--tags", metavar="tags", nargs="*", default=conf["tags"],
                    help=help_info["tags"])
parser.add_argument("--debug", action="store_true", default=config.log_debug,
                    help=help_info["debug"])
parser.add_argument("-o", "--output", nargs="?", const="yes",
                    default="no", metavar="output", help=help_info["output"])


def enable_log_file():
    conf["log_config"]["handlers"]["log_file"] = {
        "level": "DEBUG" if config.log_debug else "INFO",
        "formatter": "standard",
        "class": "logging.FileHandler",
        "filename": "log.txt",
        "mode": "a"
    }
    for x in conf["log_config"]["loggers"].keys():
        conf["log_config"]["loggers"][x]["handlers"].append("log_file")


def parse():
    args = parser.parse_args()
    conf["deck_name"] = args.deckname
    conf["tags"] = args.tags
    config.file_list = args.filename
    config.output = args.output != "no"
    config.output_path = None if args.output and args.output == "yes" else args.output
    config.log_debug = args.debug
    config.config_path = args.config
    enable_log_file()
    load_config_file()
    AnkiIn_config.update_config()


def load_config_file():
    if os.path.isfile(config.config_path):
        AnkiIn_config.execute_config(toml.load(config.config_path))
    else:
        print("Warning: Config File {} doesn't exist!".format(config.config_path))
