import sys
import argparse

version_name = "2.2.0"
deck_name = "Export"
tags = []
file_list = []
output = False  # output to file
outputpath = ""

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
parser.add_argument("-d", "--deckname", metavar="deckname", nargs="?", default=deck_name,
                    help=help_info["deckname"])
parser.add_argument("-t", "--tags", metavar="tags", nargs="*", default=tags,
                    help=help_info["tags"])
parser.add_argument("-o", "--output", nargs="?", metavar="output", help=help_info["output"])


def parse():
    args = parser.parse_args()
    global deck_name, tags, file_list, output, outputpath
    deck_name = args.deckname
    tags = args.tags
    file_list = args.filename
    output = "-o" in sys.argv or "--output" in sys.argv
    outputpath = args.output
