import re

with open('../../../data/enwikidata/country_list.txt', 'r') as country_f:
    country_list = [country for country in country_f.read().split('\n') if len(country.split(' ')) > 1]


def concat_country(text):
    for country in country_list:
        if re.search(country, text):
            text = re.sub(country, '_'.join(country.split(' ')), text)
    return text

def main():
    with open('../../../data/enwikidata/chapter9_corpus.txt', 'r') as f:
        data = f.read().split('\n')

    out_data = [concat_country(line) for line in data]
    with open('../../../data/enwikidata/concat_phrase.txt', 'w') as out_f:
        out_f.write('\n'.join(out_data))



if __name__ == '__main__':
    main()