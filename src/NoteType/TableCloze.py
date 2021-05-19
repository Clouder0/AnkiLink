from .Cloze import ClozeNote

def check(lines):
    if len(lines) < 3: return False
    return "|" in lines[0] and "|" in lines[1] and "-" in lines[1] and "|" in lines[2]

def get(text):
    sub = text.split("**")
    output = ""
    if len(sub) == 0: raise Exception("Invalid Table Cloze format, skipping.")
    # odd indexes are clozes
    for i in range(0,len(sub)):
        if(i % 2 == 1):
            output = output + '{{c' + str(((i + 1) // 2)) + '::' + sub[i] + '}}'
        else: output = output + sub[i]
    return ClozeNote(output)