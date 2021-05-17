def replaceBrackets(text, spliter,left,right):
    sub = text.split(spliter)
    output = ""
    for i in range(0, len(sub)):
        if(i % 2 == 1):
            output = output + left + sub[i] + right
        else: output = output + sub[i]
    return output

def list2str(list,l = '<div>', r = '</div>'):
    output = ""
    for x in list:
        output = output + l + x + r
    return output

def formatText(text, linebreak = True):
    text = replaceBrackets(text,"**","<b>","</b>")
    text = replaceBrackets(text,'$','\\(','\\)')
    text = list2str([x.strip() for x in text.splitlines()], '', '\n')
    text = text.strip()
    if linebreak:
        text = text.replace("\n","<br>")
    return text
