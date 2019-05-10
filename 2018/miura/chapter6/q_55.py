from lxml import etree

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    for token in root.xpath('//token'):
        if token.xpath('NER')[0].text == 'PERSON':
            print(token.xpath('word')[0].text)
