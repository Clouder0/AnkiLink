import markdown2

# python version is 3.7, so str.removesuffix/prefix is not supported.


def removeSuffix(text: str, suffix: str) -> str:
    if not text.endswith(suffix):
        return text
    return text[:len(text) - len(suffix)]


def removePrefix(text, prefix):
    if not text.startswith(prefix):
        return text
    return text[len(prefix):]


def markdown2html(text):
    # fix for standard markdown line-break
    # if a line is a part of a table, remove the space in the end
    text = list2str([x.rstrip() if "|" in x
                     else x.rstrip() + "  " for x in text.splitlines()])

    text = markdown2.markdown(
        text, extras=["footnotes", "tables", "task_list", "numbering", "code-friendly"])

    text = removeSuffix(removePrefix(text, "<p>"), "</p>\n")

    return text


def linestrip(text, left=True, right=True):
    lines = text.splitlines()
    for x in lines:
        if left:
            x = x.lstrip()
        if right:
            x = x.rstrip()
    return list2str(lines)


def replaceBrackets(text, spliter, left, right):
    sub = text.split(spliter)
    output = ""
    flag = False
    for x in sub:
        output += left + x + right if flag else x
        flag = not flag
    return output


def list2str(target, left="", right="\n", keepsuffix=False):
    output = ""
    for x in target:
        output = output + left + x + right
    if not keepsuffix:
        output = removeSuffix(output, right)
    return output


def lineTweaks(lines: list) -> str:
    # add line-break for list and table
    inList, inTable = False, False
    text = ""
    # table start tweak. if a table starts from the first line,
    # #it won"t be rendered as an empty line is added at first
    # table start
    if not inTable and "|" in lines[0] and \
            1 < len(lines) and "|" in lines[1] and "-" in lines[1]:
        text = text + "\n"
        inTable = True
    text = lines[0]

    def isListStart(index: int) -> bool:
        return not inTable and not inList and \
            "- " not in lines[index - 1] and "- " in lines[index]

    def isListEnd(index: int) -> bool:
        return inList and "- " not in lines[index]

    def isTableStart(index: int) -> bool:
        return not inTable and "|" in lines[index] and index + 1 < len(lines)\
            and "|" in lines[index + 1] and "-" in lines[index + 1]

    def isTableEnd(index: int) -> bool:
        return inTable and "|" not in lines[index]

    for i in range(1, len(lines)):
        # list start
        if isListStart(i):
            text = text + "\n"
            inList = True
        elif isListEnd(i):
            text = text + "\n"
            inList = False
        elif isTableStart(i):
            text = text + "\n"
            inTable = True
        elif isTableEnd(i):
            text = text + "\n"
            inTable = False
        text = text + "\n" + lines[i]

    return text


def formatText(text):
    lines = [x.rstrip() for x in text.splitlines()]

    if len(lines) <= 0:
        return ""

    text = lineTweaks(lines)  # tweak for tables and lists
    text = markdown2html(text)
    text = replaceBrackets(text, "$", "\\(", "\\)")
    return text


def getTitle(text: str):
    lines = text.splitlines()
    for x in lines:
        if x.startswith("# "):
            return x[2:].strip()
    return None
