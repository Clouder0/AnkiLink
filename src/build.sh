pyinstaller cli.py\
  --nowindow\
  --onefile\
  --name AnkiLink\
  --hidden-import=importer.notetypes\
  --paths="./importer/"\
  --paths="./importer/notetypes/"\
  --paths="./"