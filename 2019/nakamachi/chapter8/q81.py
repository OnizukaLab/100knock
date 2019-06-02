"""
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．

<https://gist.github.com/cupnoodlegirl/ba10cf7a412a1840714c>
"""
from utils import get_country_list, load_data
from q80 import tokenize_sentence

# from rake_nltk import Rake
#
# r = Rake()
# test = "United_States Isle of Man but I use in natural language processing"
# r.extract_keywords_from_text(test)
# print(get_country_list())

def modify_country_name_term(text_list):
    country_list = get_country_list()
    text = " ".join(text_list)
    for country in country_list:
        text = text.replace(country, "_".join(country.split()))
    return text.split()


def main():
    data = load_data().split()
    return modify_country_name_term(data)

if __name__ == '__main__':
    test = "United_States Isle of Man but I use in natural language processing"
    test = tokenize_sentence(test)
    print(modify_country_name_term(test))
    # for key in main():
    #     if key == "United_States":
    #         print(key)