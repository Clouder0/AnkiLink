import os
import sys
import datetime
import markdown2
from NoteType import QA, Choices, Cloze

 
def HandleNote(text):
    if type(text) != str: return "not string type!\n"
    lines = text.splitlines(keepends = False)
    if len(lines) == 0: return "Blank text, skipping.\n"
    try:
        ret = "Recognized as {}, invoke successfully with return code {}\n"
        if Cloze.check(text):
            return ret.format("Cloze",Cloze.get(text).add())
        elif Choices.check(text):
            return ret.format("Choices",Choices.get(text).add())
        elif QA.check(text):
            return ret.format("QA",QA.get(text).add())
        return "Unmatching any format.\n"
    except Exception as e:
        return "Error! Exception:{}\n".format(e)

def HandlePost(text):
    if type(text) != str: raise Exception("A string is required!")
    notes = text.split("\n\n")
    f = open("log.txt","a+",encoding = "utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    for note in notes:
        f.write(HandleNote(note))
    f.close()

def check_library(lib_name, auto_install = True):
    if lib_name not in os.popen('python -m pip list').read():
        print('The required module \'{}\' has not installed yet.'.format(lib_name))
        if auto_install:
            print('It is being installed automatically:')
            os.system('python -m pip install {}'.format(lib_name))
    exec('import {}'.format(lib_name))

if len(sys.argv) < 2: 
    print("Please provide a param: python AnkiImporter.py filename.md")
    sys.exit()
path = sys.argv[1]
print("path: " + path)
check_library('markdown2')
f = open(path,"r",encoding = "utf-8")
HandlePost(f.read())
f.close()
print("Done.")
