from lxml import etree

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    for word in root.xpath('//word'):
        print(word.text)
