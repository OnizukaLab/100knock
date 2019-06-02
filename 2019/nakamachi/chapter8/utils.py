import codecs
import pickle

import pandas as pd

RAW_DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/enwiki-20150112-400-r100-10576.txt"
DATA_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/enwiki-r100-tokenized.txt"
COUNTRY_LIST_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/country_list.csv"
WORD_CONTEXT_TAB_FILE_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/word_context_tab.txt"
COUNTER_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/counter.pkl"
MATRIX_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/matrix.pkl"
PRINCIPAL_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/pc_vec.pkl"
MATRIX_OBJ_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/matrix_obj.pkl"
TERM_LIST_PATH = "/Users/reiven/Documents/Python/100knock/data/chapter8/term_list.pkl"


def load_text(filepath):
    with codecs.open(filepath, "r", "utf-8") as f:
        return f.read()


def save_text(filepath, text):
    with codecs.open(filepath, "w", "utf-8") as f:
        f.write(text)


def load_pickle_object(filepath):
    with open(filepath, "rb") as f:
        obj = pickle.load(f)
        return obj


def save_pickle_object(filepath, obj):
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)


def load_raw_data():
    return load_text(RAW_DATA_PATH)


def load_data():
    return load_text(DATA_PATH)


def save_data(text):
    save_text(DATA_PATH, text)


def save_word_context_tab(text):
    save_text(WORD_CONTEXT_TAB_FILE_PATH, text)


def load_word_context_tab():
    return load_text(WORD_CONTEXT_TAB_FILE_PATH)


def get_country_list():
    df = pd.read_csv(COUNTRY_LIST_PATH)
    return list(df["ISO 3166-1に於ける英語名"])


def save_counter(counter):
    save_pickle_object(COUNTER_PATH, counter)


def load_counter():
    return load_pickle_object(COUNTER_PATH)


def save_matrix(matrix):
    save_pickle_object(MATRIX_PATH, matrix)


def load_matrix():
    return load_pickle_object(MATRIX_PATH)


def save_matrix_obj(matrix):
    save_pickle_object(MATRIX_OBJ_PATH, matrix)


def load_matrix_obj():
    return load_pickle_object(MATRIX_OBJ_PATH)


def save_term_list(term_list):
    save_pickle_object(TERM_LIST_PATH, term_list)


def load_term_list():
    return load_pickle_object(TERM_LIST_PATH)


def save_principal_vector(obj):
    save_pickle_object(PRINCIPAL_PATH, obj)


def load_principal_vector():
    return load_pickle_object(PRINCIPAL_PATH)


if __name__ == '__main__':
    pass
    # print(load_matrix().matrix)
