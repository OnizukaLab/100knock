import codecs
from random import shuffle

POS_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/rt-polarity.pos"
NEG_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/rt-polarity.neg"
SENTIMENT_TXT_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter7/sentiment.txt"


def read_text_as_sentence_list(path):
    with codecs.open(path, "r", "utf-8") as f: return f.readlines()


def generate_sentiment_from_pos_neg_data():
    pos_raw_text_list = read_text_as_sentence_list(POS_DATA_PATH)
    neg_raw_text_list = read_text_as_sentence_list(NEG_DATA_PATH)
    data = ["+1 " + text for text in pos_raw_text_list] + ["-1 " + text for text in neg_raw_text_list]
    shuffle(data)
    return data


def data_loader():
    with codecs.open(SENTIMENT_TXT_DATA_PATH, "r", "utf-8") as f:
        return f.readlines()


def generate_sentiment_txt():
    data = generate_sentiment_txt()
    with codecs.open(SENTIMENT_TXT_DATA_PATH, "w", "utf-8") as f:
        f.writelines(data)


if __name__ == '__main__':
    generate_sentiment_txt()
