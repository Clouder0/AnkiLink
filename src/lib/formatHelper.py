import markdown2

def markdown2html(text):
    #fix for standard markdown line-break
    text = list2str(list = [x.rstrip() for x in text.splitlines()])

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

    text = lines[0]
    #add line-break for list and table
    for i in range(1, len(lines)):
        if '- ' not in lines[i - 1] and '- ' in lines[i]:
            text = text + '\n\n' + lines[i]
        elif i + 1 < len(lines) and \
        lines[i - 1] != '' and \
        '|' not in lines[i - 1] and \
        '|' in lines[i] and \
        '|' in lines[i + 1]:
            text = text + '\n\n' + lines[i]
        else: text = text + '\n' + lines[i]

    text = markdown2html(text)
    text = replaceBrackets(text,'$','\\(','\\)')
    return text