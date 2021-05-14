import sys
import datetime
from note import addNote,QANote,ClozeNote,ChoicesNote

def replaceBrackets(text, spliter,left,right):
    sub = text.split(spliter)
    output = ""
    for i in range(0, len(sub)):
        if(i % 2 == 1):
            output = output + left + sub[i] + right
        else: output = output + sub[i]
    return output
    
def formatText(text):
    text = replaceBrackets(text,"**","<b>","</b>")
    text = list2str([x.strip() for x in text.splitlines()], '', '\n',False)
    print(text)
    return text

def HandleQA(text):
    text = formatText(text)
    lines = text.splitlines(keepends = False)
    front = lines[0]
    back = list2str(lines[1:])
    if front == "": return "Blank front text, skipping.\n"
    if back == "": return "Blank back text, skipping.\n"
    return "Invoke successfully, return code:{}\n".format(addNote(QANote(front,back)))

def list2str(list,l = '<div>', r = '</div>',removeFirst = True):
    output = ""
    first = True
    for x in list:
        if first == True and removeFirst == True:
            output = x
            first = False
        else:
            output = output + l + x + r
    return output

def HandleChoices(text):
    text = formatText(text)
    lines = text.split("\n")
    question = lines[0]
    options = list()
    remark = ""
    i = 1
    while i < len(lines):
        if lines[i][0] != chr(65 + i - 1): break
        options.append(lines[i].strip())
        i += 1
    options = list2str(options)
    if i < len(lines): 
        answer = list2str([x for x in lines[i] if ord(x) >= 65 and ord(x) <= 90],'','')
        i += 1
    else: return "Error! Choices with no answer.\n"
    if i < len(lines): remark = list2str(lines[i:])
    return "Invoke successfully, return code:{}\n".format(addNote(ChoicesNote(question,options,answer,remark)))

def HandleCloze(text):
    sub = text.split("**")
    output = ""
    if len(sub) == 0: return "Invalid Cloze format, skipping.\n"
    # odd indexes are clozes
    for i in range(0,len(sub)):
        if(i % 2 == 1):
            output = output + '{{c' + str(((i + 1) // 2)) + '::' + sub[i] + '}}'
        else: output = output + sub[i]
    output = output.replace('\n','<br>')
    return "Invoke successfully, return code:{}\n".format(addNote(ClozeNote(output)))

 
def HandleNote(text):
    if type(text) != str: return "not string type!\n"
    if "  - " in text: return "found Outline Structure, skipping.\n"
    if "|" in text: return "found Table Structure, skipping.\n"
    text = replaceBrackets(text,'$','\\(','\\)')
    lines = text.splitlines(keepends = False)
    if len(lines) == 0: return "Blank text, skipping.\n"
    if "**" in lines[0]:  
        HandleCloze(text)
    elif len(lines) >= 3 and len(lines[1]) >= 2 and lines[1][:2] == "A ":
        return HandleChoices(text)
    elif len(lines) >= 2:
        return HandleQA(text)
    return "Unmathcing any format.\n"

def HandlePost(text):
    if type(text) != str: raise Exception("A string is required!")
    notes = text.split("\n\n")
    f = open("log.txt","a+",encoding = "utf-8")
    f.write("\n" + datetime.datetime.now().strftime("%c") + "\n")
    for note in notes:
        f.write(HandleNote(note))
    f.close()

if len(sys.argv) < 2: 
    print("Please provide a param: python AnkiImporter.py filename.md")
    exit()
path = sys.argv[1]
print("path: " + path)
f = open(path,"r",encoding = "utf-8")
HandlePost(f.read())
f.close()
print("Done.")