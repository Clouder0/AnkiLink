import argparse

version_name = "1.1.0"
deck_name = "Export"
tags = ["#Export"]
file_list = []
output = "" #output to file

help_info = {
"filename" : "Files to be converted. You can specify multi files.",
"deckname" : "Deck to put your notes on. (default \"Export\")",
"tags"     : "Tags to append to your notes. (default [\"#Export\"])",
"output"   : "The path to output the notes to a apkg file, directly to Anki if left blank."
}

parser = argparse.ArgumentParser(description = "Anki Importer. A handy tool to import your plain text files into Anki.")
parser.add_argument("-v", "--version", action = "version", version = "Anki Importer v{}".format(version_name))
parser.add_argument("filename", metavar = "filename", nargs = "+",
help = help_info["filename"])
parser.add_argument("-d", "--deckname", metavar = "deckname", nargs = "?", default = deck_name,
help = help_info["deckname"])
parser.add_argument("-t", "--tags", metavar = "tags", nargs = "+", default = tags,
help = help_info["tags"])
parser.add_argument("-o", "--output", metavar = "output", nargs = "?", default = output,
help = help_info["output"])

args      = parser.parse_args()
deck_name = args.deckname
tags      = args.tags
file_list = args.filename
output    = args.output