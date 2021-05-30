pyinstaller cli.py\
  --nowindow \
  --name AnkiLink\
  --hidden-import=importer.notetypes\
  --paths="./importer/"\
  --paths="./importer/notetypes/"\
  --paths="./"