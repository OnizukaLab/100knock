from lxml import etree

if __name__ == '__main__':
    root = etree.parse('../../../data/nlp.txt.xml')
    for sentence in root.xpath('//sentence'):
        depdict = {}
        for dep in sentence.xpath('dependencies[@type="collapsed-dependencies"]/dep'):
            type = dep.attrib['type']
            if type == 'nsubj' or type == 'dobj':
                governor = dep.xpath('governor')[0]
                dependent = dep.xpath('dependent')[0]
                if governor.attrib['idx'] in depdict:
                    depdict[governor.attrib['idx']][type] = dependent.text
                else:
                    depdict[governor.attrib['idx']] = {'predicate':governor.text ,type: dependent.text}
                #print('{} : {}({}) -> {}({})'.format(type, governor.text, governor.attrib['idx'], dependent.text, dependent.attrib['idx']))
                #input()
        for k,v in depdict.items():
            if len(v) > 2:
                print('{}\t{}\t{}'.format(v['nsubj'], v['predicate'], v['dobj']))
            #input()
