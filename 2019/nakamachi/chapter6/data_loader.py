import codecs
import xml.etree.ElementTree as ET

RAW_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter6/nlp.txt"
XML_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter6/nlp.txt.xml"

def data_loader(xml_version_flg=False):
    if xml_version_flg:
        with codecs.open(XML_DATA_PATH, "r", "utf-8") as f:
            return ET.fromstring(f.read())
    with codecs.open(RAW_DATA_PATH, "r", "utf-8") as f:
        return f.read()  # どうせメモリに全部乗るのでデータをやっちゃう

