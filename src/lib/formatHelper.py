import markdown2

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
    return output.strip(' \n')

def remove_front(text, string):
    if len(text) >= len(string) and text[0 : len(string)] == string:
        return text[len(string) : len(text)]
    return text
        
def remove_back(text, string):
    if len(text) >= len(string) and text[len(text) - len(string) : len(text)] == string:
        return text[0 : len(text) - len(string)]
    return text

def formatText(text):
    lines = [x.rstrip() for x in text.splitlines()]
    text = lines[0]
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
    text = text.strip()
    text = markdown2.markdown(text, extras = ['footnotes', 'tables', 'task_list', 'numbering'])
    text = remove_front(text, '<p>')
    text = remove_back(text, '</p>\n')
    return replaceBrackets(text,'$','\\(','\\)')
