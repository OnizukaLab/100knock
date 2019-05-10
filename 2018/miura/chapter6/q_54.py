from lxml import etree

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    for token in root.xpath('//token'):
        print('{}\t{}\t{}'.format(token.xpath('word')[0].text, token.xpath('lemma')[0].text, token.xpath('POS')[0].text))
