import xml.etree.ElementTree as ET

def readXML(path):
    with open(path) as f:
        XmlData = f.read()
    return ET.fromstring(XmlData)


if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")

    for e in root.findall(".//word"):
        print(e.text)
