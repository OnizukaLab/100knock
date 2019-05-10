import re

if __name__ == '__main__':
    with open("../../../data/nlp.txt") as f:
        for line in f:
            s = re.sub("([^.;:?!]*[.;:?!]) ([A-Z])", "\\1\n\\2", line).strip()
            if len(s) > 0:
                print(s)
