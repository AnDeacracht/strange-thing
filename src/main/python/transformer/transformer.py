import re
from dataclasses import replace


def import_file_lines(path):
    lines = []
    with open (path, 'r') as file:
        data = file.readlines()
        for line in data:
            line = replace_chars(line)
            line = to_csv(line)
            lines.append(line)
    return lines

def import_file_string(path):
    with open (path, 'r') as file:
        return file.read()
        #print(data)
        #print(r"{}".format(data))

def tokenize(string) -> list[str]:
    return string.split("\n*")

def replace_chars(token):
    token = re.sub(r"{\d*,*\s*\d*}", "", token)
    token = token.replace("\n", "")
    token = (token
             .replace("÷", "ʔ")
             .replace("(PLB)", "")
             .replace("TM", "2"))
    token = re.sub(r"\s+", " ", token).strip()
    return token

def to_csv(token):
    token = replace_chars(token)
    parts = token.split(" ")
    if len(parts) > 1:
        if "&" in parts:
            item = token.replace("&", "~")
            meaning = ""
            return item + ";" + meaning + " \n"
        else:
            item = token.split(" ")[0]
            meaning = token.split(" ")[1].replace("'", "")
            return item + ";" + meaning + "\n"
    return token + "; \n"