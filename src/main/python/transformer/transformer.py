import re


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

def replace_chars(line):
    line = re.sub(r"{\d*,*\s*\d*}", "", line)
    line = line.replace("\n", "")
    line = (line
            .replace("÷", "ʔ")
            .replace("(PLB)", "")
            .replace("TM", "2"))
    line = re.sub(r"\s+", " ", line).strip()
    return line

def to_csv(line):
    if line.startswith('*'):
        parts = line.split(" ")
        if len(parts) > 1:
            item = line.split(" ")[0]
            meaning = line.split(" ")[1]
            return item + ";" + meaning
    return ""