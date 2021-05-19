import markdown2

def markdown2html(text):
    #fix for standard markdown line-break
    #if a line is a part of a table, remove the space in the end for proper rendering
    text = list2str(list = [x.rstrip() if "|" in x else x.rstrip() + "  " for x in text.splitlines()])

    text = markdown2.markdown(
        text, extras=['footnotes', 'tables', 'task_list', 'numbering'])

    text = text.removeprefix("<p>").removesuffix("</p>\n")

    return text

def linestrip(text,l = True, r = True):
    lines = text.splitlines()
    for x in lines:
        if l: x = x.lstrip()
        if r: x = x.rstrip()
    return list2str(lines)

def replaceBrackets(text, spliter,left,right):
    sub = text.split(spliter)
    output = ""
    for i in range(0, len(sub)):
        if(i % 2 == 1):
            output = output + left + sub[i] + right
        else: output = output + sub[i]
    return output

def list2str(list, l='', r='\n',removeSuffix = True):
    output = ""
    for x in list:
        output = output + l + x + r
    if removeSuffix: output = output.removesuffix(r)
    return output

def formatText(text):
    lines = [x.rstrip() for x in text.splitlines()]

    if len(lines) <= 0: return "" 

    #add line-break for list and table
    inList,inTable = False,False

    text = ""
    # table start tweak. if a table starts from the first line, it won't be rendered as an empty line is added at first
    if inTable == False and "|" in lines[0] and 1 < len(lines) and "|" in lines[1] and "-" in lines[1]: #table start
        text = text + "\n"
        inTable = True
    text = lines[0]

    for i in range(1, len(lines)):
        if inTable == False and inList == False and '- ' not in lines[i - 1] and '- ' in lines[i]: #list start
            text = text + '\n'
            inList = True
        if inList and "- " not in lines[i]: #list end
            text = text + "\n"
            inList = False
        if inTable == False and "|" in lines[i] and i + 1 < len(lines) and "|" in lines[i+1] and "-" in lines[i+1]: #table start
            text = text + "\n"
            inTable = True
        if inTable and "|" not in lines[i]:
            text = text + "\n"
            inTable = False
        text = text + '\n' + lines[i]

    text = markdown2html(text)
    text = replaceBrackets(text,'$','\\(','\\)')
    return text