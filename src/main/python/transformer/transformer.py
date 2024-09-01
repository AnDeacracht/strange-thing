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

# new entries are marked by * followed by newline... hopefully
def tokenize(string) -> list[str]:
    return string.split("\n*")

def replace_chars(token):
    token = kill_numbers_between_braces(token)
    token = kill_plb(token)
    token = kill_newline(token)
    token = (token
             .replace("÷", "ʔ")
             .replace("TM", "2")
             .replace("≥", "ŋ")
             )
    token = collapse_multiple_spaces(token)
    return token


def kill_newline(token):
    return token.replace("\n", "")


def kill_plb(token):
    return token.replace("(PLB)", "")


def collapse_multiple_spaces(token):
    return re.sub(r"\s+", " ", token).strip()


def kill_numbers_between_braces(token):
    return re.sub(r"{\d*,*\s*\d*}", "", token)


def to_csv(token):
    return convert_to_csv(token).replace("pre-fix", "prefix")


def convert_to_csv(token):
    token = replace_chars(token)
    parts = token.split(" ")
    parts_if_with_meaning = token.split("'")
    if len(parts) > 1:
        # multiple entries joined by the funny sign which becomes & in text, but not translation
        if "&" in parts:
            item = token.replace("&", "~")
            meaning = " "
            # multiple entries joined by the funny sign which becomes & in text, and with translation
            if len(parts_if_with_meaning) > 1:
                item = parts_if_with_meaning[0].replace("&", "~")
                meaning = parts_if_with_meaning[1].replace("'", "")
            csv_entry = item + ";" + meaning + "\n"
            return csv_entry.replace(" ;", ";")
        # actual entries with translation
        else:
            item = token.split(" ")[0]
            meaning = token.split(" ")[1].replace("'", "")
            return item + ";" + meaning + "\n"
    # heading
    return token + "; \n"